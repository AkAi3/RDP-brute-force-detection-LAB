import xml.etree.ElementTree as ET
from collections import defaultdict

tree = ET.parse("security_logs.xml")
root = tree.getroot()

ip_attempts = defaultdict(int)

for event in root.iter():
    if "EventID" in event.tag and event.text == "4625":
        ip = None

        for data in event.iter():
            if "Data" in data.tag and data.attrib.get("Name") == "IpAddress":
                ip = data.text

        if ip and ip != "-":
            ip_attempts[ip] += 1

print("\n=== Suspicious Activity ===")
for ip, count in ip_attempts.items():
    if count > 5:
        print(f"[ALERT] {ip} → {count} failed attempts")
