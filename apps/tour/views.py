from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin

from .forms import GuideForm, DriverForm
from .models import Boot, Voyage


# Create your views here.


class IndexView(TemplateView):
    template_name = 'tour/index.html'


class GuideView(SuccessMessageMixin, FormView):
    form_class = GuideForm
    template_name = 'tour/guide.html'
    success_message = '提交成功'
    success_url = reverse_lazy('tour:guide')

    def form_valid(self, form):
        form.save()
        return super(GuideView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(GuideView, self).get_context_data(**kwargs)
        context['boot'] = Boot.objects.get(pk=1)
        return context


class DriverView(SuccessMessageMixin, UpdateView):
    model = Boot
    template_name = 'tour/driver.html'
    form_class = DriverForm
    success_message = '提交成功'
    success_url = reverse_lazy('tour:driver')

    def get_context_data(self, **kwargs):
        voyage = Voyage.objects.all()
        context = super(DriverView, self).get_context_data(**kwargs)
        context['voyage'] = voyage
        return context

    def form_valid(self, form):
        form.save()
        return super(DriverView, self).form_valid(form)
