// Personalised greeting based on the hour - Session 1
function greeting(hour, name) {
  let part;
  if (hour < 12) part = "Good morning";
  else if (hour < 17) part = "Good afternoon";
  else part = "Good evening";
  return `${part}, ${name}! Your coffee is 10% off until 6 pm.`;
}

for (const h of [9, 14, 20]) {
  console.log(`${String(h).padStart(2, "0")}:00 ->`, greeting(h, "Sana"));
}
