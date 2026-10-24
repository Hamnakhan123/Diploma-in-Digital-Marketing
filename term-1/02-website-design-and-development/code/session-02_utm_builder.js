// Build tracked campaign links (UTM parameters) for a landing page
function buildUtm(base, { source, medium, campaign, content }) {
  const url = new URL(base);
  url.searchParams.set("utm_source", source);
  url.searchParams.set("utm_medium", medium);
  url.searchParams.set("utm_campaign", campaign);
  if (content) url.searchParams.set("utm_content", content);
  return url.toString();
}

const page = "https://chaibox.pk/offers";
const placements = [
  { source: "instagram", medium: "social", campaign: "friday_bogo", content: "story" },
  { source: "facebook", medium: "cpc", campaign: "friday_bogo", content: "carousel" },
  { source: "newsletter", medium: "email", campaign: "friday_bogo" },
];

for (const p of placements) {
  console.log(`${p.source.padEnd(10)} → ${buildUtm(page, p)}`);
}

// Anchor links point to a section on the same or another page
const anchor = new URL("https://chaibox.pk/menu#kashmiri");
console.log("\nPage:", anchor.pathname, "| Section (fragment):", anchor.hash);
