from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404, render
from django.views import generic
from .models import Faq, Answer

class FaqListView(generic.ListView):
    #model = models.Faq
    template_name = 'index.html'
    def get_queryset(self):
        return Faq.objects.order_by("-created_at")

class FaqEditView(generic.UpdateView):
    model = Faq
    template_name = 'edit_faq.html'

class FaqCreateView(generic.CreateView):
    model = Faq
    fields = ['title','category','content']
    template_name = 'create_faq.html'
    def create(request):
        faq = get_object_or_404(Faq)
        title = faq.title
        content = faq.content
        category = faq.category
        created_at = faq.created_at
        updated_at = faq.updated_at
        


class FaqDetailView(generic.DetailView):
    model = Faq
    template_name = 'detail_faq.html'