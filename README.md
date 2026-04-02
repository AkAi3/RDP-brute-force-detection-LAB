# RDP-brute-force-detection-LAB
This project simulates a real-world authentication attack on a Windows system and demonstrates how such activity can be detected using system logs and basic automation.
# 🛡️ RDP Brute Force Detection Lab

---

## 🎯 Objectives

* Perform network reconnaissance to identify exposed services
* Simulate authentication-based attacks (RDP/SMB)
* Analyze Windows Security logs (Event ID 4625)
* Detect brute-force behavior using a Python script

---

## 🧱 Lab Architecture

```
Kali Linux (Attacker) → Windows VM (Target) → Event Logs → Python Detection
```

---

## ⚙️ Tools & Technologies

* **Kali Linux** – Attack simulation
* **Windows VM** – Target system & log generation
* **Nmap** – Network scanning & reconnaissance
* **xfreerdp / smbclient** – Authentication attempts
* **Windows Event Viewer** – Log analysis
* **Python** – Detection automation

---

## 🔍 Reconnaissance

* Scanned the network using Nmap
* Identified active hosts in subnet (192.168.56.0/24)
* Detected open RDP port (3389) on target system

---

## ⚔️ Attack Simulation

* Performed multiple failed login attempts from Kali Linux
* Used different usernames and passwords to simulate:

  * Brute-force attacks
  * Username enumeration
* Generated authentication failure logs on Windows

---

## 📊 Log Analysis

Analyzed Windows Security Logs focusing on:

* **Event ID:** 4625 (Failed login)
* **Key Fields:**

  * Source Network Address (Attacker IP)
  * Account Name
  * Logon Type (10 = RDP, 3 = Network login)

Observed repeated login failures from a single IP, indicating suspicious behavior.

---

## 🤖 Detection Automation

Developed a Python script to:

* Parse exported XML logs
* Count failed login attempts per IP
* Identify suspicious patterns

### 🔎 Detection Logic

* > 5 failed logins from same IP → Possible brute-force attack
* Multiple usernames → Username enumeration
* Logon Type 10 → RDP-based attack

---

## 🚨 Results

* Successfully simulated attack scenarios
* Identified attacker IP (Kali machine) from logs
* Detected abnormal login patterns using automation
* Demonstrated end-to-end SOC workflow

---

## 📸 Screenshots

Include in `/screenshots`:

* Nmap scan results
* Attack attempts (Kali terminal)
* Event Viewer logs (4625 events)
* Detailed log entry (showing IP + logon type)
* Python script output

---

## 🧠 Skills Demonstrated

* Network reconnaissance
* Log analysis & correlation
* Threat detection
* Python scripting
* SOC workflow understanding

---

## 🔥 Conclusion

This project showcases a practical approach to detecting authentication attacks using system logs and automation. It reflects real-world SOC operations by combining attack simulation, log analysis, and detection logic into a complete workflow.
