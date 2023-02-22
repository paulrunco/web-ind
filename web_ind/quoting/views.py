from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.http import HttpResponse

from quoting.models import Quote, Line



class QuoteListView(ListView):
    model = Quote
    context_object_name = 'quotes'

class QuoteDetailView(DetailView):
    model = Quote
    context_object_name = 'quote'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        slug = self.kwargs['pk']
        print(slug)
        context['lines'] = Line.objects.filter(quote=slug)
        return context