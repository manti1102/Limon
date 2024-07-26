from django.shortcuts import render
from django.views.generic import TemplateView
from journal.models import Publication

class HomeView(TemplateView):
    template_name = 'index.html'

class AboutView(TemplateView):
    template_name = 'about.html'


# Create your views here.
class Publication_detailView(TemplateView):
    template_name = 'publication-detail.html'
    def get_context_data(self, **kwargs):
        publication_pk = kwargs['pk']
        context ={
            'publication': Publication.objects.get(publication_pk)
        }
        return context