from openpyxl import Workbook

def create_excel(rows, total):
    wb = Workbook()
    ws = wb.active

    ws.append(["Item","No","L","B","D","Qty"])

    for r in rows:
        ws.append([
            r.item, r.no, r.length,
            r.breadth, r.depth, r.quantity
        ])

    ws.append(["","","","","Total", total])
    wb.save("output.xlsx")
