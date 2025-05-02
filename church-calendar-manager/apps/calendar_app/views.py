from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render

from .forms import EventoForm, JustificativaConflitoForm
from .models import ConflitoMarcado, Evento, Ministerio


@login_required
def create_event(request):
    form = EventoForm(request.POST or None)
    if form.is_valid():
        evento = form.save(commit=False)
        evento.criado_por = request.user
        if not request.user.is_superuser:
            evento.ministerio = request.user.ministerio
        evento.save()
        return redirect('events_list')
    return render(request, 'calendar/pages/event_form.html', {'form': form})

@login_required
def events_list(request):
    eventos = Evento.objects.all() if request.user.is_superuser else Evento.objects.filter(ministerio=request.user.ministerio)
    return render(request, 'calendar/pages/events_list.html', {'eventos': eventos})

@login_required
def home(request):
    return render(request, 'calendar/pages/home.html')

@login_required
def conflitos_de_datas(request):
    eventos = Evento.objects.values('data').annotate(total=Count('id')).filter(total__gt=1)
    datas_conflitantes = [e['data'] for e in eventos]
    eventos_conflitantes = Evento.objects.filter(data__in=datas_conflitantes)

    if request.method == "POST":
        e1 = get_object_or_404(Evento, id=request.POST['evento1_id'])
        e2 = get_object_or_404(Evento, id=request.POST['evento2_id'])
        justificativa = request.POST['justificativa']
        ConflitoMarcado.objects.create(evento1=e1, evento2=e2, justificativa=justificativa)
        return redirect('conflitos')

    return render(request, 'calendar/conflict_list.html', {
        'eventos': eventos_conflitantes,
        'conflitos': ConflitoMarcado.objects.all()
    })

class MyLoginView(LoginView):
    template_name = "calendar/pages/login.html"
