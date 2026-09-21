# ARDENT JANA: A Low-Resource, Self-Diagnosing, Student-Oriented Homelab System

**TL;DR:** ArdentJana is a fully containerized, AI-monitored homelab ecosystem designed to completely replace costly monthly subscriptions like Google Photos, Apple iCloud, Google Drive, and Spotify. It features an invisible, self-healing AI agent that automatically diagnoses and restarts crashed services, requiring zero manual maintenance.

## The Objective & Use Case
This architecture is built for ultimate accessibility. It is intended for anyone and everyone, regardless of hardware constraints. Whether deployed on a full-grade enterprise server, the aging repurposed PC of a broke pre-med student, or a Raspberry Pi—if you can plug it in and run it 24/7, this infrastructure will work for you.

By self-hosting these open-source tools, students and individuals can outright replace predatory subscription models, saving hundreds of dollars a month. It reclaims vital funds, redirecting them away from corporate monopolies and back into a student's future. 

## The Infrastructure
ArdentJana leverages Docker Compose to manage a lightweight fleet of purpose-built services:

* **Network & Security:** Pi-hole and Dnsmasq handle ad-blocking and local DNS routing, Nginx Proxy Manager securely exposes services, and Vaultwarden self-hosts encrypted password management. 
* **Productivity & Study:** Anki-sync-server keeps critical flashcards updated across devices, Trilium manages hierarchical note-taking, and Kanboard tracks project tasks.
* **Media & Storage:** Navidrome and Audiobookshelf stream personal music and audiobooks, Shairport-sync enables AirPlay capabilities, and Filebrowser provides remote drive access.
* **Monitoring & Automation:** Uptime Kuma and Beszel track system health, Changedetection monitors web alterations, Homebridge bridges smart devices, and Watchdog force-restarts unhealthy containers.

## The AI Agentic Loop
The crown jewel of ArdentJana is the `repair_agent.py` script—an invisible Python background process that acts as the system's autonomic nervous system.
* **Monitor:** It continuously polls the host via SSH to check the health status of mission-critical containers.
* **Diagnose:** If a service crashes, the agent extracts the last 40 lines of the container's logs and feeds them into Google's Gemini 2.5 Flash AI model.
* **Remediate:** Acting as an expert DevOps engineer, the AI analyzes the crash data and generates a precise shell command, which the agent immediately executes on the host to heal the service.

## AI Integration Guide
To deploy the AI repair agent on your own host machine:
1. Install Python and the `google-genai` SDK on the monitoring machine.
2. Store your API token in a secure environment variable (`GEMINI_API_KEY`).
3. Configure `TARGET_HOST` in the script with your server's SSH credentials.
4. Run the script invisibly in the background to enable 24/7 automated remediation.

---

## Philosophy & Origins: Fighting Structural Violence

**Ardent** (*adj.*): Hardworking, passionate.  
**Jana** (*noun, Arabic*): Heaven. 

The name *ArdentJana* translates to a hardworking heaven. But its roots lie in a promise of redemption and a commitment to fighting structural violence.

Let us face the unforgiving reality of modern medicine and higher education: the greatest barrier to entry is not intellect; it is gatekeeping. Nepotism and generational wealth stand as towering sentinels guarding the doors to professional success. The journey is paved with exorbitant tolls—prep courses, exam registrations, application fees, and compounding tuition—that systematically price out the underprivileged. This is structural violence in its most insidious, normalized form: a financial filter masquerading as a meritocracy. 

This project is a direct counter-offensive against those barriers. I built this project to forge an IRL heaven for myself, creating an infrastructure of digital resistance and financial empowerment that makes my daily life—and my path to becoming a pediatric neurosurgeon—sustainable. 

In high school, I reached the top ten nationally in speech and debate. I arrived at that podium, however, through a strategy of ruthless exploitation. I weaponized the mechanics of debate, cornering opponents with arguments that defended the indefensible—running positions like "racism good" or "slavery good" simply to shock, disorient, and mathematically win the round. I won the ballots, defeating even members of the Team USA Olympic squad. But the victories were ashes in my mouth. 

That profound dissonance birthed a reckoning. I made a solemn vow to myself: to repent for the rhetorical violence I had wielded, I would dedicate my life to dismantling structural violence. (I owe a profound debt of gratitude to scholars Deborah DuNann Winter and Dana C. Leighton, whose work illuminated these invisible forces of oppression. I highly urge reading their seminal work: [Section II: Structural Violence](https://bpb-us-w2.wpmucdn.com/u.osu.edu/dist/b/7538/files/2014/10/Section-II-Structural-Violence-Winter-Leighton-28aggie.pdf)).

Growing up, Computer Science was the one class I dropped out of because it felt insurmountable. Yet here stands my first CS triumph—a masterpiece forged over hundreds of hours, made possible by Google Gemini and a free college subscription. I believe with absolute conviction that anyone can create a heaven for themselves, regardless of the cards they are dealt in life. I am open-sourcing this with the hope that it can become a tool of financial and digital liberation for anyone who needs it.

Inspired by Iron Man, the goal was always to build a personal, self-sustaining virtual Jarvis. ArdentJana is the realization of that dream. *(Note: If Jarvis fails one more time, this repository will officially be renamed to Friday).*

**What's Next?**  
This project is just the groundwork. Future projects include building a dedicated AI LLM prompt accelerator to push the boundaries of this ecosystem even further.
