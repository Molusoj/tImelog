from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import redirect
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView

from .models import TimeLog

# Create your views here.
class TimeLogListView(LoginRequiredMixin, ListView):
    """docstring for TimelogView"""
    model = TimeLog
    template_name = "home.html"
    context_object_name = 'timelogs'

    def get_queryset(self):
        timelogs = super().get_queryset()
        return timelogs.filter(user_id=self.request.user)  # returns the  timelog according to user_id


class TimeLogCreateView(LoginRequiredMixin, CreateView):
    """docstring for TimeLogCreateView"""
    model = TimeLog
    template_name = "timelog_form.html"
    fields = ['CI_CO']
    context_object_name = 'timelogs'
    success_url = '/'

    # to validate the form
    def form_valid(self, form):
        form.instance.user_id = self.request.user
        return super().form_valid(form)


def error(self):
    return render(request, 'error.html')
