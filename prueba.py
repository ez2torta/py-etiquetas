# From the FAQ at reportlab.org/oss/rl-toolkit/faq/#1.1
# Import some constructors, some paragraph styles and other conveniences from other modules.
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.rl_config import defaultPageSize
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.platypus import Image
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas
PAGE_HEIGHT = defaultPageSize[0]
PAGE_WIDTH = defaultPageSize[0]
defaultPageSize = letter
styles = getSampleStyleSheet()
Title = "Comparison Index"
pageinfo = "platypus example"
Image3 = 'Sazonadores del mundo.png'
# Define the fixed features of the first page of the document
def myFirstPage(canvas, doc):
    canvas.saveState()
    canvas.setFontSize(22)
    canvas.setFont('Helvetica-Bold', 36)
    canvas.drawString(50, 670, 'Health & Welfare')
    canvas.setFont('Helvetica-Bold', 24)
    canvas.drawString(50, 625, 'Benchmark Comparison Report')
    canvas.setFont('Helvetica', 16)
    canvas.drawString(50, 550, 'Prepared for:')
    canvas.setFont('Times-Roman', 12)
    canvas.drawString(inch, 0.25 * inch, "First Page / %s" % pageinfo)
    canvas.restoreState()
# Since we want pages after the first to look different from the first we define an alternate layout for
# the fixed features of the other pages.
# Note that the two functions use the pdfgen level canvas operations to  paint the annotations for the pages.
def myLaterPages(canvas, doc):
    canvas.saveState()
    canvas.setFont('Times-Roman', 23)
    canvas.drawString(inch, 0.75 * inch, "Page %d %s" % (doc.page, pageinfo))
    canvas.restoreState()
def myThirdPages(canvas, doc):
    canvas.saveState()
    canvas.setFont('Times-Roman', 9)
    canvas.drawString(inch, 0.75 * inch, "Page %d %s" % (doc.page, pageinfo))
    canvas.restoreState()
# Create a story and build the document
def go():
    doc = SimpleDocTemplate("Comparison Index.pdf", pagesize=letter)
    # Story = [Spacer(1, 2 * inch)]
    Story = []

    # logo = "Sazonadores del mundo.jpg"
    # im = Image(logo, 7 * inch, 2 * inch)
    # Story.append(im)
    logo = "Sazonadores del mundo.png"
    im2 = Image(logo, 4 * inch, 4 * inch)
    Story.append(im2)
    Story.append(im2)
    Story.append(im2)
    doc.build(Story)
if __name__ == "__main__":
    go()
