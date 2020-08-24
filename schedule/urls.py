from django.conf.urls import url
from django.urls import path
from django.contrib.auth.decorators import login_required
from schedule import views


urlpatterns = [
    path('calendario', login_required(views.CalendarView.as_view()), name='calendar'),
    path('calendario/<int:pk>', login_required(views.CalendarDirectView.as_view()), name='calendar_direct'),
    path('evento/nuevo/', login_required(views.EventCreateView), name='event_new'),
    path('evento/', login_required(views.EventListView.as_view()), name='event_list'),
    path('evento/editar/<int:pk>/', login_required(views.EventCreateView), name='event_edit'),
    path('evento/eliminar/<int:pk>/', login_required(views.EventDelete), name='event_delete'),


    path('citas/', login_required(views.DatesListView.as_view()), name='dates_list'),
    path('citas/nuevo/', login_required(views.DatesCreateView), name='dates_new'),
    path('citas/editar/<int:pk>/', login_required(views.DatesCreateView), name='dates_edit'),
    path('citas/eliminar/<int:pk>/', login_required(views.DatesDelete), name='dates_delete'),
    path('citas/nuevo_directo/<int:pk>/', login_required(views.DatesDirectCreateView.as_view()), name='dates_new_direct'),
    path('citas/cancelar/<int:pk>/', login_required(views.DatesCancelView.as_view()), name='dates_cancel'),
    path('citas/aceptar/<int:pk>/', login_required(views.DatesAcceptView.as_view()), name='dates_accept'),

    path('buscar/', login_required(views.SearchRequestedView.as_view()), name='search'),




]