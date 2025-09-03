import os
import subprocess
import time
import re
import psutil

def find_file(filename, search_paths):
    for path in search_paths:
        for root, dirs, files in os.walk(path):
            if filename in files:
                return os.path.join(root, filename)
    return None

def wait_for_tor_bootstrap(process):
    while True:
        line = process.stdout.readline()
        if not line:
            break
        decoded = line.decode(errors="ignore").strip()
        print(decoded)
        if re.search(r"Bootstrapped 100%", decoded):
            print("[+] Tor is fully bootstrapped!")
            break

def kill_process_by_name(name):
    for proc in psutil.process_iter(['name']):
        if proc.info['name'] and name.lower() in proc.info['name'].lower():
            try:
                proc.kill()
            except:
                pass

def main():
    user = os.getenv("USERNAME")
    downloads = os.path.join("C:\\Users", user, "Downloads")
    appdata_roaming = os.path.join("C:\\Users", user, "AppData", "Roaming", "tor")
    appdata_local = os.path.join("C:\\Users", user, "AppData", "Local")

    print("[*] Searching for tor.exe")
    tor_exe = find_file("tor.exe", [downloads])
    if not tor_exe:
        print("[-] tor.exe not found in Downloads")
        return
    print(f"[+] Found tor.exe: {tor_exe}")

    torrc_path = os.path.join(appdata_roaming, "torrc")
    if not os.path.exists(torrc_path):
        print(f"[-] torrc not found in {appdata_roaming}")
        return
    print(f"[+] Found torrc: {torrc_path}")

    kill_process_by_name("tor.exe")
    print("[*] Starting Tor")
    tor_process = subprocess.Popen(
        [tor_exe, "-f", torrc_path],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        creationflags=subprocess.CREATE_NEW_CONSOLE
    )
    wait_for_tor_bootstrap(tor_process)

    print("[*] Searching for Vivaldi.exe")
    vivaldi_exe = find_file("vivaldi.exe", [appdata_local])
    if not vivaldi_exe:
        print("[-] Vivaldi not found in AppData\\Local")
        return
    print(f"[+] Found Vivaldi: {vivaldi_exe}")

    kill_process_by_name("vivaldi.exe")
    print("[*] Starting Vivaldi")
    subprocess.Popen([
        vivaldi_exe,
        "--proxy-server=socks5://127.0.0.1:9050",
        "--proxy-bypass-list=<-loopback>"
    ])

    print("[✓] All done! Vivaldi is running through Tor.")

if __name__ == "__main__":
    main()
