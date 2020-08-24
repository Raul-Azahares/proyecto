import calendar
from datetime import datetime, date, timedelta
from datetime import datetime as dt
import datetime
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.utils.safestring import mark_safe
from social_core.backends import username

from authentication.decorators import allowed_user
# from authentication.signals import userprofile
from facebook.settings import REQUESTED_GROUP_NAME, APPLICANT_GROUP_NAME
from .forms import EventForm, DatesForm, DatesFormRaul
from .models import *
from .utils import Calendar, CalendarDirect
from django.utils.decorators import method_decorator





#@method_decorator(allowed_user(allowed_roles=[REQUESTED_GROUP_NAME]), name='dispatch')
class CalendarView(generic.ListView):
    """
    @Desc: Crea el calendario mostrando los eventos creados por el usuario
    """
    model = Event
    template_name = 'event/calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        d = get_date(self.request.GET.get('month', None))
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)

        pk_owner = self.request.user.profile.pk
        cal = Calendar(d.year, d.month, pk_owner)

        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        return context


class CalendarDirectView(generic.ListView):
    """
    @Desc: Crea el calendario mostrando los eventos creados por el usuario,al solicitante ,
    sin los links para editar dichos eventos
    """
    model = Event
    template_name = 'event/calendar_direct.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        d = get_date(self.request.GET.get('month', None))
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        context['pk'] = self.kwargs['pk']
        context['username'] = UserProfile.objects.get(pk=self.kwargs['pk']).user.username
        pk_owner = self.kwargs['pk']

        cal = CalendarDirect(d.year, d.month, pk_owner)

        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        return context


def prev_month(d):
    """
    @Desc: Devuelve el mes anterior del calendario
    """
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month


def next_month(d):
    """
    @Desc: Devuelve el proximo mes del calendario
    """
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month


def get_date(req_day):
    """
    @Desc: Devuelve la fecha  en el calendario
    """
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return dt.today()


#@allowed_user(allowed_roles=[REQUESTED_GROUP_NAME])
def EventCreateView(request, pk=None):
    """
    @Desc: Crea o edita un Evento
    """
    if pk:
        instance = get_object_or_404(Event, pk=pk)
    else:
        instance = Event()
        instance.owner = request.user.profile

    form = EventForm(request.POST or None, instance=instance)
    if request.POST and form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('calendar'))
    return render(request, 'event/event_add.html', {'form': form})


#@allowed_user(allowed_roles=[APPLICANT_GROUP_NAME])
def DatesCreateView(request, pk=None):
    """
    @Desc: Crea o edita una Cita
    """
    if pk:
        instance = get_object_or_404(Dates, pk=pk)
    else:
        instance = Dates()
        instance.requester = request.user.profile

    form = DatesForm(request.POST or None, instance=instance)
    model = "Citas"
    if request.POST and form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('dates_list'))
    return render(request, 'dates/dates_add.html', {'form': form, 'model': model})


#@method_decorator(allowed_user(allowed_roles=[REQUESTED_GROUP_NAME]), name='dispatch')
class EventListView(generic.ListView):
    """
    @Desc: Devuelve la lista de Eventos por usuario autenticado
    """
    model = Event
    context_object_name = 'events'
    template_name = "event/event_list.html"


    def get_context_data(self, **kwargs):
        context = super(EventListView, self).get_context_data(**kwargs)
        context['model'] = 'Eventos'
        return context

    def get_queryset(self):
        return Event.objects.filter(owner=self.request.user.profile)


#@method_decorator(allowed_user(allowed_roles=[APPLICANT_GROUP_NAME]), name='dispatch')
class DatesListView(generic.ListView):
    """
    @Desc: Devuelve la lista de Citas por usuario autenticado
    """
    model = Dates
    context_object_name = 'dates'
    template_name = "dates/dates_list.html"

    def get_context_data(self, **kwargs):
        context = super(DatesListView, self).get_context_data(**kwargs)
        context['model'] = 'Citas'
        return context

    def get_queryset(self):
        if self.request.user.groups.all()[0].name == REQUESTED_GROUP_NAME:
            return Dates.objects.filter(agent=self.request.user.profile)
        else:
            return Dates.objects.filter(requester=self.request.user.profile)


#@allowed_user(allowed_roles=[REQUESTED_GROUP_NAME])
def EventDelete(request, pk):
    """
    @Desc: Elimina un Evento
    """
    Event.objects.get(pk=pk).delete()
    return HttpResponseRedirect(reverse('event_list'))


#@allowed_user(allowed_roles=[APPLICANT_GROUP_NAME])
def DatesDelete(request, pk):
    """
    @Desc: Elimina una Cita
    """
    Dates.objects.get(pk=pk).delete()
    return HttpResponseRedirect(reverse('dates_list'))

#@method_decorator(allowed_user(allowed_roles=[APPLICANT_GROUP_NAME]), name='dispatch')
class SearchRequestedView(generic.ListView):
    """
    @Desc: Devuelve la lista de usuarios solicitados por una busqueda personalizada
    """
    model = UserProfile
    template_name = 'requested/search_result.html'

    def get_queryset(self):
        query = self.request.GET.get('q', None)
        object_list = None
        if query:
            object_list = UserProfile.objects.filter(
                Q(user__username__contains=query) & Q(user__groups__name=REQUESTED_GROUP_NAME))
        return object_list


class DatesDirectCreateView(generic.CreateView):
    """
    @Desc: Crea una Cita a partir de la busqueda realizada por el usuario
    """
    template_name = 'dates/dates_add.html'
    form_class = DatesFormRaul
    model = Dates
    success_url = reverse_lazy('dates_list')

    def dispatch(self, *args, **kwargs):
        return super(DatesDirectCreateView, self).dispatch(*args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super(DatesDirectCreateView, self).get_form_kwargs()
        kwargs.update({'pk': self.kwargs['pk']})
        return kwargs

    def form_valid(self, form):
        dates = form.save(commit=False)
        dates.agent = UserProfile.objects.get(pk=self.kwargs['pk'])
        dates.requester = self.request.user.profile
        dates.save()
        return super(DatesDirectCreateView, self).form_valid(form)

    def get_success_url(self):
        return super(DatesDirectCreateView, self).get_success_url()


class DatesCancelView(generic.View):
    """
    @Desc: Cancela una cita, la pone en estado Cancelada
    """
    model = Dates
    success_url = reverse_lazy('dates_list')

    def get(self, request, *args, **kwargs):
        object = self.model.objects.get(pk=self.kwargs['pk'])
        object.state = STATE_DATES[4][0]
        object.save()
        return redirect(self.success_url)

class DatesAcceptView(generic.View):
    """
    @Desc: Cancela una cita, la pone en estado Aceptada
    """
    model = Dates
    success_url = reverse_lazy('dates_list')

    def get(self, request, *args, **kwargs):
        object = self.model.objects.get(pk=self.kwargs['pk'])
        object.state = STATE_DATES[1][0]
        object.save()
        return redirect(self.success_url)
