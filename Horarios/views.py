import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, Table, TableStyle, Image
from reportlab.lib.enums import TA_CENTER
from reportlab.lib import colors
from django.contrib.auth.models import User
from django.http import HttpResponse, FileResponse
from Horarios.models import Bloque, Horario, Profesor
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

def index(request):
    return render(request, 'Horarios/index.html')
    # return redirect('/accounts/login/')

@login_required
def profesor(request, profesor_id):
    profesorSelect = get_object_or_404(Profesor, pk=profesor_id-1)
    if request.method == "POST":
        datos = request.POST.getlist('bloque')
        d = ', '.join(datos)
        profesorSelect.dias_disp=d
        profesorSelect.save()
    bloqueList = Bloque.objects.order_by('h_inicio')
    context = {
        'bloqueList': bloqueList
    }
    return render(request, 'Horarios/profesor.html', context)

@login_required
def menu(request):
    return render(request, 'Horarios/menu.html')

def pdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=hello.pdf'
    p = canvas.Canvas(response, pagesize=A4)

    for profes in Profesor.objects.all():
        nombre = "Profesor: "+profes.nombres+" "+profes.apellidos
        p.drawString(100, 700, nombre)
        styles = getSampleStyleSheet()
        styleBH = styles["Normal"]
        styleBH.alignment = TA_CENTER
        styleBH.fontsize = 12

        hora = Paragraph('''Hora''',styleBH)
        Lu = Paragraph('''Lunes''',styleBH)
        Ma = Paragraph('''Martes''',styleBH)
        Mi = Paragraph('''Miercoles''',styleBH)
        Ju = Paragraph('''Jueves''',styleBH)
        Vi = Paragraph('''Viernes''',styleBH)
        Sa = Paragraph('''Sabado''',styleBH)

        data = []
        data.append([hora,Lu,Ma,Mi,Ju,Vi,Sa])

        styleN = styles['BodyText']
        styleN.alignment = TA_CENTER
        styleN.fontsize = 7

        high = 550
        for b in Bloque.objects.all():
            fila = [str(b.h_inicio.hour)+":"+str(b.h_inicio.minute)+" - "+str(b.h_fin.hour)+":"+str(b.h_fin.minute),'','','','','','']
            data.append(fila)
            high = high - 18

        print(data)
        for d in profes.dias_disp.split():
            d = d.strip(",")
            if d.endswith("Lu"):
                x = 1
            elif d.endswith("Ma"):
                x = 2
            elif d.endswith("Mi"):
                x = 3
            elif d.endswith("Ju"):
                x = 4
            elif d.endswith("Vi"):
                x = 5
            else:
                x = 6
            y = int(d.strip("Bloques_LuMaMiJuViSa,"))
            print(x," ",y)
            data[y][x] = "X"

        width, height = A4
        table = Table(data, colWidths=[4*cm, 2*cm, 2*cm, 2*cm, 2*cm, 2*cm, 2*cm])
        table.setStyle(TableStyle([
            ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
            ('BOX', (0,0), (-1,-1), 0.25, colors.black)
        ]))
        table.wrapOn(p, width, height)
        table.drawOn(p, 30, high)
        p.showPage()

    p.save()
    return response
