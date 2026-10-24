// 1) Box model: rendered width under content-box vs border-box
function renderedWidth({ width, padding, border }, sizing) {
  return sizing === "content-box" ? width + 2 * padding + 2 * border : width;
}
const box = { width: 256, padding: 20, border: 1 };
console.log("Card: width 256px, padding 20px, border 1px");
console.log("  content-box total width:", renderedWidth(box, "content-box"), "px");
console.log("  border-box  total width:", renderedWidth(box, "border-box"), "px",
            "(content area shrinks to", box.width - 2 * box.padding - 2 * box.border, "px)");

// 2) Colour contrast ratio (WCAG) – is the button text readable?
function luminance(hex) {
  const [r, g, b] = hex.match(/\w\w/g).map(h => parseInt(h, 16) / 255)
    .map(c => (c <= 0.03928 ? c / 12.92 : ((c + 0.055) / 1.055) ** 2.4));
  return 0.2126 * r + 0.7152 * g + 0.0722 * b;
}
function contrast(a, b) {
  const [l1, l2] = [luminance(a), luminance(b)].sort((x, y) => y - x);
  return (l1 + 0.05) / (l2 + 0.05);
}
const pairs = [["#ffffff", "#7a3e00"], ["#ffffff", "#ffb703"], ["#333333", "#ffb703"], ["#999999", "#ffffff"]];
console.log("\nText on background   Ratio   WCAG AA (4.5:1 normal text)");
for (const [fg, bg] of pairs) {
  const r = contrast(fg, bg);
  console.log(`${fg} on ${bg}`.padEnd(20), r.toFixed(2).padStart(6), "  ", r >= 4.5 ? "PASS" : "FAIL");
}
