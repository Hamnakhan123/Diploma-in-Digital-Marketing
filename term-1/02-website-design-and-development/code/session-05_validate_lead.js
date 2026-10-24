// The same checks the HTML form performs (required, pattern, min/max), written in JavaScript.
// Servers must always re-check: browser validation can be bypassed.
const rules = {
  name:    v => v.trim().length >= 2 || "Enter your full name (2+ characters)",
  phone:   v => /^03\d{9}$/.test(v) || "Use the format 03XXXXXXXXX",
  email:   v => v === "" || /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v) || "Email looks wrong",
  event:   v => ["Office", "Mehndi", "Wedding"].includes(v) || "Choose an event type",
  guests:  v => (Number(v) >= 10 && Number(v) <= 1000) || "Guests must be 10-1000",
  consent: v => v === true || "Consent is required",
};

function validate(lead) {
  return Object.entries(rules)
    .map(([field, check]) => [field, check(lead[field])])
    .filter(([, result]) => result !== true);
}

const leads = [
  { name: "Ayesha Khan", phone: "03001234567", email: "", event: "Wedding", guests: 300, consent: true },
  { name: "B", phone: "3001234567", email: "bilal@mail", event: "", guests: 5, consent: false },
];

leads.forEach((lead, i) => {
  const errors = validate(lead);
  console.log(`Lead ${i + 1}: ${errors.length ? "REJECTED" : "ACCEPTED"}`);
  errors.forEach(([f, msg]) => console.log(`  - ${f}: ${msg}`));
});

// Simple form conversion rate for the landing page
const visits = 2400, submissions = 132;
console.log(`\nForm conversion rate: ${(submissions / visits * 100).toFixed(1)}%`);
