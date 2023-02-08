from django.shortcuts import render
from django.views.generic import TemplateView, View
from .models import *


class HomePageView(TemplateView):
    template_name = "home.html"


class DashBoardPageView(TemplateView):
    template_name = "dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # print("Connected...")
        kw = self.request.GET.get("carname")
        context["all_cars"] = Car.objects.all().order_by("-id")
        context["car_detail"] = Car.objects.get(car_id=kw)
        context["driver"] = Driver.objects.get(drive_car=context["car_detail"].id)
        return context
