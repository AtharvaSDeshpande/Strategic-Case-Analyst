import os
from datetime import datetime

date_str = datetime.now().strftime("%Y-%m-%d")

entries = {
    "value-chain.md": f"\n\n## {date_str}\n- **Application Learning**: Value Chain analysis isn't just about finding where costs are added; it's about finding where time can be eliminated. A structural advantage is created when a step (like storage) is entirely removed rather than just optimized.\n",
    "9-box-ge-matrix.md": f"\n\n## {date_str}\n- **Application Learning**: The GE Matrix is an excellent tool for post-mortem analysis of failed geographic expansion. Capital should be ruthlessly pulled from low-attractiveness/low-strength quadrants to fund growth.\n",
    "five-forces.md": f"\n\n## {date_str}\n- **Application Learning**: The Threat of Substitutes can be neutralized not just by building a better product, but by altering the buyer's economics. Bundling a substitute for free to an existing massive user base effectively destroys the substitute's go-to-market motion.\n",
    "corporate-scope.md": f"\n\n## {date_str}\n- **Application Learning**: Horizontal integration and corporate scope expansion often target adjacent networks rather than direct revenue generators. Owning the spaces where users work ensures they eventually deploy to your core infrastructure.\n",
    "bcg-matrix.md": f"\n\n## {date_str}\n- **Application Learning**: A 'Dog' in the BCG matrix can still be a multi-billion dollar, globally recognized brand. The matrix forces objective evaluation of growth and margin relative to the rest of the portfolio, overriding emotional attachment to famous brands.\n",
    "ansoff-matrix.md": f"\n\n## {date_str}\n- **Application Learning**: In mature markets, Product Development is heavily tied to format innovation and pricing architecture. Changing the physical format of an existing product can unlock massive price premiums without requiring new customers.\n"
}

os.makedirs('../wiki/frameworks', exist_ok=True)

for filename, content in entries.items():
    filepath = os.path.join('../wiki/frameworks', filename)
    mode = 'a' if os.path.exists(filepath) else 'w'
    with open(filepath, mode) as f:
        if mode == 'w':
            f.write(f"# {filename.replace('.md', '').replace('-', ' ').title()}\n")
        f.write(content)

# Update index.md
index_path = '../wiki/index.md'
with open(index_path, 'r') as f:
    index_content = f.read()

new_links = []
if "9-box-ge-matrix.md" not in index_content:
    new_links.append("- [9-Box GE Matrix](frameworks/9-box-ge-matrix.md)")
if "corporate-scope.md" not in index_content:
    new_links.append("- [Corporate Scope](frameworks/corporate-scope.md)")

if new_links:
    with open(index_path, 'a') as f:
        f.write("\n" + "\n".join(new_links) + "\n")

# Update capability-log.md
with open('../wiki/capability-log.md', 'a') as f:
    f.write(f"\n- **{date_str}**: Refined ability to apply strategic frameworks without naming them, focusing purely on operational reality and financial outcomes across distinct sectors.\n")

# Update reusable-heuristics.md
with open('../wiki/reusable-heuristics.md', 'a') as f:
    f.write(f"\n- **Heuristic**: When analyzing competitive defense, look for bundling strategies that alter buyer economics before looking at feature differentiation. (Confidence: High)\n")
