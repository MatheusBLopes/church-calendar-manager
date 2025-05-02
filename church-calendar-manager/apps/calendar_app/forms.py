from django import forms

from .models import ConflitoMarcado, Evento


class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['titulo', 'descricao', 'data', 'hora_inicio', 'hora_fim', 'ministerio', 'ocorreu']

class JustificativaConflitoForm(forms.ModelForm):
    class Meta:
        model = ConflitoMarcado
        fields = ['justificativa']
