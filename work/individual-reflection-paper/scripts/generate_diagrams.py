import matplotlib.pyplot as plt
import os

# Create diagrams dir
os.makedirs('diagrams', exist_ok=True)

# Function for capability pie chart
def create_pie(filename, title, labels, sizes, explode):
    fig, ax = plt.subplots(figsize=(6, 6))
    colors = ['#1f77b4', '#aec7e8', '#ff7f0e', '#ffbb78', '#2ca02c']
    ax.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=False, startangle=90, colors=colors[:len(labels)])
    ax.axis('equal')
    plt.title(title, pad=20)
    plt.savefig(f'diagrams/{filename}', dpi=300, bbox_inches='tight')
    plt.close()

# 1. Costco Capability Pie
create_pie('fig1_costco_capability.png', 'Costco Capabilities Distribution', 
           ['Supply Chain & Logistics (Core)', 'Membership Management', 'Store Operations', 'Merchandising'], 
           [45, 25, 15, 15], (0.1, 0, 0, 0))

# 2. Costco 5 Forces (simple bar or radar)
fig, ax = plt.subplots(figsize=(7, 5))
forces = ['Supplier Power', 'Buyer Power', 'Competitive Rivalry', 'Threat of Substitution', 'Threat of New Entry']
impact = [2, 3, 4, 3, 2] # 1 to 5 scale
ax.barh(forces, impact, color='#1f77b4')
ax.set_xlim(0, 5)
plt.title('Costco: Supply Chain Leverage vs Market Forces')
plt.savefig('diagrams/fig2_costco_5forces.png', dpi=300, bbox_inches='tight')
plt.close()

# 3. Costco Corporate Scope (Horizontal Bar)
fig, ax = plt.subplots(figsize=(7, 5))
categories = ['Branded Goods', 'Kirkland Signature (Private Label)']
shares = [75, 25]
ax.bar(categories, shares, color=['#aec7e8', '#1f77b4'])
ax.set_ylabel('Percentage of Sales')
plt.title('Costco: Vertical Integration via Private Label (2023)')
plt.savefig('diagrams/fig3_costco_scope.png', dpi=300, bbox_inches='tight')
plt.close()

# 4. Netflix Capability Pie
create_pie('fig4_netflix_capability.png', 'Netflix Capabilities Distribution', 
           ['Content Delivery & Analytics (Core)', 'Original Content Production', 'Marketing', 'Platform Eng'], 
           [40, 30, 15, 15], (0.1, 0, 0, 0))

# 5. Netflix S.E. Model (Scatter / Timeline)
fig, ax = plt.subplots(figsize=(8, 4))
years = [1998, 2007, 2013, 2024]
events = ['DVD by Mail', 'Streaming Launch', 'House of Cards (Originals)', 'Ad-supported Tier']
ax.plot(years, [1]*len(years), 'bo-')
for i, txt in enumerate(events):
    ax.annotate(txt, (years[i], 1.02), ha='center')
ax.set_ylim(0.9, 1.2)
ax.set_yticks([])
plt.title('Netflix: Environmental Adaptation Timeline')
plt.savefig('diagrams/fig5_netflix_se.png', dpi=300, bbox_inches='tight')
plt.close()

# 6. Netflix Value Chain
fig, ax = plt.subplots(figsize=(8, 3))
steps = ['Content Creation\n($17B Spend)', 'Licensing', 'Cloud Infrastructure\n(AWS)', 'Direct to Consumer\nPlatform']
ax.bar(steps, [1,1,1,1], color='#aec7e8', edgecolor='black')
plt.title('Netflix: Streamlined Value Chain')
ax.set_yticks([])
plt.savefig('diagrams/fig6_netflix_valuechain.png', dpi=300, bbox_inches='tight')
plt.close()

# 7. Nestle Capability Pie
create_pie('fig7_nestle_capability.png', 'Nestle Capabilities Distribution', 
           ['Brand Portfolio Mgt (Core)', 'R&D / Nutrition Science', 'Global Supply Chain', 'Marketing'], 
           [40, 25, 20, 15], (0.1, 0, 0, 0))

# 8. Nestle BCG Matrix (Bubble chart)
fig, ax = plt.subplots(figsize=(6, 6))
ax.scatter([0.8, 0.2, 0.7, 0.3], [0.8, 0.2, 0.3, 0.8], s=1000, alpha=0.5, c=['green', 'red', 'blue', 'orange'])
ax.text(0.8, 0.8, 'PetCare\n(Star)', ha='center', va='center')
ax.text(0.2, 0.2, 'US Candy (2018)\n(Dog-Divested)', ha='center', va='center')
ax.text(0.7, 0.3, 'Nespresso\n(Cash Cow)', ha='center', va='center')
ax.text(0.3, 0.8, 'Plant-Based\n(Question Mark)', ha='center', va='center')
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_xlabel('Relative Market Share')
ax.set_ylabel('Market Growth Rate')
plt.title('Nestle: Capital Allocation across Portfolio')
plt.savefig('diagrams/fig8_nestle_bcg.png', dpi=300, bbox_inches='tight')
plt.close()

# 9. Nestle Ansoff Matrix
fig, ax = plt.subplots(figsize=(6, 6))
ax.plot([0.5, 0.5], [0, 1], 'k--')
ax.plot([0, 1], [0.5, 0.5], 'k--')
ax.text(0.25, 0.75, 'Market Penetration\n(Aimmune Acq)', ha='center', va='center')
ax.text(0.75, 0.75, 'Product Development\n(Health Science)', ha='center', va='center')
ax.text(0.25, 0.25, 'Market Development\n(Emerging Markets)', ha='center', va='center')
ax.text(0.75, 0.25, 'Diversification\n(New Vet Clinics)', ha='center', va='center')
ax.set_xticks([0.25, 0.75])
ax.set_xticklabels(['Existing Products', 'New Products'])
ax.set_yticks([0.25, 0.75])
ax.set_yticklabels(['New Markets', 'Existing Markets'])
plt.title('Nestle: Pathways to Growth')
plt.savefig('diagrams/fig9_nestle_ansoff.png', dpi=300, bbox_inches='tight')
plt.close()

print("Diagrams generated.")
