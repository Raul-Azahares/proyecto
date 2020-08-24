from django.contrib.auth.models import Group
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
# Create your views here.
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import TemplateView

from schedule.choices import STATE_DATES
from schedule.models import Dates
from .decorators import unauthenticated_user
from .forms import SignUpForm, LoginForm, UserProfileUpdateForm
from .models import UserProfile


class NoAuthorize(TemplateView):
    template_name = 'accounts/401.html'


@unauthenticated_user
def loginPage(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username= username,password=password)

        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Username OR Password is incorrect')

    context = {'form':form}
    return render(request, 'accounts/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

@unauthenticated_user
def registerPage(request):
    form = SignUpForm()
    if request.method == 'POST':
      form = SignUpForm(request.POST)
      if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        messages.success(request,'Account was created for ' + username)
        return redirect('login')

    context = {'form': form}
    return render(request, 'accounts/register.html', context)


@login_required(login_url='login')
def home(request):
    group = ""
    if request.user.profile:
        for g in request.user.groups.all():
            print('Group name:', g.name, 'Group id:', g.id)
            group = g.name
            break

        if group == "Solicitante":
            # Counts
            dates_all = Dates.objects.filter(requester=request.user.profile).count()
            dates_pending = Dates.objects.filter(requester=request.user.profile, state=STATE_DATES[0][0]).count()

            # Details
            dates_detail_all = Dates.objects.filter(requester=request.user.profile, state=STATE_DATES[4][0] or STATE_DATES[5][0])
            dates_detail_pending = Dates.objects.filter(requester=request.user.profile, state=STATE_DATES[0][0])
        else:
            # Counts
            dates_all = Dates.objects.filter(agent=request.user.profile).count()
            dates_pending = Dates.objects.filter(agent=request.user.profile, state=STATE_DATES[0][0]).count()

            # Details
            dates_detail_all = Dates.objects.filter(agent=request.user.profile, state=STATE_DATES[4][0] or STATE_DATES[5][0])
            dates_detail_pending = Dates.objects.filter(agent=request.user.profile, state=STATE_DATES[0][0])

    return render(request, 'home.html', locals())


class profileUpdateView(generic.UpdateView):
    form_class =UserProfileUpdateForm
    template_name = 'accounts/profile_edit.html'
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        return self.request.user.profile

    def form_valid(self, form):
        clean = form.cleaned_data
        self.object = form.save()
        return super(profileUpdateView, self).form_valid(form)

    def get_success_url(self):
        return super(profileUpdateView, self).get_success_url()



