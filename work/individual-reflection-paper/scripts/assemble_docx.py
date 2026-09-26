from docx import Document
from docx.shared import Inches, Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH

doc = Document()

# Clean typography and simple formatting
style = doc.styles['Normal']
font = style.font
font.name = 'Calibri'
font.size = Pt(11)

title = doc.add_heading('Corporate Endurance and Capability Leveraging', 0)
title.alignment = WD_ALIGN_PARAGRAPH.CENTER

# Paragraph 1
p1 = doc.add_paragraph(
    "When I examine how large organizations sustain their market position, I consistently find that their success hinges on a single, deeply ingrained capability that dictates every move they make. A company does not simply choose a strategy in a vacuum; it acts in ways that leverage its core operational strength while defending against unique environmental pressures. By looking closely at three distinct giants—Walmart in retail, Microsoft in enterprise software, and Procter & Gamble in consumer goods—I can see how capital allocation, operational flow, and competitive maneuvering are directly downstream of what each company fundamentally does best."
)
p1.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY

# Walmart
p2 = doc.add_paragraph(
    "For Walmart, the foundational capability is an absolute mastery of logistics and supply chain efficiency (Figure 1). Their advantage is not merely buying in bulk; it is the physical velocity of the goods themselves. When analyzing the path a product takes from a manufacturer to a store shelf, it becomes clear that storage is an enemy of profit. Walmart pioneered a method known as cross-docking, where inbound deliveries from suppliers are transferred almost immediately to outbound store trucks, rarely resting on a warehouse floor (Figure 2). By eliminating the need to put away, store, and retrieve inventory, Walmart successfully shaved an estimated 6% to 8% off their total supply chain costs. This structural advantage means they can systematically undercut competitors on price without sacrificing their own margins, turning a backend logistical process into a frontline consumer promise."
)
p2.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY

doc.add_picture('../diagrams/figure_1_walmart_pie.png', width=Inches(4.5))
doc.paragraphs[-1].alignment = WD_ALIGN_PARAGRAPH.CENTER
caption1 = doc.add_paragraph("Figure 1: Walmart Organizational Capabilities Distribution")
caption1.alignment = WD_ALIGN_PARAGRAPH.CENTER
caption1.style.font.size = Pt(10)
caption1.style.font.italic = True

doc.add_picture('../diagrams/figure_2_walmart_value_chain.png', width=Inches(4.5))
doc.paragraphs[-1].alignment = WD_ALIGN_PARAGRAPH.CENTER
caption2 = doc.add_paragraph("Figure 2: Upstream velocity and zero-storage operations")
caption2.alignment = WD_ALIGN_PARAGRAPH.CENTER
caption2.style.font.size = Pt(10)
caption2.style.font.italic = True

p3 = doc.add_paragraph(
    "However, operational brilliance does not guarantee universal success, which forces difficult decisions about where to deploy capital. Walmart’s aggressive expansion highlighted the limits of applying a rigid model to wildly different geographic realities (Figure 3). In a market like Mexico, their operational formula translated well and fueled massive growth, justifying heavy reinvestment. But in Germany, a mature market characterized by entrenched discount competitors and strict labor regulations, the model failed to adapt. Recognizing that investing further would only erode value, Walmart retreated in 2006, absorbing a staggering $1 billion pretax loss. This calculated withdrawal reveals a crucial discipline: an organization must objectively assess the attractiveness of a market against its own ability to win there, ruthlessly cutting losses in stagnant environments to fund growth where its capabilities actually matter."
)
p3.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY

doc.add_picture('../diagrams/figure_3_walmart_ge.png', width=Inches(4.5))
doc.paragraphs[-1].alignment = WD_ALIGN_PARAGRAPH.CENTER
caption3 = doc.add_paragraph("Figure 3: Geographic Resource Allocation and Market Exit")
caption3.alignment = WD_ALIGN_PARAGRAPH.CENTER
caption3.style.font.size = Pt(10)
caption3.style.font.italic = True

doc.add_page_break()

# Microsoft
p4 = doc.add_paragraph(
    "Transitioning from the physical movement of goods to the digital realm, Microsoft’s core capability is ecosystem integration and enterprise software lock-in (Figure 4). Their power lies in ensuring that once a business adopts their infrastructure, the switching costs become impossibly high. This dynamic became vividly apparent in how they handled the existential threat posed by Slack, an agile newcomer that sought to redefine enterprise communication. Rather than engaging in a feature-by-feature war, Microsoft leveraged its massive, entrenched footprint. On March 14, 2017, they launched Teams and bundled it as a free inclusion within their existing Office 365 subscriptions (Figure 5). By distributing a substitute product for free to millions of captive users, they effectively suffocated the newcomer’s growth potential. It was a masterclass in defensive maneuvering: neutralizing a competitive threat by altering the basic economics of the category for the buyer."
)
p4.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY

doc.add_picture('../diagrams/figure_4_microsoft_pie.png', width=Inches(4.5))
doc.paragraphs[-1].alignment = WD_ALIGN_PARAGRAPH.CENTER
caption4 = doc.add_paragraph("Figure 4: Microsoft Organizational Capabilities Distribution")
caption4.alignment = WD_ALIGN_PARAGRAPH.CENTER
caption4.style.font.size = Pt(10)
caption4.style.font.italic = True

doc.add_picture('../diagrams/figure_5_microsoft_forces.png', width=Inches(4.5))
doc.paragraphs[-1].alignment = WD_ALIGN_PARAGRAPH.CENTER
caption5 = doc.add_paragraph("Figure 5: Neutralizing substitutes through infrastructure bundling")
caption5.alignment = WD_ALIGN_PARAGRAPH.CENTER
caption5.style.font.size = Pt(10)
caption5.style.font.italic = True

p5 = doc.add_paragraph(
    "Microsoft does not just defend its borders; it aggressively expands them by acquiring adjacent networks that deepen its gravitational pull (Figure 6). The $7.5 billion acquisition of GitHub on June 4, 2018, is a perfect illustration. Microsoft did not buy a code repository for its direct subscription revenue. They bought the digital space where developers live and work. By integrating GitHub into Azure and their broader suite of developer tools, they created a seamless pipeline from writing code to deploying it on Microsoft servers. Expanding into these adjacent spaces ensures that the entire lifecycle of a professional’s work remains tethered to the Microsoft platform, fortifying their structural dominance."
)
p5.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY

doc.add_picture('../diagrams/figure_6_microsoft_scope.png', width=Inches(4.5))
doc.paragraphs[-1].alignment = WD_ALIGN_PARAGRAPH.CENTER
caption6 = doc.add_paragraph("Figure 6: Adjacent network acquisitions driving ecosystem gravity")
caption6.alignment = WD_ALIGN_PARAGRAPH.CENTER
caption6.style.font.size = Pt(10)
caption6.style.font.italic = True

doc.add_page_break()

# P&G
p6 = doc.add_paragraph(
    "Finally, in the fast-moving consumer goods sector, Procter & Gamble operates through a core capability of brand management and consumer innovation (Figure 7). Managing dozens of distinct product lines requires a ruthless approach to balancing cash generation with long-term growth (Figure 8). I find their 2014 decision to divest Duracell to Berkshire Hathaway for $4.7 billion particularly illuminating. To an outsider, selling a globally recognized brand seems counterproductive. Yet, within P&G's internal portfolio, batteries were a slow-growing segment that tied up capital and management attention. By shedding this division, P&G reallocated billions of dollars toward high-margin, faster-growing household names like Tide and Gillette. It demonstrates that a healthy corporate portfolio requires pruning; holding onto a famous but stagnant product is a strategic error when those resources could fuel genuine growth engines."
)
p6.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY

doc.add_picture('../diagrams/figure_7_pg_pie.png', width=Inches(4.5))
doc.paragraphs[-1].alignment = WD_ALIGN_PARAGRAPH.CENTER
caption7 = doc.add_paragraph("Figure 7: P&G Organizational Capabilities Distribution")
caption7.alignment = WD_ALIGN_PARAGRAPH.CENTER
caption7.style.font.size = Pt(10)
caption7.style.font.italic = True

doc.add_picture('../diagrams/figure_8_pg_bcg.png', width=Inches(4.5))
doc.paragraphs[-1].alignment = WD_ALIGN_PARAGRAPH.CENTER
caption8 = doc.add_paragraph("Figure 8: Portfolio pruning and reallocation of capital")
caption8.alignment = WD_ALIGN_PARAGRAPH.CENTER
caption8.style.font.size = Pt(10)
caption8.style.font.italic = True

p7 = doc.add_paragraph(
    "When P&G does lean into its core products, it pursues growth not necessarily by finding new customers, but by redefining the product format itself (Figure 9). In a saturated laundry detergent market, selling more liquid soap is a difficult proposition. Instead, P&G introduced Tide Pods in 2012. This innovation solved a minor consumer inconvenience—measuring liquid—and allowed P&G to command an estimated 25% price premium per load. They essentially convinced existing buyers to pay significantly more for the exact same underlying cleaning capability, purely through a format change. It is a striking example of how product development can extract fresh margin out of a mature market, proving that innovation is as much about pricing architecture as it is about chemistry."
)
p7.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY

doc.add_picture('../diagrams/figure_9_pg_ansoff.png', width=Inches(4.5))
doc.paragraphs[-1].alignment = WD_ALIGN_PARAGRAPH.CENTER
caption9 = doc.add_paragraph("Figure 9: Extracting margin via format innovation in mature markets")
caption9.alignment = WD_ALIGN_PARAGRAPH.CENTER
caption9.style.font.size = Pt(10)
caption9.style.font.italic = True

# Conclusion
p8 = doc.add_paragraph(
    "Through these three lenses, the reality of corporate endurance becomes clear. Whether it is Walmart aggressively managing the flow of physical capital, Microsoft manipulating the competitive landscape through bundling and strategic acquisitions, or P&G ruthlessly optimizing a portfolio of consumer brands, success is never accidental. It is the result of deeply understanding a core organizational strength and systematically projecting that strength into the market, adapting to threats and opportunities with calculated precision."
)
p8.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY

doc.save('../Reflection_Paper.docx')
