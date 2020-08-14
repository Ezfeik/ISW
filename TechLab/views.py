from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from TechLab.models import Usuario, Paciente
from django.contrib.auth.decorators import login_required
from TechLab.forms import PacienteForm, OrdenForm
from django.http import HttpResponse

# Create your views here.
def index(request):
    return redirect('/accounts/login/')

@login_required
def menu(request):
    if request.user.is_authenticated:
        user = request.user
        username = request.user.username
        aux = Usuario.objects.get(usuario=user)
        tipo = aux.tipo
        context = {
            'username': username,
            'tipo': tipo
        }
        return render(request, 'Horarios/menu.html', context)

@login_required
def pacientes(request):
    if request.method == "POST" and not request.POST.get('buscaRut'):
        p = Paciente.objects.order_by('rut')
    elif request.method == "POST":
        try:
            p = [Paciente.objects.get(rut=request.POST.get('buscaRut'))]
        except Paciente.DoesNotExist:
            p = None
    else:
        p = Paciente.objects.order_by('rut')
    context = {
        'pacientes': p
    }

    return render(request, 'Horarios/pacientes.html', context)

@login_required
def registrar(request):
    upload = PacienteForm()
    if request.method == "POST":
        upload = PacienteForm(request.POST)
        if upload.is_valid():
            upload.save()
            return redirect('/menu/pacientes/')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : '/menu/pacientes/'}}">reload</a>""")
    else:
        return render(request, 'Horarios/registro.html', {'upload_form': upload, 'funcion': 1})

@login_required
def editar(request, paciente_id):
    paciente_id = int(paciente_id)
    try:
        paciente_sel = Paciente.objects.get(id = paciente_id)
    except Paciente.DoesNotExist:
        return redirect('/menu/pacientes/')
    paciente_form = PacienteForm(request.POST or None, instance = paciente_sel)
    if paciente_form.is_valid():
       paciente_form.save()
       return redirect('/menu/pacientes/')
    return render(request, 'Horarios/registro.html', {'upload_form': paciente_form, 'funcion': 2})

@login_required
def ordenes(request):
    if request.method == "POST":
        p = Paciente.objects.get(rut=request.POST.get('rut'))
    return render(request, 'Horarios/ordenes.html')

@login_required
def generarOrden(request, paciente_id):
    paciente_id = int(paciente_id)
    try:
        paciente_sel = Paciente.objects.get(id = paciente_id)
    except Paciente.DoesNotExist:
        return redirect('/menu/pacientes/')

    orden_form = OrdenForm(initial={'paciente': paciente_sel})

    if request.method == "POST":
        orden_form = OrdenForm(request.POST)
        if orden_form.is_valid():
            orden_form.save()
            return redirect('/menu/pacientes/')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : '/menu/pacientes/'}}">reload</a>""")
    else:
        return render(request, 'Horarios/orden.html', {'upload_form': orden_form, 'p': paciente_sel})
