import subprocess
import time
import datetime
import os
from google import genai

TARGET_HOST = "jarvisv3@192.168.1.47"
CHECK_INTERVAL = 60
LOG_FILE = r"C:\Users\Hari\pi-repair-agent\repair_agent.log"

client = genai.Client()

def log_event(message):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_line = f"[{timestamp}] {message}"
    with open(LOG_FILE, "a") as f:
        f.write(log_line + "\n")

def run_remote_cmd(command, timeout=30):
    try:
        cmd = ["ssh", TARGET_HOST, command]
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout, creationflags=subprocess.CREATE_NO_WINDOW)
        return result.stdout.strip(), result.stderr.strip(), result.returncode
    except Exception as e:
        return "", str(e), -1

def check_container_health(container_name):
    cmd = 'docker inspect --format="{{.State.Status}}" ' + container_name
    stdout, stderr, code = run_remote_cmd(cmd, timeout=10)
    if code == 0 and stdout:
        return stdout.strip()
    return "missing"

def get_container_logs(container_name):
    stdout, _, _ = run_remote_cmd(f"docker logs --tail 40 {container_name}", timeout=15)
    return stdout

def ask_gemini_for_fix(container_name, logs):
    log_event(f"Consulting Gemini AI for diagnosis on '{container_name}'...")
    prompt = f"""
    You are an expert DevOps engineer managing a Raspberry Pi Docker host.
    The container '{container_name}' is unhealthy or stopped. Here are the last container logs:
    {logs}

    Provide ONLY a single, valid, safe bash command to fix or restart this specific container (e.g., docker restart {container_name}).
    Do not include markdown code blocks, explanations, or extra text. Just output the raw shell command.
    """
    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt,
        )
        command = response.text.strip().replace("`ash", "").replace("`", "").strip()
        return command if command else f"docker restart {container_name}"
    except Exception as e:
        log_event(f"Gemini API error: {e}. Falling back to standard restart.")
        return f"docker restart {container_name}"

def remediate_service(container_name):
    log_event(f"ALERT: Container '{container_name}' on the Pi is down. Gathering logs for AI analysis...")
    logs = get_container_logs(container_name)

    fix_command = ask_gemini_for_fix(container_name, logs)
    log_event(f"Executing AI-suggested remediation: {fix_command}")

    stdout, stderr, code = run_remote_cmd(fix_command, timeout=45)
    if code == 0:
        log_event(f"SUCCESS: Remediation applied for '{container_name}'. Output: {stdout}")
    else:
        log_event(f"FAILURE: Remediation failed for '{container_name}': {stderr}")

def main():
    log_event("HP Z240 AI-Powered Agentic Repair Loop initialized (Invisible Mode).")
    monitored_services = ["pihole", "dashlit", "vaultwarden", "uptime-kuma"]

    while True:
        for service in monitored_services:
            status = check_container_health(service)
            if status != "running":
                remediate_service(service)
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    main()
