from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether
from reportlab.pdfgen import canvas

OUT = "output/pdf/respostas_alocacao_memoria_buddy.pdf"
FONT = "/System/Library/Fonts/Supplemental/Arial.ttf"
FONT_B = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
pdfmetrics.registerFont(TTFont("Arial", FONT))
pdfmetrics.registerFont(TTFont("Arial-Bold", FONT_B))

navy = colors.HexColor("#17324D")
blue = colors.HexColor("#2F6B9A")
light = colors.HexColor("#EAF2F8")
green = colors.HexColor("#DDF2E5")
orange = colors.HexColor("#FCE8D5")
gray = colors.HexColor("#F4F6F7")

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name="TitleA", parent=styles["Title"], fontName="Arial-Bold", fontSize=22, leading=27, textColor=navy, alignment=TA_CENTER, spaceAfter=10))
styles.add(ParagraphStyle(name="Sub", parent=styles["Normal"], fontName="Arial", fontSize=11, leading=15, textColor=colors.HexColor("#425466"), alignment=TA_CENTER))
styles.add(ParagraphStyle(name="H1A", parent=styles["Heading1"], fontName="Arial-Bold", fontSize=16, leading=20, textColor=navy, spaceBefore=6, spaceAfter=8))
styles.add(ParagraphStyle(name="H2A", parent=styles["Heading2"], fontName="Arial-Bold", fontSize=12.5, leading=16, textColor=blue, spaceBefore=7, spaceAfter=5))
styles.add(ParagraphStyle(name="BodyA", parent=styles["BodyText"], fontName="Arial", fontSize=9.5, leading=13.2, textColor=colors.HexColor("#222222"), spaceAfter=5))
styles.add(ParagraphStyle(name="SmallA", parent=styles["BodyText"], fontName="Arial", fontSize=8.2, leading=10.5, textColor=colors.HexColor("#333333")))
styles.add(ParagraphStyle(name="HeaderCell", parent=styles["BodyText"], fontName="Arial-Bold", fontSize=8.2, leading=10.5, textColor=colors.white))
styles.add(ParagraphStyle(name="NoteA", parent=styles["BodyText"], fontName="Arial", fontSize=9, leading=12, textColor=colors.HexColor("#34495E"), backColor=light, borderPadding=7, borderColor=blue, borderWidth=.5, borderRadius=3, spaceBefore=4, spaceAfter=7))

def P(text, style="BodyA"):
    return Paragraph(text, styles[style])

def footer(c, doc):
    c.saveState()
    c.setStrokeColor(colors.HexColor("#D5DDE5"))
    c.line(1.6*cm, 1.25*cm, 19.4*cm, 1.25*cm)
    c.setFont("Arial", 8)
    c.setFillColor(colors.HexColor("#6B7785"))
    c.drawString(1.6*cm, .82*cm, "Alocação de memória - respostas")
    c.drawRightString(19.4*cm, .82*cm, f"Página {doc.page}")
    c.restoreState()

def table(data, widths, header=True, font=8.5, row_bg=None):
    t = Table(data, colWidths=widths, repeatRows=1 if header else 0, hAlign="LEFT")
    cmds = [
        ("FONTNAME", (0,0), (-1,-1), "Arial"),
        ("FONTSIZE", (0,0), (-1,-1), font),
        ("LEADING", (0,0), (-1,-1), font+2),
        ("GRID", (0,0), (-1,-1), .35, colors.HexColor("#C6D0D9")),
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
        ("LEFTPADDING", (0,0), (-1,-1), 6), ("RIGHTPADDING", (0,0), (-1,-1), 6),
        ("TOPPADDING", (0,0), (-1,-1), 5), ("BOTTOMPADDING", (0,0), (-1,-1), 5),
    ]
    if header:
        cmds += [("BACKGROUND", (0,0), (-1,0), navy), ("TEXTCOLOR", (0,0), (-1,0), colors.white), ("FONTNAME", (0,0), (-1,0), "Arial-Bold")]
    if row_bg:
        for r, col in row_bg.items(): cmds.append(("BACKGROUND", (0,r), (-1,r), col))
    t.setStyle(TableStyle(cmds))
    return t

def buddy_row(label, blocks, compact=False):
    cells = [P(f"<b>{label}</b>", "SmallA")]
    for name, size, color in blocks:
        cells.append(P(f"<b>{name}</b><br/>{size} KB", "SmallA"))
    widths = [2.7*cm] + [max(1.8*cm, (16.4*cm)/max(1,len(blocks)))]*len(blocks)
    t = Table([cells], colWidths=widths, rowHeights=1.1*cm, hAlign="LEFT")
    cmds = [("GRID",(0,0),(-1,-1),.5,colors.HexColor("#AEBBC7")), ("VALIGN",(0,0),(-1,-1),"MIDDLE"), ("ALIGN",(1,0),(-1,-1),"CENTER"), ("LEFTPADDING",(0,0),(-1,-1),3), ("RIGHTPADDING",(0,0),(-1,-1),3)]
    for i, (_,_,col) in enumerate(blocks, start=1): cmds.append(("BACKGROUND",(i,0),(i,0),col))
    cmds.append(("BACKGROUND",(0,0),(0,0),gray))
    t.setStyle(TableStyle(cmds))
    return t

story = []
story += [Spacer(1, 1.7*cm), P("Resolução comentada - Alocação de Memória", "TitleA"), P("Entendendo First Fit, Best Fit, Worst Fit, fragmentação e o Alocador Buddy", "Sub"), Spacer(1, .9*cm)]
story += [P("A ideia aqui é acompanhar o raciocínio, e não apenas marcar as alternativas. No Buddy, vamos considerar blocos em potências de 2 e escolher sempre o menor bloco disponível que consiga atender ao pedido.", "NoteA")]
story += [P("1. Estratégias de Alocação", "H1A"), P("Temos os blocos livres <b>200 KB | 500 KB | 100 KB | 350 KB | 600 KB</b> e um processo pedindo <b>250 KB</b>.", "BodyA")]
story += [table([[P("Estratégia", "HeaderCell"), P("Regra", "HeaderCell"), P("Bloco escolhido", "HeaderCell"), P("Alternativa", "HeaderCell")], [P("First Fit"), P("Primeiro bloco, da esquerda para a direita, que comporta 250 KB."), P("<b>500 KB</b>"), P("Resposta B")], [P("Best Fit"), P("Menor bloco que comporta 250 KB."), P("<b>350 KB</b>"), P("Resposta C")], [P("Worst Fit"), P("Maior bloco disponível que comporta 250 KB."), P("<b>600 KB</b>"), P("Resposta D")]], [3.0*cm, 8.0*cm, 3.0*cm, 2.8*cm], row_bg={1: colors.white,2:gray,3:colors.white})]
story += [Spacer(1, .35*cm), P("2. Fragmentação", "H1A"), P("Questão 1: como 130 KB não é uma potência de 2, o Buddy sobe para o próximo tamanho possível: 256 KB. Sobram 256 - 130 = <b>126 KB</b> dentro do bloco.", "BodyA"), P("Resposta: <b>(B) 256 KB alocados, com 126 KB de fragmentação interna.</b>", "NoteA"), P("Questão 2: esse desperdício dentro do bloco reservado é justamente a fragmentação interna. Ela aparece bastante no Buddy porque os pedidos são arredondados para potências de 2.", "BodyA"), P("Resposta: <b>(B) Fragmentação interna.</b>", "NoteA")]
story += [PageBreak(), P("3. Alocador Buddy - memória de 2 MB", "H1A"), P("Começamos com 2048 KB livres. Como o Buddy trabalha com potências de 2, os pedidos acabam ocupando: P1 = 256 KB, P2 = 512 KB, P3 = 128 KB, P4 = 512 KB, P5 = 256 KB, P6 = 128 KB e P7 = 512 KB.", "BodyA"), P("Na leitura abaixo, verde representa um processo e cinza representa espaço livre. Os intervalos indicam os endereços em KB.", "NoteA")]

steps = [
    ("Etapa 0 - início", [("Livre",2048,gray)], "-", "0 KB"),
    ("1 - aloca P1 (200 KB)", [("P1",256,green),("Livre",256,gray),("Livre",512,gray),("Livre",1024,gray)], "2048 -> 1024 + 1024; 1024 -> 512 + 512; 512 -> 256 + 256", "56 KB"),
    ("2 - aloca P2 (400 KB)", [("P1",256,green),("Livre",256,gray),("P2",512,green),("Livre",1024,gray)], "512 livre -> P2 = 512", "168 KB"),
    ("3 - aloca P3 (100 KB)", [("P1",256,green),("P3",128,green),("Livre",128,gray),("P2",512,green),("Livre",1024,gray)], "256 livre -> 128 + 128; P3 = 128", "196 KB"),
    ("4 - aloca P4 (300 KB)", [("P1",256,green),("P3",128,green),("Livre",128,gray),("P2",512,green),("P4",512,green),("Livre",512,gray)], "1024 livre -> 512 + 512; P4 = 512", "302 KB"),
    ("5 - aloca P5 (150 KB)", [("P1",256,green),("P3",128,green),("Livre",128,gray),("P2",512,green),("P4",512,green),("P5",256,green),("Livre",256,gray)], "512 livre -> 256 + 256; P5 = 256", "358 KB"),
]
for title, blocks, split, frag in steps:
    story += [P(title, "H2A"), buddy_row("Blocos", blocks), P(f"<b>Split:</b> {split} &nbsp;&nbsp; <b>Fragmentação interna acumulada:</b> {frag}", "SmallA"), Spacer(1,.12*cm)]

story += [PageBreak(), P("Continuação das operações", "H1A")]
steps2 = [
    ("6 - libera P1", [("Livre",256,gray),("P3",128,green),("Livre",128,gray),("P2",512,green),("P4",512,green),("P5",256,green),("Livre",256,gray)], "Não ocorre merge: o buddy de P1 contém P3 e um livre de 128 KB.", "302 KB (P1 ainda não conta; espaço liberado)"),
    ("7 - libera P3", [("Livre",512,gray),("P2",512,green),("P4",512,green),("P5",256,green),("Livre",256,gray)], "Merge 128 + 128 -> 256; depois 256 + 256 -> 512.", "246 KB"),
    ("8 - aloca P6 (120 KB)", [("P6",128,green),("Livre",128,gray),("Livre",256,gray),("P2",512,green),("P4",512,green),("P5",256,green),("Livre",256,gray)], "512 livre -> 256 + 256; 256 -> 128 + 128; P6 = 128.", "254 KB"),
    ("9 - libera P5", [("P6",128,green),("Livre",128,gray),("Livre",256,gray),("P2",512,green),("P4",512,green),("Livre",512,gray)], "Merge 256 + 256 -> 512 no final da memória.", "254 KB"),
    ("10 - libera P2", [("P6",128,green),("Livre",128,gray),("Livre",256,gray),("Livre",512,gray),("P4",512,green),("Livre",512,gray)], "Não ocorre merge: o buddy de P2 é o bloco que contém P6 e livres de 128/256 KB.", "254 KB"),
    ("11 - aloca P7 (350 KB)", [("P6",128,green),("Livre",128,gray),("Livre",256,gray),("P7",512,green),("P4",512,green),("Livre",512,gray)], "Usa o bloco livre de 512 KB. Fragmentação de P7 = 512 - 350 = 162 KB.", "170 KB (P6 + P7)"),
    ("12 - libera P4", [("P6",128,green),("Livre",128,gray),("Livre",256,gray),("P7",512,green),("Livre",1024,gray)], "Merge 512 + 512 -> 1024 no intervalo 1024-2048 KB.", "170 KB"),
]
for title, blocks, split, frag in steps2:
    story += [P(title, "H2A"), buddy_row("Blocos", blocks), P(f"<b>Merge/observação:</b> {split} &nbsp;&nbsp; <b>Fragmentação interna ativa:</b> {frag}", "SmallA"), Spacer(1,.10*cm)]

story += [PageBreak(), P("Estado final e resumo", "H1A"), P("Depois de todas as operações, a memória fica assim, do menor para o maior endereço:", "BodyA")]
story += [table([[P("Intervalo (KB)","HeaderCell"),P("Tamanho", "HeaderCell"),P("Estado", "HeaderCell"),P("Observação", "HeaderCell")], [P("0-128"),P("128 KB"),P("P6"),P("Solicitou 120 KB; 8 KB internos")], [P("128-256"),P("128 KB"),P("Livre"),P("Não pode ser unido ao bloco livre seguinte")], [P("256-512"),P("256 KB"),P("Livre"),P("Buddy diferente; não há merge")], [P("512-1024"),P("512 KB"),P("P7"),P("Solicitou 350 KB; 162 KB internos")], [P("1024-2048"),P("1024 KB"),P("Livre"),P("Resultado do merge após liberar P4")]], [3.2*cm,2.4*cm,2.5*cm,8.3*cm], row_bg={1:green,2:gray,3:gray,4:green,5:gray})]
story += [Spacer(1,.35*cm), P("Totais", "H2A")]
story += [table([[P("Métrica", "HeaderCell"), P("Cálculo", "HeaderCell"), P("Resultado", "HeaderCell")], [P("Fragmentação interna ativa"), P("(256 - 200) não conta mais, pois P1 foi liberado; P6: 128 - 120; P7: 512 - 350"), P("<b>170 KB</b>")], [P("Fragmentação externa / espaço livre"), P("128 + 256 + 1024"), P("<b>1408 KB</b>")], [P("Fragmentação total, somando as duas"), P("170 + 1408"), P("<b>1578 KB</b>")]], [4.0*cm,9.3*cm,3.1*cm], row_bg={1:colors.white,2:gray,3:orange})]
story += [Spacer(1,.35*cm), P("Em outras palavras: os processos que continuam na memória desperdiçam <b>170 KB</b> dentro dos próprios blocos, enquanto existem <b>1408 KB</b> livres, mas distribuídos em blocos que não podem ser juntados naquele momento. Se a questão pedir uma soma única, temos <b>1578 KB</b>; na prática, é melhor mostrar os dois valores separados.", "NoteA")]

doc = SimpleDocTemplate(OUT, pagesize=A4, rightMargin=1.6*cm, leftMargin=1.6*cm, topMargin=1.5*cm, bottomMargin=1.6*cm, title="Respostas - Alocação de Memória")
doc.build(story, onFirstPage=footer, onLaterPages=footer)
print(OUT)
