from django.conf.urls import url, include

from .views import (
    QuestionListView, question_list, question_add, question_edit, question_delete,
    tag_list, tag_add, tag_edit, tag_delete, CategoryListView,
    CategoryCreateView, CategoryDeleteView, CategoryEditView,
    search_by_category)

urlpatterns = [
    # rotas para questões
    url(r'^ajax/search_by_category/$', search_by_category,
                                       name='search_by_category'),
    url(r'^$', QuestionListView.as_view(), name='question_list'),
    url(r'^nova/', question_add, name='question_add'),
    url(r'^editar/(?P<question_id>\d+)/$', question_edit,
                                           name='question_edit'),
    url(r'^excluir/(?P<question_id>\d+)/$', question_delete,
                                            name='question_delete'),

    # rotas para as categorias
    url(r'^categorias/$', CategoryListView.as_view(),
                          name='category_list'),
    url(r'^categorias/nova/$', CategoryCreateView.as_view(),
                               name='category_add'),
    url(r'^categorias/editar/(?P<slug>[\w_-]+)/$', CategoryEditView.as_view(),
                                                   name='category_edit'),
    url(r'^categorias/excluir/(?P<pk>\d+)/$', CategoryDeleteView.as_view(),
                                              name='category_delete'),

    # rotas para as tags
    url(r'^tags/$', tag_list, name='tag_list'),
    url(r'^tags/nova/$', tag_add, name='tag_add'),
    url(r'^tags/editar/(?P<tag_id>\d+)/$', tag_edit, name='tag_edit'),
    url(r'^tags/excluir/(?P<tag_id>\d+)/$', tag_delete, name='tag_delete'),
]
