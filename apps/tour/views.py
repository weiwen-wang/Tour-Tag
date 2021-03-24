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
    success_message = 'submit successfully'
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
    success_message = 'submit successfully'
    success_url = reverse_lazy('tour:driver')

    def get_context_data(self, **kwargs):
        voyage = Voyage.objects.all()
        context = super(DriverView, self).get_context_data(**kwargs)
        context['voyage'] = voyage
        return context

    def form_valid(self, form):
        form.save()
        return super(DriverView, self).form_valid(form)

from django.db import models
from django.http import HttpResponse
import colorsys
import time
from threading import Timer
from sys import exit
from PIL import Image, ImageDraw, ImageFont
import unicornhathd
from django.shortcuts import render
from apps.tour.models import Guide

lines = [str(Guide.objects.latest('id')),str(Guide.objects.values('start').last()),str(Guide.objects.values('end').last())]
colours = (255, 0, 0)
FONT = ('/usr/share/fonts/truetype/freefont/FreeSansBold.ttf', 8)
unicornhathd.rotation(0)
unicornhathd.brightness(0.6)
width, height = unicornhathd.get_shape()
text_x = width
text_y = 3
font_file, font_size = FONT
font = ImageFont.truetype(font_file, font_size)
text_width, text_height = width, 0
for line in lines:
    w, h = font.getsize(line)
    text_width += w + width
    text_height = max(text_height, h)
text_width += width + text_x + 1
image = Image.new('RGB', (text_width, max(16, text_height)), (0, 0, 0))
draw = ImageDraw.Draw(image)
offset_left = 0
for index, line in enumerate(lines):
    draw.text((text_x + offset_left, text_y), line, colours, font=font)
    offset_left += font.getsize(line)[0] + width

cancel_tmr = False


#def light_view(request):
#    return render(request, 'tour/guide.html')


def turn_on(request):
    global cancel_tmr
    while cancel_tmr != True:
        for scroll in range(text_width - width):
            for x in range(width):
                for y in range(height):
                    pixel = image.getpixel((x + scroll, y))
                    r, g, b = [int(n) for n in pixel]
                    unicornhathd.set_pixel(width - 1 - x, y, r, g, b)
            unicornhathd.show()
            time.sleep(0.2)
    return render(request, 'tour/guide.html')
def turn_off(request):
    global cancel_tmr
    cancel_tmr = True
    unicornhathd.off()
    return render(request, 'tour/guide.html')
def refresh(request):
    global cancel_tmr
    cancel_tmr = False
    return render(request, 'tour/guide.html')