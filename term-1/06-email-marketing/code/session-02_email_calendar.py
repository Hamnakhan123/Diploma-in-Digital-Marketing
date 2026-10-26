# Build a 3-month email calendar around Pakistani retail moments, mixing campaign types
# and respecting a weekly frequency cap. Prepared by Hamna Zahid Khan, Junior Lecturer.
import datetime as dt, csv

START, WEEKS, CAP = dt.date(2026, 10, 5), 13, 2      # Mondays from 5 Oct 2026; max 2 emails/week
EVENTS = {  # date: (campaign type, subject idea)  - verify dates each year
    dt.date(2026, 11, 6): ("Promotional", "11.11 early access starts now"),
    dt.date(2026, 11, 11): ("Promotional", "11.11: up to 40% off - today only"),
    dt.date(2026, 11, 27): ("Promotional", "White Friday deals inside"),
    dt.date(2026, 12, 11): ("Seasonal", "Wedding season gift guide"),
    dt.date(2026, 12, 24): ("Seasonal", "Year-end sale + Quaid Day reads"),
}
ROTATION = [("Newsletter", "This week's new arrivals + staff pick"), ("Educational", "How to choose your next book in 3 questions"),
            ("Newsletter", "Reader of the month"), ("Re-engagement", "Still interested? Pick your topics")]
rows, i = [], 0
for w in range(WEEKS):
    monday = START + dt.timedelta(weeks=w)
    week_days = [monday + dt.timedelta(days=d) for d in range(7)]
    planned = [(d, *EVENTS[d]) for d in week_days if d in EVENTS]
    friday = monday + dt.timedelta(days=4)
    slot = friday if friday not in EVENTS else monday + dt.timedelta(days=1)   # never two emails on one day
    if len(planned) < CAP:
        t, s = ROTATION[i % len(ROTATION)]; i += 1
        planned.append((slot, t, s))
    for d, t, s in sorted(planned)[:CAP]:
        rows.append([d.isoformat(), d.strftime("%a"), "11:00 PKT", t, s])
with open("session-02_email_calendar.csv", "w", newline="") as f:
    wr = csv.writer(f); wr.writerow(["date", "day", "send_time", "type", "subject_idea"]); wr.writerows(rows)
for r in rows:
    print(" | ".join(r))
types = {}
for r in rows: types[r[3]] = types.get(r[3], 0) + 1
print(f"\n{len(rows)} emails in {WEEKS} weeks (avg {len(rows) / WEEKS:.1f}/week):", types)
