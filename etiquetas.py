import sys

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import legal
from reportlab.platypus import  Table, TableStyle, Image
from reportlab.lib import colors
from reportlab.lib.units import inch

def create_pdf(filename):
    a = Image(filename)
    a.drawHeight = 2.25*inch
    a.drawWidth = 4*inch
    data=[[a,a],[a,a],[a,a],[a,a],[a,a],[a,a]]
    prefix = filename[:-4]
    output_filename = f"Etiquetas {prefix}.pdf"
    c = canvas.Canvas(output_filename, pagesize=legal)
    table = Table(data, colWidths=a.drawWidth, rowHeights=a.drawHeight)
    table.setStyle(TableStyle([
                            ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                            ('BOX', (0,0), (-1,-1), 0.25, colors.black),
                            ('BACKGROUND',(0,0),(-1,2),colors.lightgrey)
                            ]))
    table.wrapOn(c, 0, 0)
    table.drawOn(c,0,0)
    c.save()
    print(f"Salida {output_filename} exitosa")

filename = sys.argv[-1]
if not (filename.endswith('.jpg') or filename.endswith('.png')):
    raise ValueError("filename should be image with jpg or png extension")
create_pdf(filename)
