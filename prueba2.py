from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, Table, TableStyle, Image
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.lib import colors
from reportlab.lib.units import inch

a = Image("Sazonadores del mundo.jpg")  
a.drawHeight = 2.25*inch
a.drawWidth = 4*inch
data=[[a,a],[a,a],[a,a],[a,a],[a,a]]
c = canvas.Canvas("salida.pdf", pagesize=A4)
table = Table(data, colWidths=a.drawWidth, rowHeights=a.drawHeight)
table.setStyle(TableStyle([
                           ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                           ('BOX', (0,0), (-1,-1), 0.25, colors.black),
                           ('BACKGROUND',(0,0),(-1,2),colors.lightgrey)
                           ]))
table.wrapOn(c, 200, 400)
table.drawOn(c,0,0)
c.save()