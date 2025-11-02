# 🔍Net_Scan  
![](/media1.PNG)

# About
### A lightweight, fast, and beginner-friendly **Port Scanner** and **Subdomain Scanner** written in Python — designed for CTFs, network assessments.

---

##  Features

-  Fast scanning
-  Subdomain enumeration with HTTP/HTTPS fallback
-  Verbose mode 
-  colored output for clarity
-  Works platform (tested on Linux, Windows, Arch VM)

---

##  Tools Included

### 1. Net_Scan (Port Scanner)

Scans TCP ports for a given host using multithreading.

### 2. Net_Scan (Subdomain Scanner)

Discovers live subdomains from a wordlist using HTTP & HTTPS methods.

##  Requirements

- Python 3.x
- [`termcolor`]
- [`requests`]

## Install dependencies
```
pip install requests termcolor
```
##  Installation
> 1. Clone the repository:
   ```bash
   git clone https://github.com/knightc0de/Net_scan.git
   cd Net_scan
  ```
### lauch script
> 2. A simple Net_scan.sh launcher script allows selection between scanners with interactive options.
```
chmod 700 Net_scan.sh
./Net_scan.sh

```
# 👨‍💻Author 
### @Knightc0de

