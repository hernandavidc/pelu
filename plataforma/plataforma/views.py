from django.views.generic import TemplateView
from django.shortcuts import render

class HomePageView(TemplateView):
    template_name = "plataforma/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class DashboardPageView(TemplateView):
    template_name = "plataforma/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context