import os
import datetime

date_str = datetime.date.today().isoformat()
wiki_dir = r"c:\Users\athar\Desktop\Antigravity Playground\Strategic-Case-Analyst\wiki"
frameworks_dir = os.path.join(wiki_dir, "frameworks")

def append_to_file(filepath, content):
    with open(filepath, 'a', encoding='utf-8') as f:
        f.write(f"\n\n{content}")

# Value chain
append_to_file(os.path.join(frameworks_dir, "value-chain.md"), f"## {date_str} - Retail Reconfiguration\n- Taught that cost engineering isn't just a support activity, but a constraint that dictates the entire inbound and outbound logistics configuration (e.g., forcing customer co-production).")

# Corporate Scope
append_to_file(os.path.join(frameworks_dir, "corporate-scope.md"), f"## {date_str} - Vertical Integration for Cost\n- Taught that extending corporate scope backwards into raw materials can be a defensive move to protect a low-price guarantee against supplier shocks.")

# Five Forces
append_to_file(os.path.join(frameworks_dir, "five-forces.md"), f"## {date_str} - Software Lock-in as a Moat\n- Taught that buyer power can be neutralized not just by lack of alternatives, but by the prohibitive switching costs of retraining developers and rewriting legacy code on a proprietary platform.")

# Aghion-Howitt (Schumpeterian Creative Destruction)
aghion_path = os.path.join(frameworks_dir, "aghion-howitt.md")
with open(aghion_path, 'w', encoding='utf-8') as f:
    f.write(f"# Aghion-Howitt (Schumpeterian Creative Destruction)\n\n## {date_str} - Planned Obsolescence\n- Taught that the most durable tech monopolies actively destroy their own cash cows with new generations to prevent competitors from finding an entry point.")

# BCG Matrix
append_to_file(os.path.join(frameworks_dir, "bcg-matrix.md"), f"## {date_str} - Pruning at Scale\n- Taught that scale is a liability if unmanaged, and the matrix is as much about identifying which 'dogs' to cut (to free up capital) as it is about feeding the 'stars'.")

# Ansoff Matrix
append_to_file(os.path.join(frameworks_dir, "ansoff-matrix.md"), f"## {date_str} - Margin Expansion\n- Taught that diversification isn't just about growth, but about migrating the portfolio into higher-margin categories to escape commodity pricing pressures.")

# Capability log
append_to_file(os.path.join(wiki_dir, "capability-log.md"), f"\n- **{date_str}**: Sharpened the ability to weave multiple distinct frameworks into a cohesive, concept-silent narrative without losing the analytical rigor of the models.")
