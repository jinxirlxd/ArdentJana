# ArdentJana

**Ardent** (*adj.*): Hardworking, passionate.  
**Jana** (*noun, Arabic*): Heaven. 

The name *ArdentJana* translates to a hardworking heaven. But its roots lie in a promise of redemption. 

In high school, I reached the top ten nationally in speech and debate. I arrived at that podium, however, through a strategy of ruthless exploitation. To win, I weaponized the mechanics of debate, cornering opponents with arguments that defended the indefensible—running positions like "racism good" or "slavery good" simply to shock, disorient, and mathematically win the round. I won the ballots. I even defeated members of the Team USA Olympic squad. But the victories were ashes in my mouth. I hated the moral compromises I had made for the sake of a trophy.

That profound dissonance birthed a reckoning. I made a solemn promise to myself: to repent for the rhetorical violence I had wielded, I would dedicate my life to dismantling *structural violence*. My journey toward pediatric neurosurgery, and the very foundation of this project, are the fulfillment of that vow. 

I owe a profound debt of gratitude to Deborah DuNann Winter and Dana C. Leighton. Your work illuminated the invisible forces of oppression and helped me find my life's true purpose. (For those seeking to understand the framework that drives this mission, I urge you to read their seminal work: [Section II: Structural Violence](https://bpb-us-w2.wpmucdn.com/u.osu.edu/dist/b/7538/files/2014/10/Section-II-Structural-Violence-Winter-Leighton-28aggie.pdf)).

Let us face the unforgiving reality of modern medicine: the greatest barrier to entry is not intellect; it is gatekeeping. Nepotism and generational wealth stand as towering sentinels guarding the doors to medical school. The journey is paved with exorbitant tolls—prep courses, MCAT registrations, application fees, and compounding tuition—that systematically price out the underprivileged. This is structural violence in its most insidious, normalized form: a financial filter masquerading as a meritocracy. 

ArdentJana is a direct counter-offensive against those barriers. I built this project to forge an IRL heaven for myself, creating an infrastructure of resistance and empowerment that makes my daily life—and my path to medicine—sustainable. By self-hosting these tools, a student can replace predatory subscription models outright. This homelab is designed to functionally replace Google Photos, Apple iCloud, Google Drive, Spotify, and Apple Music, saving hundreds of dollars a month. It reclaims those vital funds, redirecting them away from corporate monopolies and back into a student's future. 

I believe with absolute conviction that anyone can create a heaven for themselves, regardless of the cards they are dealt in life. Growing up, Computer Science was the one class I dropped out of because it felt insurmountable. Yet here stands my first CS triumph—a masterpiece forged over hundreds of hours, made possible by the power of Google Gemini and a free college subscription. I am open-sourcing this with the hope that it can become a tool of financial and digital liberation for anyone who needs it.

Inspired by Iron Man, the goal was always to build a personal, self-sustaining virtual Jarvis. ArdentJana is the realization of that dream: a fully containerized ecosystem monitored by an invisible, AI-powered agentic loop. *(Note: If Jarvis fails one more time, this repository will officially be renamed to Friday).*

## The Usecase
This architecture is intended for anyone and everyone, regardless of how massive or modest your hardware might be. From the aging, repurposed PC of a broke pre-med student to a full-grade enterprise server—or even theoretically deployed on an old smartphone—if you can plug it in and run it 24/7, this infrastructure will work for you. It is a low-resource, high-yield sanctuary built for ultimate accessibility.

## The Infrastructure
ArdentJana leverages Docker Compose to manage a lightweight fleet of purpose-built services:

* **Network & Security:** Pi-hole and Dnsmasq handle ad-blocking and local DNS routing, while Nginx Proxy Manager securely exposes services. Vaultwarden self-hosts encrypted password management. 
* **Productivity & Study:** Anki-sync-server keeps critical medical flashcards updated across devices, Trilium manages hierarchical note-taking, and Kanboard tracks project tasks.
* **Media & Storage:** Navidrome and Audiobookshelf stream personal music and audiobooks, Shairport-sync enables AirPlay capabilities, and Filebrowser provides remote drive access.
* **Monitoring & Automation:** Uptime Kuma and Beszel track system health, Changedetection monitors web alterations, Homebridge bridges smart devices, and Watchdog force-restarts unhealthy containers.

## The AI Agentic Loop
The crown jewel of ArdentJana is the `repair_agent.py` script—an invisible Python background process that acts as the system's brain. 
* **Monitor:** It continuously polls the Raspberry Pi via SSH to check the health status of mission-critical containers.
* **Diagnose:** If a service crashes, the agent extracts the last 40 lines of the container's logs and feeds them into Google's Gemini 2.5 Flash model.
* **Remediate:** Acting as an expert DevOps engineer, the AI analyzes the crash data and generates a precise shell command, which the agent immediately executes on the Pi to heal the service.

## AI Integration Guide
To deploy the AI repair agent on your own host machine:
1. Install Python and the `google-genai` SDK on the monitoring machine.
2. Store your API token in a secure environment variable (`GEMINI_API_KEY`).
3. Configure `TARGET_HOST` in the script with your Pi's SSH credentials.
4. Run the script invisibly in the background to enable 24/7 automated remediation.

## What's Next?
This project is just the groundwork. Stay tuned—future projects include building a dedicated AI LLM prompt accelerator to push the boundaries of this ecosystem even further.
