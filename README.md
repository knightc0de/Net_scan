# 🔍Net_Scan  



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

## Install
```
pip install requests termcolor
```
### lauch script
> A simple Net_scan.sh launcher script allows selection between scanners with interactive options.
```
chmod +x Net_scan.sh
./Net_scan.sh

```
# 👨‍💻Author 
### @Knightc0de

