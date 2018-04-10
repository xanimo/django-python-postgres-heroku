from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.edit import DeleteView
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from .forms import SnippetForm
from .models import Snippet

# Create your views here.
class SnippetListView(ListView):
    model = Snippet
    template_name = 'snippets/home.html'

    def get_context_data(self, **kwargs):
        context = super(SnippetListView, self).get_context_data(**kwargs)
        return context

class SnippetDetailView(DetailView):
    model = Snippet
    template_name = 'snippets/detail.html'

class SnippetDeleteView(DeleteView):
    model = Snippet
    template_name = 'snippets/snippet_confirm_delete.html'
    success_url = '/'


def new(request):
    if request.method == 'POST':
        form = SnippetForm(request.POST)
        if form.is_valid():
            Snippet(
            title= form.cleaned_data['title'],
            language= form.cleaned_data['language'],
            snippet= form.cleaned_data['snippet'],
            description= form.cleaned_data['description']).save()
            return redirect('/')
    else:
        context = { 'header': 'GET', 'form': SnippetForm() }
        return render(request, 'snippets/new.html', context)