from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from .models import Entry

class BlogListView(ListView):
  model = Entry
  template_name = 'home.html'

class BlogDetailView(DetailView):
  model = Entry
  template_name = 'entry_detail.html'

class BlogCreateView(CreateView):
  model = Entry
  template_name = 'entry_new.html'
  fields = ['title', 'author', 'body']