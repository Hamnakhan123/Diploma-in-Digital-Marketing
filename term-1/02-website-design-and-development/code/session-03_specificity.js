// Simple CSS specificity calculator: (IDs, classes/attributes/pseudo-classes, elements/pseudo-elements)
function specificity(selector) {
  let s = selector;
  const count = (re) => { const m = s.match(re) || []; s = s.replace(re, " "); return m.length; };
  const pe  = count(/::[\w-]+/g);                 // pseudo-elements
  const ids = count(/#[\w-]+/g);
  const cls = count(/\.[\w-]+|\[[^\]]+\]|:[\w-]+(\([^)]*\))?/g);
  const el  = count(/(^|[\s>+~])[a-zA-Z][\w-]*/g) + pe;
  return [ids, cls, el];
}

const selectors = ["p", ".price", "nav a", "nav a:hover", "#offer-banner", "#menu .price", "a[target=\"_blank\"]::after", "body div.container p"];
const rows = selectors.map(sel => ({ sel, spec: specificity(sel) }));
rows.sort((a, b) => b.spec[0] - a.spec[0] || b.spec[1] - a.spec[1] || b.spec[2] - a.spec[2]);

console.log("Selector".padEnd(28), "Specificity (ID, Class, Element)");
for (const r of rows) console.log(r.sel.padEnd(28), "(" + r.spec.join(", ") + ")");
console.log("\nHighest specificity (wins if these targeted the same element):", rows[0].sel);
console.log("Inline style=\"…\" beats all of these; !important beats inline (use rarely).");
