from django.contrib.admin.widgets import AdminSplitDateTime
from django.forms import TextInput, Textarea, Select, DateTimeInput, SplitDateTimeWidget, TimeInput, DateInput

from authentication.models import UserProfile
from .models import Event, Dates
from django import forms


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ["title", "description", "date_start_time", "time_start_time", "date_end_time",
                  "time_end_time"]

        widgets = {
            "title": TextInput(attrs={"class": "form-control", 'placeholder': 'Titulo', }),
            "description": Textarea(attrs={"class": "form-control", 'placeholder': 'Descripcion', }),
            "time_start_time": TimeInput(attrs={"class": "form-control", "type": "time"}),
            "date_start_time": DateInput(attrs={"class": "form-control", "type": "date"}),
            "time_end_time": TimeInput(attrs={"class": "form-control", "type": "time"}),
            "date_end_time": DateInput(attrs={"class": "form-control", "type": "date"}),
        }
        labels = {
            "title": "Titulo",
            "description": "Descripcion",
            "time_start_time": "Hora Inicio",
            "date_start_time": "Fecha Inicio",
            "time_end_time": "Hora Fin",
            "date_end_time": "Fecha Fin",
        }


class DatesForm(forms.ModelForm):
    class Meta:
        model = Dates
        fields = ["title", "description", "agent", "date_start_time", "time_start_time", "date_end_time",
                  "time_end_time"]
        widgets = {
            "title": TextInput(attrs={"class": "form-control", 'placeholder': 'Titulo', }),
            "description": Textarea(attrs={"class": "form-control", 'placeholder': 'Descripcion', }),
            "agent": Select(attrs={"class": "form-control"}),
            "time_start_time": TimeInput(attrs={"class": "form-control", "type": "time"}),
            "date_start_time": DateInput(attrs={"class": "form-control", "type": "date"}),
            "time_end_time": TimeInput(attrs={"class": "form-control", "type": "time"}),
            "date_end_time": DateInput(attrs={"class": "form-control", "type": "date"}),
        }
        labels = {
            "title": "Titulo",
            "agent": "Solicitado",
            "description": "Descripcion",
            "time_start_time": "Hora Inicio",
            "date_start_time": "Fecha Inicio",
            "time_end_time": "Hora Fin",
            "date_end_time": "Fecha Fin",
        }

    def __init__(self, *args, **kwargs):
        super(DatesForm, self).__init__(*args, **kwargs)
        self.fields['agent'].queryset = UserProfile.objects.filter(user__groups__name__exact="Solicitado")


class DatesFormRaul(forms.ModelForm):
    class Meta:
        model = Dates
        fields = ["title", "description", "agent", "date_start_time", "time_start_time", "date_end_time",
                  "time_end_time"]
        widgets = {
            "title": TextInput(attrs={"class": "form-control", 'placeholder': 'Titulo', }),
            "description": Textarea(attrs={"class": "form-control", 'placeholder': 'Descripcion', }),
            "agent": Select(attrs={"class": "form-control"}),
            "time_start_time": TimeInput(attrs={"class": "form-control", "type": "time"}),
            "date_start_time": DateInput(attrs={"class": "form-control", "type": "date"}),
            "time_end_time": TimeInput(attrs={"class": "form-control", "type": "time"}),
            "date_end_time": DateInput(attrs={"class": "form-control", "type": "date"}),
        }
        labels = {
            "title": "Titulo",
            "agent": "Solicitado",
            "description": "Descripcion",
            "time_start_time": "Hora Inicio",
            "date_start_time": "Fecha Inicio",
            "time_end_time": "Hora Fin",
            "date_end_time": "Fecha Fin",
        }

    def __init__(self, *args, **kwargs):
        self.pk = kwargs.pop('pk')
        super(DatesFormRaul, self).__init__(*args, **kwargs)
        self.fields['agent'].queryset = UserProfile.objects.filter(id=self.pk)
        self.fields['agent'].initial = UserProfile.objects.get(id=self.pk)
