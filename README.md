# 🧅Tor Expert Bundle + Vivaldi + obfs4 Bridges on Windows

<img width="1400" height="500" alt="image" src="https://github.com/user-attachments/assets/aa6daaa9-d2dc-41d4-9516-7257305e0055" />

*This guide explains how to configure Tor Expert Bundle with **obfs4** bridges combined with Vivaldi Browser via SOCKS5. It includes fetching bridges, compiling obfs4proxy, and full browser configuration.*

<details>
<summary>📥 1. Download Tor Expert Bundle</summary>

1. *Go to the official website:* [Tor Project - Expert Bundle](https://www.torproject.org/download/tor/).  
2. *Download* **Windows Expert Bundle** (not Tor Browser).  
3. *Extract the archive, for example into:*  

```
C:\Users\<YourName>\Downloads\tor-expert-bundle-windows-i686-14.5.6\tor
```
</details>

<details>
<summary>🛠 2. Compile obfs4proxy.exe</summary>

1. *The binary `obfs4proxy.exe` is not included in the Expert Bundle.*  
2. *Fetch the source code from GitHub:* [Yawning/obfs4](https://github.com/Yawning/obfs4?utm_source=chatgpt.com)  
3. *Install **Go** for Windows:* [https://golang.org/dl/](https://golang.org/dl/)  
4. *Open `cmd.exe` in the project folder and compile:*  

```cmd
go build -o obfs4proxy.exe ./obfs4proxy
```

5. *Place the compiled file into the Tor Expert Bundle folder, for example:*  

```
C:\Users\<YourName>\Downloads\tor-expert-bundle-windows-i686-14.5.6\tor
```
</details>

<details>
<summary>⭐ 2Bonus. Download Everything</summary>

```powershell
$DownloadPath = [Environment]::GetFolderPath("UserProfile") + "\Downloads"

if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
    $GitUrl = "https://github.com/git-for-windows/git/releases/latest/download/Git-2.47.0-64-bit.exe"
    $GitInstaller = Join-Path $DownloadPath "git-installer.exe"
    Invoke-WebRequest -Uri $GitUrl -OutFile $GitInstaller
    Start-Process -FilePath $GitInstaller -ArgumentList "/VERYSILENT" -Verb RunAs -Wait
}

$TorUrl = "https://archive.torproject.org/tor-package-archive/torbrowser/14.5.6/tor-expert-bundle-windows-i686-14.5.6.tar.gz"
$TorFile = Join-Path $DownloadPath "tor-expert-bundle-windows-i686-14.5.6.tar.gz"

if (-not (Test-Path $TorFile)) {
    Invoke-WebRequest -Uri $TorUrl -OutFile $TorFile
}

try {
    $TorExtractPath = Join-Path $DownloadPath "tor-expert-bundle"
    if (Test-Path $TorExtractPath) { Remove-Item -Recurse -Force $TorExtractPath }
    mkdir $TorExtractPath | Out-Null
    tar -xzf $TorFile -C $TorExtractPath
} catch {}

Set-Location $DownloadPath
$Obfs4Path = Join-Path $DownloadPath "obfs4"
if (Test-Path $Obfs4Path) {
    Remove-Item -Recurse -Force $Obfs4Path
}
git clone "https://github.com/Yawning/obfs4.git"

$GoUrl = "https://go.dev/dl/go1.25.0.windows-amd64.msi"
$GoInstaller = Join-Path $DownloadPath "go1.25.0.windows-amd64.msi"

if (-not (Test-Path $GoInstaller)) {
    Invoke-WebRequest -Uri $GoUrl -OutFile $GoInstaller
}

Start-Process -FilePath "msiexec.exe" -ArgumentList "/i `"$GoInstaller`" /qn" -Verb RunAs -Wait
```
</details>

<details>
<summary>🌉 3. Configure torrc with obfs4 bridges</summary>

*Create or edit the `torrc` file in:*  

```
C:\Users\<YourName>\AppData\Roaming\tor\torrc
```

*Minimal example:*  

```txt
SocksPort 9050
UseBridges 1
ClientTransportPlugin obfs4 exec C:\Users\<YourName>\Downloads\tor-expert-bundle-windows-i686-14.5.6\tor\obfs4proxy.exe

Bridge obfs4 83.136.106.151:899 9227826C1117020553E6F7ACBBC2CE7EE5FF5595 cert=aM6Vcv8Wx9/gBRlaqz1UQbuOP6EC96VtI/Ll0CJydbJu+mz75ESFl+a8DddZpUXjdDwBRQ iat-mode=0
Bridge obfs4 70.104.192.207:9003 31F79D4C6E831FBDAB5ACAB9DB02B40A6A24E93E cert=KM/Ss74USK7NzzQE40uZEmeSV17dmr8ukI2vsE071gT2qWNPVyLZnzg9rIQcO09FCyvOYA iat-mode=0
```

> ⚠️ *Replace the bridges with the ones you fetch from Tor Browser > Settings > Tor > “Configure a New Bridge” or from* [https://bridges.torproject.org/](https://bridges.torproject.org/).

</details>

<details>
<summary>🚀 4. Start Tor Expert Bundle</summary>

*Open `cmd.exe` and type:*  

```cmd
"C:\Users\<YourName>\Downloads\tor-expert-bundle-windows-i686-14.5.6\tor\tor.exe" -f "C:\Users\<YourName>\AppData\Roaming\tor\torrc"
```

* *Wait until the log shows* **Bootstrapped 100%**.

</details>

<details>
<summary>🌐 5. Start Vivaldi via SOCKS5</summary>

*In a new cmd, type:*  

```cmd
"C:\Users\<YourName>\AppData\Local\Vivaldi\Application\vivaldi.exe" --proxy-server="socks5://127.0.0.1:9050" --proxy-bypass-list="<-loopback>"
```

* *Check your anonymity on* [https://check.torproject.org](https://check.torproject.org).

</details>

<details>
<summary>📡 6. Fetch new obfs4 bridges</summary>

1. *Install Tor Browser to get bridges:*  
   * *Open* **Tor Browser > Settings > Tor > Configure a New Bridge**  
   * *Choose* **obfs4** and copy the Bridge lines.  

2. *Replace them in your `torrc` with the new bridges.*  

*Example:*  

```txt
Bridge obfs4 83.136.106.151:899 9227826C1117020553E6F7ACBBC2CE7EE5FF5595 cert=... iat-mode=0
Bridge obfs4 70.104.192.207:9003 31F79D4C6E831FBDAB5ACAB9DB02B40A6A24E93E cert=... iat-mode=0
```
</details>

<details>
<summary>💡 Vivaldi Browser Settings</summary>

[🎥 Video](https://github.com/user-attachments/assets/79c69fa0-e59c-4bfa-b81c-32ad6eb3d6e7)

</details>

<details>
<summary>🏬 Vivaldi Browser Extensions</summary>

1. [uBlock Origin](https://chromewebstore.google.com/detail/ublock-origin-lite/ddkjiahejlhfcafbddmgiahcphecmpfh?hl=en)  
   *Blocks ads, trackers, malicious scripts.*  

2. [Privacy Badger](https://chromewebstore.google.com/detail/privacy-badger/pkehgijcmpdhfbdbbnkijodmdjhbjlgp?hl=en)  
   *Blocks trackers automatically.*  

3. [Decentraleyes](https://chromewebstore.google.com/detail/decentraleyes/ldpochfccmkkmhdbclfhpagapcfdljkj/support)  
   *Avoids connections to external CDN servers by serving local resources.*  

</details>

<details>
<summary>🚀 Launcher Vivaldi Browser</summary>

1. *Clone mon github:*
```cmd
git clone https://github.com/datadr1p/OpsecVivaldiBrowser
```

2. *Execute VivaldiBrowserLauncher.exe*

3. *Si tu n'as pas confiance, c'est un simple script python, tu peux le decompilé via pyinstaller*
```cmd

```

</details>
<details> 
<summary>🚀 Vivaldi Browser Launcher</summary>

1. *Clone my GitHub:*
```cmd
git clone https://github.com/datadr1p/OpsecVivaldiBrowser
```
1.2 *Open the folder and open the cmd in the folder and install nuitka.*
```cmd
pip install nuitka
```
1.3 *Compile the .py into .exe*
```cmd
python -m nuitka --onefile --windows-icon-from-ico=vivaldi.ico VivaldiBrowserLauncher.py
```
2. *Run VivaldiBrowserLauncher.exe*
3. *Put the .exe you compiled in in the start menu*
```cmd
%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\
```
