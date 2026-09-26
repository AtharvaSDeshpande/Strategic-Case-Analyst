import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# Create directories
base_dir = r"c:\Users\athar\Desktop\Antigravity Playground\Strategic-Case-Analyst\work\reflectionPaper2"
os.makedirs(os.path.join(base_dir, "scripts"), exist_ok=True)
os.makedirs(os.path.join(base_dir, "diagrams"), exist_ok=True)
out_dir = os.path.join(base_dir, "diagrams")

def save_fig(name):
    plt.savefig(os.path.join(out_dir, name), dpi=300, bbox_inches='tight')
    plt.close()

# 1. IKEA Capability Pie Chart
plt.figure(figsize=(8,6))
labels = ['Cost Engineering (Core)', 'Store Experience', 'Supply Chain', 'Brand Marketing']
sizes = [45, 20, 25, 10]
colors = ['#1f77b4', '#aec7e8', '#ff7f0e', '#ffbb78']
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140, 
        explode=(0.1, 0, 0, 0))
plt.title("Figure 1: IKEA Organizational Capability Distribution")
save_fig("figure_1_ikea_capability.png")

# 2. IKEA Value Chain
fig, ax = plt.subplots(figsize=(10,6))
ax.axis('off')
ax.add_patch(patches.Rectangle((0.1, 0.6), 0.8, 0.2, facecolor='#aec7e8', edgecolor='black'))
plt.text(0.5, 0.7, 'Support Activities (Procurement, Tech Development, HR)', ha='center', va='center', fontsize=12)
ax.add_patch(patches.Rectangle((0.1, 0.3), 0.25, 0.25, facecolor='#1f77b4', edgecolor='black'))
plt.text(0.225, 0.425, 'Inbound\nLogistics\n(Flat-pack)', ha='center', va='center', color='white')
ax.add_patch(patches.Rectangle((0.375, 0.3), 0.25, 0.25, facecolor='#ff7f0e', edgecolor='black'))
plt.text(0.5, 0.425, 'Operations\n(Cost-driven\nDesign)', ha='center', va='center', color='white')
ax.add_patch(patches.Rectangle((0.65, 0.3), 0.25, 0.25, facecolor='#2ca02c', edgecolor='black'))
plt.text(0.775, 0.425, 'Outbound\n(Customer\nAssembly)', ha='center', va='center', color='white')
plt.title("Figure 2: IKEA Operating Model Reconfiguration")
save_fig("figure_2_ikea_value_chain.png")

# 3. IKEA Corporate Scope
plt.figure(figsize=(8,6))
plt.plot([1, 2, 3], [1, 2, 3], marker='o', markersize=20, color='#1f77b4')
plt.text(1, 0.8, 'Raw Materials\n(Forests)', ha='center')
plt.text(2, 1.8, 'Manufacturing', ha='center')
plt.text(3, 2.8, 'Retail\n(Stores)', ha='center')
plt.xlim(0, 4)
plt.ylim(0, 4)
plt.axis('off')
plt.title("Figure 3: Vertical Integration for Cost Control")
save_fig("figure_3_ikea_scope.png")

# 4. NVIDIA Capability Pie Chart
plt.figure(figsize=(8,6))
labels = ['Software Ecosystem (Core)', 'Silicon Design', 'Supply Chain', 'Gaming Brand']
sizes = [50, 25, 15, 10]
colors = ['#2ca02c', '#98df8a', '#d62728', '#ff9896']
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140, 
        explode=(0.1, 0, 0, 0))
plt.title("Figure 4: NVIDIA Organizational Capability Distribution")
save_fig("figure_4_nvidia_capability.png")

# 5. NVIDIA 5 Forces
fig, ax = plt.subplots(figsize=(8,8))
ax.axis('off')
ax.add_patch(patches.Rectangle((0.35, 0.4), 0.3, 0.2, facecolor='#2ca02c', edgecolor='black'))
plt.text(0.5, 0.5, 'High Rivalry\n(Custom Silicon)', ha='center', va='center', color='white')
ax.add_patch(patches.Rectangle((0.35, 0.7), 0.3, 0.15, facecolor='#98df8a', edgecolor='black'))
plt.text(0.5, 0.775, 'New Entrants\n(High Barrier via Ecosystem)', ha='center', va='center')
ax.add_patch(patches.Rectangle((0.35, 0.15), 0.3, 0.15, facecolor='#98df8a', edgecolor='black'))
plt.text(0.5, 0.225, 'Substitutes\n(Low Threat)', ha='center', va='center')
ax.add_patch(patches.Rectangle((0.05, 0.425), 0.25, 0.15, facecolor='#ff9896', edgecolor='black'))
plt.text(0.175, 0.5, 'Suppliers\n(Foundry Power)', ha='center', va='center')
ax.add_patch(patches.Rectangle((0.7, 0.425), 0.25, 0.15, facecolor='#98df8a', edgecolor='black'))
plt.text(0.825, 0.5, 'Buyers\n(Locked-in)', ha='center', va='center')
plt.title("Figure 5: The Software Ecosystem Moat")
save_fig("figure_5_nvidia_5forces.png")

# 6. NVIDIA Aghion-Howitt (Schumpeterian Creative Destruction)
plt.figure(figsize=(8,6))
x = np.linspace(0, 10, 100)
y1 = np.exp(-(x-2)**2)
y2 = np.exp(-(x-5)**2)
y3 = np.exp(-(x-8)**2)
plt.plot(x, y1, label='Generation 1')
plt.plot(x, y2, label='Generation 2 (Cannibalizes Gen 1)')
plt.plot(x, y3, label='Generation 3 (Cannibalizes Gen 2)')
plt.fill_between(x, y1, alpha=0.3)
plt.fill_between(x, y2, alpha=0.3)
plt.fill_between(x, y3, alpha=0.3)
plt.yticks([])
plt.xlabel('Time')
plt.ylabel('Market Value / Adoption')
plt.title("Figure 6: Planned Obsolescence via Rapid Innovation")
plt.legend()
save_fig("figure_6_nvidia_creative_destruction.png")

# 7. Unilever Capability Pie Chart
plt.figure(figsize=(8,6))
labels = ['Portfolio Management (Core)', 'Global Distribution', 'R&D', 'Sustainability Initiatives']
sizes = [40, 30, 15, 15]
colors = ['#d62728', '#ff9896', '#9467bd', '#c5b0d5']
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140, 
        explode=(0.1, 0, 0, 0))
plt.title("Figure 7: Unilever Organizational Capability Distribution")
save_fig("figure_7_unilever_capability.png")

# 8. Unilever BCG Matrix
fig, ax = plt.subplots(figsize=(8,8))
ax.plot([0.5, 0.5], [0, 1], 'k--')
ax.plot([0, 1], [0.5, 0.5], 'k--')
ax.add_patch(patches.Rectangle((0, 0.5), 0.5, 0.5, facecolor='#aec7e8', alpha=0.3))
plt.text(0.25, 0.95, 'High Share, High Growth', ha='center', fontsize=12, fontweight='bold')
ax.add_patch(patches.Rectangle((0.5, 0.5), 0.5, 0.5, facecolor='#ffbb78', alpha=0.3))
plt.text(0.75, 0.95, 'Low Share, High Growth', ha='center', fontsize=12, fontweight='bold')
ax.add_patch(patches.Rectangle((0, 0), 0.5, 0.5, facecolor='#98df8a', alpha=0.3))
plt.text(0.25, 0.45, 'High Share, Low Growth', ha='center', fontsize=12, fontweight='bold')
ax.add_patch(patches.Rectangle((0.5, 0), 0.5, 0.5, facecolor='#ff9896', alpha=0.3))
plt.text(0.75, 0.45, 'Low Share, Low Growth\n(Pruned 1,200 brands)', ha='center', fontsize=12, fontweight='bold')
plt.scatter([0.2, 0.3], [0.2, 0.3], s=[1000, 800], color='green', label='Core 400 Brands')
plt.scatter([0.7, 0.8, 0.6], [0.2, 0.3, 0.1], s=[100, 50, 150], color='red', label='Divested Brands')
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.xticks([])
plt.yticks([])
plt.xlabel('Relative Market Share', fontsize=12)
plt.ylabel('Market Growth Rate', fontsize=12)
plt.title("Figure 8: Brand Portfolio Pruning")
plt.legend(loc='lower right')
save_fig("figure_8_unilever_bcg.png")

# 9. Unilever Ansoff Matrix
fig, ax = plt.subplots(figsize=(8,8))
ax.plot([0.5, 0.5], [0, 1], 'k-')
ax.plot([0, 1], [0.5, 0.5], 'k-')
plt.text(0.25, 0.75, 'Emerging Markets', ha='center', va='center', fontsize=12)
plt.text(0.75, 0.75, 'Sustainable Variants', ha='center', va='center', fontsize=12)
plt.text(0.25, 0.25, 'New Demographics', ha='center', va='center', fontsize=12)
plt.text(0.75, 0.25, 'Prestige Beauty Acquisitions', ha='center', va='center', fontsize=12, color='blue', fontweight='bold')
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.xticks([0.25, 0.75], ['Existing Products', 'New Products'], fontsize=12)
plt.yticks([0.25, 0.75], ['New Markets', 'Existing Markets'], fontsize=12, rotation=90)
plt.title("Figure 9: Growth via Premium Categories")
save_fig("figure_9_unilever_ansoff.png")
