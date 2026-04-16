QRJacker 🛡️
QRJacker is a modular Python-based framework designed for browser automation research and educational security testing. It integrates Selenium for browser control, Flask for serving web templates, and Cloudflare Tunnels to provide secure, public access to local services without port forwarding.

🚀 Features
Multi-Platform Stubs: Menu support for WhatsApp, Telegram, TikTok, and Instagram.

Dynamic Payload Selection: Choose between different social engineering templates (e.g., "Gift Win" or "Free Data") via the command-line interface.

Automated Tunneling: Integrated cloudflared setup that automatically detects system architecture and generates a public .trycloudflare.com URL.

Real-time QR Sync: Captures and encodes WhatsApp Web QR codes into Base64 format to be displayed on custom Flask landing pages.

🛠️ Prerequisites
This tool is designed for Linux environments (Kali Linux, Ubuntu, etc.).

System Dependencies:

Bash
sudo apt update
sudo apt install chromium-browser chromium-driver wget -y
Python Libraries:

Bash
pip install flask selenium colorama
📂 Project Structure
main.py: The entry point that initializes the banner and main menu.

whatsapp.py: The core engine handling Selenium, the Flask server, and Cloudflare tunnels.

sub_menu.py: Manages the specific campaign selection (e.g., choice of landing page).

payload.py: Bridges the UI menu to the backend execution logic.

banner.py / color.py: Handles terminal aesthetics and randomization.

📥 Installation & Setup
Clone the Repo:

Bash
git clone https://github.com/your-username/QRJacker.git
cd QRJacker
Organize Templates:
Ensure your directory contains a templates/ folder with the following files:

gift.html

free_data.html

Run the Application:

Bash
python3 main.py
⚙️ How It Works
Selection: The user selects a target platform and a specific template from the terminal menu.

Initialization: The script checks for cloudflared. If missing, it downloads the correct version for your architecture (amd64 or arm64).

Automation: A headless or windowed Chrome instance opens WhatsApp Web.

Forwarding: Cloudflare creates a tunnel from your local port 5000 to a public URL.

Access: When a victim visits the public URL, the Flask index route serves the template corresponding to your initial menu choice.

⚠️ Disclaimer
This tool is strictly for educational purposes and authorized security auditing. Unauthorized use of this tool against targets without prior consent is illegal. The developer assumes no liability for misuse or damage caused by this program.
