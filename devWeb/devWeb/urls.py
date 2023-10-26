from django.contrib import admin
from django.urls import path
from task import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('sair/', views.sair, name='sair'),
    path('tasks/', views.tasks, name='tasks'),
    path('criando/tarefa/', views.criandoTarefa, name='criandoTarefa'),
    path('criando/<int:task_id>/', views.taskDetalhe, name='taskDetalhe'), 
    path('criando/<int:task_id>/complete', views.completeTarefa, name='completeTarefa'), 
    path('criando/<int:task_id>/delete', views.deletarTarefa, name='deletarTarefa'), 
    path('exibir_tarefas_completadas', views.exibirTarefasCompletadas, name='exibirTarefasCompletadas'), 
    path('erro/', views.erro, name='404'),
]
