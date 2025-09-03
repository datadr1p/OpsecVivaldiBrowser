# Tor Expert Bundle + Vivaldi via obfs4 Bridges sur Windows

<img width="1280" height="691" alt="image" src="https://github.com/user-attachments/assets/aa6daaa9-d2dc-41d4-9516-7257305e0055" />

Ce guide explique comment configurer Tor Expert Bundle avec des ponts **obfs4** + Vivaldi via SOCKS5. Ce guide inclut la récupération des bridges, la compilation d'obfs4proxy, et la configuration complète du naviguateur.

<details>
<summary>📥 1. Télécharger Tor Expert Bundle</summary>

1. Rendez-vous sur le site officiel : [Tor Project - Expert Bundle](https://www.torproject.org/download/tor/).
2. Téléchargez **Windows Expert Bundle** (pas le Tor Browser).
3. Extrayez l’archive, par exemple dans :

```
C:\Users\<VotreNom>\Downloads\tor-expert-bundle-windows-i686-14.5.6\tor
```

</details>

<details>
<summary>🛠 2. Compiler obfs4proxy.exe</summary>

1. Le binaire `obfs4proxy.exe` n’est pas inclus dans l’Expert Bundle.
2. Récupérez le code source depuis GitHub : [Yawning/obfs4](https://github.com/Yawning/obfs4?utm_source=chatgpt.com)
3. Installez **Go** pour Windows : [https://golang.org/dl/](https://golang.org/dl/)
4. Ouvrez `cmd.exe` dans le dossier du projet et compilez :

```cmd
go build -o obfs4proxy.exe ./obfs4proxy
```

5. Placez le fichier compilé dans le dossier Tor Expert Bundle, par exemple :

```
C:\Users\<VotreNom>\Downloads\tor-expert-bundle-windows-i686-14.5.6\tor
```

</details>

<details>
<summary>🌉 3. Configurer torrc avec des ponts obfs4</summary>

Créez ou éditez le fichier `torrc` dans :

```
C:\Users\<VotreNom>\AppData\Roaming\tor\torrc
```

Exemple minimal :

```txt
SocksPort 9050
UseBridges 1
ClientTransportPlugin obfs4 exec C:\Users\<VotreNom>\Downloads\tor-expert-bundle-windows-i686-14.5.6\tor\obfs4proxy.exe

Bridge obfs4 83.136.106.151:899 9227826C1117020553E6F7ACBBC2CE7EE5FF5595 cert=aM6Vcv8Wx9/gBRlaqz1UQbuOP6EC96VtI/Ll0CJydbJu+mz75ESFl+a8DddZpUXjdDwBRQ iat-mode=0
Bridge obfs4 70.104.192.207:9003 31F79D4C6E831FBDAB5ACAB9DB02B40A6A24E93E cert=KM/Ss74USK7NzzQE40uZEmeSV17dmr8ukI2vsE071gT2qWNPVyLZnzg9rIQcO09FCyvOYA iat-mode=0
```

> ⚠️ Remplacez les bridges par ceux que vous récupérez depuis Tor Browser > Settings > Tor > “Configure a New Bridge” ou depuis [https://bridges.torproject.org/](https://bridges.torproject.org/).

</details>

<details>
<summary>🚀 4. Lancer Tor Expert Bundle</summary>

Ouvrez `cmd.exe` et tapez :

```cmd
"C:\Users\<VotreNom>\Downloads\tor-expert-bundle-windows-i686-14.5.6\tor\tor.exe" -f "C:\Users\<VotreNom>\AppData\Roaming\tor\torrc"
```

* Attendez que le log affiche **Bootstrapped 100%**.

</details>

<details>
<summary>🌐 5. Lancer Vivaldi via SOCKS5</summary>

Dans un nouveau cmd, tapez :

```cmd
"C:\Users\<VotreNom>\AppData\Local\Vivaldi\Application\vivaldi.exe" --proxy-server="socks5://127.0.0.1:9050" --proxy-bypass-list="<-loopback>"
```

* Vérifiez votre anonymat sur [https://check.torproject.org](https://check.torproject.org).

</details>

<details>
<summary>📡 6. Récupérer de nouveaux bridges obfs4</summary>

1. Installez Tor Browser pour obtenir des bridges :

   * Ouvrez **Tor Browser > Settings > Tor > Configure a New Bridge**
   * Choisissez **obfs4** et copiez les lignes Bridge.
2. Remplacez-les dans votre `torrc` avec les ponts “faux” ou de test.

Exemple à copier-coller :

```txt
Bridge obfs4 83.136.106.151:899 9227826C1117020553E6F7ACBBC2CE7EE5FF5595 cert=... iat-mode=0
Bridge obfs4 70.104.192.207:9003 31F79D4C6E831FBDAB5ACAB9DB02B40A6A24E93E cert=... iat-mode=0
```

</details>

<details>
<summary>💡 Paramètre Vivaldi</summary>

</details>
