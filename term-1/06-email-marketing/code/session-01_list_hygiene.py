# Clean an email list before sending: validate format, fix common typos, remove duplicates,
# role addresses and unconfirmed or unsubscribed contacts. Prepared by Hamna Zahid Khan, Junior Lecturer.
# All addresses are invented (example domains) for practice.
import re

RAW = """name,email,consent,status
Ayesha Khan,ayesha.khan@gmail.com,double_opt_in,active
Bilal Ahmed,BILAL.AHMED@GMAIL.COM ,double_opt_in,active
Bilal A.,bilal.ahmed@gmail.com,single_opt_in,active
Sara Malik,sara.malik@gmial.com,double_opt_in,active
Info Desk,info@example-traders.pk,imported,active
Usman Tariq,usman.tariq@yahoo,double_opt_in,active
Hira Shah,hira.shah@hotmail.com,double_opt_in,unsubscribed
Zain Raza,zain.raza@outlook.com,purchased_list,active
Maryam Iqbal,maryam.iqbal@gmail.com,single_opt_in,active
Fahad Ali,fahad..ali@gmail.com,double_opt_in,active
Noor Fatima,noor.fatima@yaho.com,double_opt_in,active
Sales Team,sales@example-shop.pk,double_opt_in,active"""

PATTERN = re.compile(r"^[a-z0-9](?:[a-z0-9._%+-]*[a-z0-9])?@[a-z0-9-]+(?:\.[a-z0-9-]+)*\.[a-z]{2,}$")
TYPOS = {"gmial.com": "gmail.com", "gmal.com": "gmail.com", "yaho.com": "yahoo.com", "hotmial.com": "hotmail.com", "outlok.com": "outlook.com"}
ROLE = {"info", "sales", "admin", "support", "noreply", "contact"}
OK_CONSENT = {"double_opt_in", "single_opt_in"}

rows = [r.split(",") for r in RAW.splitlines()[1:]]
seen, keep, report = set(), [], []
for name, email, consent, status in rows:
    e = email.strip().lower()
    local, _, domain = e.partition("@")
    if domain in TYPOS:
        report.append(f"FIXED   {e} -> {local}@{TYPOS[domain]} (typo)"); domain = TYPOS[domain]; e = f"{local}@{domain}"
    if ".." in e or not PATTERN.match(e):
        report.append(f"REMOVED {e} (invalid format)"); continue
    if status == "unsubscribed":
        report.append(f"REMOVED {e} (unsubscribed - must never be emailed)"); continue
    if consent not in OK_CONSENT:
        report.append(f"REMOVED {e} (no valid consent: {consent})"); continue
    if local in ROLE:
        report.append(f"FLAGGED {e} (role address - low engagement, kept for B2B review)")
    if e in seen:
        report.append(f"REMOVED {e} (duplicate)"); continue
    seen.add(e); keep.append((name, e, consent))

print("\n".join(report))
print(f"\nStart: {len(rows)} contacts -> clean list: {len(keep)} contacts ({len(keep) / len(rows):.0%})")
for n, e, c in keep:
    print(f"  {n:<14}{e:<30}{c}")
