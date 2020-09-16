from reportlab.pdfgen import canvas
from reportlab.lib.units import mm

def coord(x, y, unit=1):
    x, y = x * unit, y * unit
    return x, y

c = canvas.Canvas('hola.pdf', bottomup=0)

c.drawString(*coord(15, 20, mm), text='Bienvenidos nuevamente a Reportlab!')
c.showPage()
c.save()
