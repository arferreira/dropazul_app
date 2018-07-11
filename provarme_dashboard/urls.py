from django.conf.urls import url
from django.urls import path, include


# views Dashboard
from provarme_dashboard.dashboard.views import IndexView as dashboard_index


from provarme_dashboard.views import *



app_name="provarme_dashboard"

urlpatterns = [
    # Rota principal do dashboard
    path('', dashboard_index.as_view(), name='index'),

    # Alunos
    path('alunos/', CustomerListView.as_view(), name='customers'),
    path('aluno/novo', CustomerCreateView.as_view(), name='new_customer'),
    path('aluno/editar/<int:pk>', CustomerUpdateView.as_view(), name='update_customer'),
    path('aluno/excluir/<int:customer_id>', customer_delete, name='delete_customer'),


    # professores
    path('professores/', EmployeeListView.as_view(), name='employees'),
    path('professor/novo', EmployeeCreateView.as_view(), name='new_employee'),
    path('professor/editar/<int:pk>', EmployeeUpdateView.as_view(), name='update_employee'),
    path('professor/excluir/<int:employee_id>', employee_delete, name='delete_employee'),


    # Categorias
    path('categorias/', CategoryListView.as_view(), name='categories'),
    path('categoria/nova/', CategoryCreateView.as_view(), name='new_category'),
    path('categoria/editar/<int:pk>', CategoryUpdateView.as_view(), name='update_category'),
    path('categoria/excluir/<int:category_id>', category_delete, name='delete_category'),


    # Questões
    path('questoes/', QuestionListView.as_view(), name='questions'),
    path('questao/nova/', QuestionCreateView.as_view(), name='new_question'),
    path('questao/editar/<int:pk>', QuestionUpdateView.as_view(), name='update_question'),
    path('questao/excluir/<int:question_id>', question_delete, name='delete_question'),



]