[![GitHub stars](https://img.shields.io/github/stars/Gameye98/hlrlookup.svg)](https://github.com/Gameye98/hlrlookup/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/Gameye98/hlrlookup.svg)](https://github.com/Gameye98/hlrlookup/network/members)
[![GitHub issues](https://img.shields.io/github/issues/Gameye98/hlrlookup.svg)](https://github.com/Gameye98/hlrlookup/issues)
[![GitHub watchers](https://img.shields.io/github/watchers/Gameye98/hlrlookup.svg)](https://github.com/Gameye98/hlrlookup/watchers)
[![Python](https://img.shields.io/badge/language-Python%203-blue.svg)](https://www.python.org)
[![WTFPL](https://img.shields.io/badge/license-WTFPL-red.svg)](http://www.wtfpl.net/)
[![BlackHole Security](https://img.shields.io/badge/team-BlackHole%20Security-ocean.svg)](https://github.com/BlackHoleSecurity)
[![Gameye98/DedSecTL](https://img.shields.io/badge/author-Gameye98/DedSecTL-red.svg)](https://github.com/Gameye98)

[![ForTheBadge built-by-developers](http://ForTheBadge.com/images/badges/built-by-developers.svg)](https://github.com/Gameye98)  

[![BlackHole Security](.gitbhs.svg)](https://github.com/BlackHoleSecurity)

# HLR Lookup
This Python script performs HLR (Home Location Register) lookups to validate mobile phone numbers, check if they are active, and retrieve information about the carrier. It can be used to streamline SMS campaigns or for number verification purposes.

*note: only works for Indonesia Phone Numbers

```bash
 _   _     _         _
| |_| |___| |___ ___| |_ _ _ ___
|   | |  _| | . | . | '_| | | . |
|_|_|_|_| |_|___|___|_,_|___|  _|
Author: Gameye98 2024/10/16 |_|

Operator: Telkomunikasi Seluler (Telkomsel) - KartuHALO/Simpati/KartuAS
HLR     : JAKARTA, Indonesia
```

## Installation and Usage
- For Linux
```bash
$ sudo apt-get update && sudo apt-get upgrade -y
$ sudo apt-get install python3 git
$ git clone https://github.com/Gameye98/hlrlookup
$ python3 hlrlookup.py 08xxxxxxx
```
- For Termux
```bash
$ apt update && apt upgrade -y
$ apt install python git
$ git clone https://github.com/Gameye98/hlrlookup
$ python hlrlookup.py 08xxxxxxx
```
