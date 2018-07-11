from django.shortcuts import render, render_to_response
from django.http.response import Http404, HttpResponseRedirect, HttpResponse
from django.core import serializers
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.urls import reverse
from django.db import transaction
from django.http import JsonResponse

from question.models import Question
from question.forms import QuestionForm, QuestionAlternativesFormSet



class QuestionListView(LoginRequiredMixin, ListView):
    """
        Class Based View responsável pela listagem de todas as questões
    """
    model = Question
    template_name = 'question_list.html'

    def get_context_data(self, **kwargs):
        context = super(QuestionListView, self).get_context_data(**kwargs)
        context['questions'] = Question.objects.all()
        return context

@login_required
@csrf_exempt
def question_list(request):
    """
    Visão para listagem das questões cadastradas
    """
    if request.method == 'GET':
        return render(
            request,
            'question_list.html',
            {
                'questions': Question.objects.all()
            })
    else:
        raise Http404()


@login_required
@csrf_exempt
def question_add(request):
    """
    Cria uma nova questão
    """
    if request.method == 'GET':
        form = QuestionForm
        formset = QuestionAlternativesFormSet
        formset.extra = 4
        return render(
            request,
            'question_form.html',
            {
                'form': form,
                'formset': formset
            })
    elif request.method == 'POST':
        form = QuestionForm(request.POST)
        formset = QuestionAlternativesFormSet(request.POST)
        if form.is_valid() and formset.is_valid():
            #import pdb; pdb.set_trace()
            with transaction.atomic():
                question = form.save()
                formset.instance = question
                formset.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Questão criada com sucesso'
            )
            try:
                if request.POST['save-new'] == '':
                    return HttpResponseRedirect(reverse('question_add'))
            except:
                return HttpResponseRedirect(reverse('question_list'))
        else:
            return render_to_response(
                'question_form.html',
                {
                    'request': request,
                    'form': form,
                    'formset': QuestionAlternativesFormSet
                })


@login_required
@csrf_exempt
def question_edit(request, question_id):
    """
    Editar uma questão existente
    """
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404()

    if request.method == 'GET':
        form = QuestionForm(instance=question)
        formset = QuestionAlternativesFormSet(instance=question)
        formset.extra = 1
        return render(
            request,
            'question_form.html',
            {
                  'form': form,
                  'formset': formset,
            })
    elif request.method == 'POST':
        form = QuestionForm(request.POST, instance=question)
        formset = QuestionAlternativesFormSet(request.POST, instance=question)
        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Questão editada com sucesso'
            )
            try:
                if request.POST['save-new'] == '':
                    return HttpResponseRedirect(reverse('question_add'))
            except:
                return HttpResponseRedirect(reverse('question_list'))
        else:
            return render_to_response(
                'question_form.html',
                {
                    'request': request,
                    'form': form,
                    'formset': formset
                })
    else:
        raise Http404()


@login_required
@csrf_exempt
def question_delete(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404()
    if request.method == 'GET':
        question.delete()
        return HttpResponseRedirect(reverse('question_list'))
    else:
        raise Http404()

def search_by_category(request):
    import json
    if request.is_ajax():
        print("**ajax questions**")
        category = request.GET.get('category', None)
        return JsonResponse({'questions': list(Question.objects.filter(
                categories=category).values('id', 'wording'))})
