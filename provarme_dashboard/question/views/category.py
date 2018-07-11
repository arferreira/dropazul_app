from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import render


from question.models import Category
from question.forms import CategoryForm


class CategoryListView(LoginRequiredMixin, ListView):
    """
        Class Based View responsável pela listagem de todas as categorias
    """
    model = Category
    template_name = 'category_list.html'

    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['nodes'] = Category.objects.all()
        return context


class CategoryCreateView(LoginRequiredMixin, CreateView):
    """
        Class based view responsável pela criação de uma categoria
    """
    model = Category
    form_class = CategoryForm
    template_name = 'category_form.html'
    success_url = reverse_lazy('category_list')


class CategoryEditView(LoginRequiredMixin, UpdateView):
    """
        Class based view responsável pela edição da categoria
    """
    model = Category
    form_class = CategoryForm
    template_name = 'category_form.html'
    success_url = reverse_lazy('category_list')


class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    """
        Class based view responsável por deletar categorias
    """
    model = Category
    success_url = reverse_lazy('category_list')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
