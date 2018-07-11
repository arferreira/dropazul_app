from django.shortcuts import render, render_to_response
from django.http.response import Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from django.contrib import messages

from question.models import Tag
from question.forms import TagForm


@login_required
@csrf_exempt
def tag_list(request):
    u"""
    Visão para listagem das questões cadastradas
    """
    if request.method == 'GET':
        return render(
            request,
            'tag_list.html',
            {
                'request': request,
                'tags': Tag.objects.all()
            })
    else:
        raise Http404()


@login_required
@csrf_exempt
def tag_add(request):
    u"""

    Cria uma nova questão

    """
    if request.method == 'GET':
        return render(
            request,
            'tag_form.html',
            {
                'request': request,
                'form': TagForm
            })
    elif request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            tag = form.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Tag criada com sucesso'
            )
            return HttpResponseRedirect(reverse('tag_list'))
        else:
            return render_to_response(
                'tag_form.html',
                {
                    'request': request,
                    'form': form
                })


@login_required
@csrf_exempt
def tag_edit(request, tag_id):
    u"""

    Editar uma questão existente

    """
    try:
        tag = Tag.objects.get(pk=tag_id)
    except Tag.DoesNotExist:
        raise Http404()

    if request.method == 'GET':
        form = TagForm(instance=tag)
        return render(
            request, 'tag_form.html',
            {
                'form': form,
            }
        )
    elif request.method == 'POST':
        form = TagForm(request.POST, instance=tag)
        if form.is_valid():
            form.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Tag Editada com sucesso'
            )
            return HttpResponseRedirect(reverse('tag_list'))
        else:
            return render_to_response(
                'tag_form.html',
                {
                    'request': request,
                    'form': form
                })
    else:
        raise Http404()


@login_required
@csrf_exempt
def tag_delete(request, tag_id):
    try:
        tag = Tag.objects.get(pk=tag_id)
    except Tag.DoesNotExist:
        raise Http404()
    if request.method == 'GET':
        tag.delete()
        return HttpResponseRedirect(reverse('tag_list'))
    else:
        raise Http404()
