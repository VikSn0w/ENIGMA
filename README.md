# 🛡️ Enigma Token Generator

This project includes **three different versions** of an `Enigma` token generator function.  
Each version improves security, randomness, and timing in a different way.

---

## 🔥 Versions Overview

| Feature                       | Version 1 | Version 2 |     Version 3      |
|:-------------------------------|:---------:|:---------:|:------------------:|
| 🔒 **Security**                | ❌ Weak (MD5) | ✅ Strong (SHA-256) | ✅ Strong (SHA-256) |
| 🎲 **Randomized Salt**         | ❌ No | ✅ Yes |        ❌ No        |
| ⏰ **Time Dependency**         | 📅 Per Day | ⚡ Per Execution | 🕒 Every N Minutes |
| 🕹️ **Control over Lifespan**  | ❌ No | ❌ No |       ✅ Yes        |
| 🏎️ **Performance**            | 🚀 Fast | 🚀 Fast |      🚀 Fast       |
| 🌎 **UTC-Based**               | ❌ Local Time | ❌ Local Time |       ✅ Yes        |
| 📄 **Hash Algorithm**          | MD5 | SHA-256 |      SHA-256       |
| Year                           | 2022 | 2024 |       2025         |
---

## 🧪 Version Details

### Version 1: Simple MD5-Based Token

```python
    def Enigma(mult, div, fix)
```

* Based on current date (year, month, day, day-of-year).
* Same token generated all day.
* No randomness, easy to predict.
* Hash Function: MD5 (⚠️ considered weak)
* Use Case:
  * Simple tracking or non-critical identifiers.

### Version 2: SHA-256 Token with Random Salt
```python
    def Enigma(mult, div, fix, salt)
```
* Hash Function: SHA-256 (✅ secure)
* Based on current date but includes a random salt.
* Token is unique every time you generate it.
* Resistant to replay attacks.
* Use Case:
    * Secure session keys, one-time tokens, authentication.

### Version 3: Time-Interval Based Token
```python
    def Enigma(mult, div, fix, interval_minutes=5)
```
* Hash Function: SHA-256 (✅ secure)
* Based on current UTC time, not local time.
* Token changes every N minutes (default: 5 minutes).
* No need for a salt; still predictable in controlled systems.
* Use Case:
    * Temporary access keys, synchronized systems, time-limited sessions.

## ✨ How to Choose?

If you need...
* 🔥 Quick & simple - Version 1
* 🔒 Maximum security and randomness - Version 2
* 🕒 Time-based token without random salt - Version 3

## 🛠️ Future Ideas
1. ⏳ Allow adjustable expiration times for Version 2.

2. 🔒 Optionally encrypt the tokens for even higher security.

3. 📈 Add a verification function to validate tokens server-side.

## 📜 License
This project is free and open-source, provided as-is without any warranty.
Use at your own risk.