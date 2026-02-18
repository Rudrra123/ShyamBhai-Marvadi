from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Image
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.units import cm
from reportlab.platypus import HRFlowable
from datetime import datetime

# ================= FONT =================
pdfmetrics.registerFont(
    TTFont("Gujarati", "fonts/NotoSansGujarati-Regular.ttf")
)
today_date = datetime.now().strftime("%d-%m-%Y")
HEADER_HEIGHT = 60

# ================= HEADER =================
# def draw_header_background(canvas, doc):
#     canvas.saveState()

#     PAGE_WIDTH, PAGE_HEIGHT = A4

#     # WATERMARK
#     canvas.setFillAlpha(0.07)
#     canvas.drawImage(
#         "images/logo.png",
#         x=3 * cm,
#         y=5 * cm,
#         width=13 * cm,
#         height=13 * cm,
#         mask="auto"
#     )
#     canvas.setFillAlpha(1)

#     # TITLE
#     canvas.setFont("Gujarati", 15)
#     canvas.drawCentredString(
#         PAGE_WIDTH / 2,
#         PAGE_HEIGHT - 32,
#         "Measurement Sheet"
#     )

#     # HEADER LINE
#     canvas.setLineWidth(1.3)
#     canvas.line(
#         15,
#         PAGE_HEIGHT - HEADER_HEIGHT,
#         PAGE_WIDTH - 15,
#         PAGE_HEIGHT - HEADER_HEIGHT
#     )

#     canvas.restoreState()
def draw_header_background(canvas, doc):
    canvas.saveState()

    PAGE_WIDTH, PAGE_HEIGHT = A4

    logo_width = 140
    logo_height = 120
    header_height = 80

    # ===== LOGO (Left) =====

    canvas.drawImage(
        "Images/logo.png",
        x=10,
        y=PAGE_HEIGHT - header_height + (header_height - logo_height) / 2,
        width=logo_width,
        height=logo_height,
        mask="auto"
    )

    # ===== COMPANY NAME (CENTER) =====
    canvas.setFont("Gujarati", 18)
    canvas.drawCentredString(
        PAGE_WIDTH / 2,
        PAGE_HEIGHT - 35,
        "AADESH CONSTRUCTION"
    )

    # ===== SUBTITLE (CENTER) =====
    canvas.setFont("Gujarati", 12)
    canvas.drawCentredString(
        PAGE_WIDTH / 2,
        PAGE_HEIGHT - 55,
        "Measurement Sheet"
    )

    # ===== LINE =====
    canvas.setLineWidth(1.5)
    canvas.line(
        15,
        PAGE_HEIGHT - 70,
        PAGE_WIDTH - 15,
        PAGE_HEIGHT - 70
    )
    # ===== WATERMARK =====
    canvas.saveState()

    canvas.setFillAlpha(0.08)  # Transparency (0.05–0.1 best)

    watermark_width = 500
    watermark_height = 500

    canvas.drawImage(
        "Images/logo.png",
        x=(PAGE_WIDTH - watermark_width) / 2,
        y=(PAGE_HEIGHT - watermark_height) / 2,
        width=watermark_width,
        height=watermark_height,
        mask="auto"
    )

    canvas.setFillAlpha(1)
    canvas.restoreState()

    canvas.restoreState()


# ================= PDF =================
def create_pdf(rows, total, header):

    pdf = SimpleDocTemplate(
        "output.pdf",
        pagesize=A4,
        leftMargin=15,
        rightMargin=15,
        topMargin=HEADER_HEIGHT + 15,
        bottomMargin=20
    )

    elements = []

    # ================= STYLES =================
    box_text = ParagraphStyle(
        name="box",
        fontName="Gujarati",
        fontSize=10,
        leading=16,
        alignment=0
    )

    th = ParagraphStyle(
        name="th",
        fontName="Gujarati",
        fontSize=9,
        leading=11,
        alignment=1
    )

    td = ParagraphStyle(
        name="td",
        fontName="Gujarati",
        fontSize=9,
        leading=11,
        alignment=1
    )

    bold_style = ParagraphStyle(
        name="bold",
        fontName="Gujarati",
        fontSize=10,
        leading=12,
        alignment=2
    )

    # ================= TOP INFO BOX =================
   # ================= TOP INFO BOX =================

    left_heading = Paragraph("<b>CLIENT DETAILS</b>", th)
    right_heading = Paragraph("<b>PROJECT DETAILS</b>", th)

    left_info = Paragraph(
        f"Name : {header.name}<br/>"
        f"Mobile : {header.mobile}<br/>"
        f"Site Address : {header.address}",
        box_text
    )

    right_info = Paragraph(
        f"Name of Work : {header.work_name}<br/>"
        f"Date : {today_date}",
        box_text
    )

    top_table = Table(
        [
            [left_heading, right_heading],
            [left_info, right_info]
        ],
        colWidths=[280, 280],
    )

    top_table.setStyle(TableStyle([

        # Thin outer border
        ("BOX", (0,0), (-1,-1), 0.8, colors.HexColor("#b5b5b5")),

        # Thin vertical divider
        ("LINEBEFORE", (1,0), (1,-1), 0.6, colors.HexColor("#d0d0d0")),

        # Heading background
        ("BACKGROUND", (0,0), (-1,0), colors.HexColor("#f2f2f2")),

        # Line below heading row
        ("LINEBELOW", (0,0), (-1,0), 0.8, colors.HexColor("#b5b5b5")),

        # Padding
        ("LEFTPADDING", (0,0), (-1,-1), 15),
        ("RIGHTPADDING", (0,0), (-1,-1), 15),
        ("TOPPADDING", (0,0), (-1,-1), 6),
        ("BOTTOMPADDING", (0,0), (-1,-1), 6),

        ("VALIGN", (0,0), (-1,-1), "TOP"),
    ]))



    # top_table.setStyle(TableStyle([
    #     ("BOX", (0,0), (-1,-1), 1.2, colors.black),
    #     ("BACKGROUND", (0,0), (-1,-1), colors.whitesmoke),
    #     ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
    #     ("LEFTPADDING", (1,0), (1,0), 20),
    #     ("TOPPADDING", (0,0), (-1,-1), 10),
    #     ("BOTTOMPADDING", (0,0), (-1,-1), 10),
    # ]))

    elements.append(top_table)
    elements.append(Spacer(1, 12))


    PAGE_WIDTH, PAGE_HEIGHT = A4
    usable_width = PAGE_WIDTH - pdf.leftMargin - pdf.rightMargin

    colWidths = [
      usable_width * 0.08,  # Item No
        usable_width * 0.28,  # Items
        usable_width * 0.06,  # No
        usable_width * 0.08,  # Length
        usable_width * 0.10,  # Breadth
        usable_width * 0.14,  # Quantity
        usable_width * 0.12,  # Price
        usable_width * 0.13,  # Total Price
    ]

    # ================= MAIN TABLE =================
    data = [[
        Paragraph("Item No<br/>(આઇટમ નંબર)", th),
        Paragraph("Items<br/>(આઇટમ)", th),
        Paragraph("No<br/>(નંબર)", th),
        Paragraph("Length<br/>(લંબાઈ)", th),
        Paragraph("Breadth<br/>(પહોળાઈ)", th),
        Paragraph("Total Quantity<br/>(કુલ માપ)", th),
        Paragraph("Price<br/>(દર)", th),
        Paragraph("Total Price<br/>(કુલ રકમ)", th),
    ]]

    for i, r in enumerate(rows, start=1):
        data.append([
            Paragraph(str(i), td),
            Paragraph(r.item, td),
            Paragraph(str(r.no), td),
            Paragraph(str(r.length), td),
            Paragraph(str(r.breadth), td),
            Paragraph(str(r.quantity), td),
            Paragraph(str(r.price), td),
            Paragraph(str(r.total_price), td),
        ])

    # TOTAL ROW
    data.append([
        "", "", "", "", "", "",
        Paragraph("<b>Grand Total</b>", bold_style),
        Paragraph(f"<b>{total}</b>", bold_style)
    ])

    table = Table(
        data,
        colWidths,
        repeatRows=1
    )

    table.setStyle(TableStyle([

        # Outer border light
        ("BOX", (0,0), (-1,-1), 0.8, colors.HexColor("#b5b5b5")),

        # Inner grid light
        ("INNERGRID", (0,0), (-1,-1), 0.4, colors.HexColor("#e0e0e0")),

        # Header background
        ("BACKGROUND", (0,0), (-1,0), colors.HexColor("#f2f2f2")),

        # Strong line below header
        ("LINEBELOW", (0,0), (-1,0), 0.9, colors.HexColor("#b5b5b5")),

        # Total row highlight
        ("BACKGROUND", (0,-1), (-1,-1), colors.HexColor("#f7f7f7")),
        ("LINEABOVE", (0,-1), (-1,-1), 0.9, colors.HexColor("#b5b5b5")),

        # Align numbers right
        ("ALIGN", (2,1), (-1,-1), "RIGHT"),

        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
    ]))


    elements.append(table)
    elements.append(Spacer(1, 25))

    # ================= FOOTER =================
    elements.append(HRFlowable(width="100%", thickness=1))
    elements.append(Spacer(1, 10))

    footer_para = Paragraph(
        "Authorized Signature ____________________________<br/><br/>"
        "Thank You For Your Business",
        box_text
    )

    elements.append(footer_para)

    # ================= BUILD =================
    pdf.build(
        elements,
        onFirstPage=draw_header_background,
        onLaterPages=draw_header_background
    )
