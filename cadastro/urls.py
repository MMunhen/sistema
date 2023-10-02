from django.urls import path
from cadastro import views

urlpatterns = [
    path('', views.index, name='index'),
    path('print', views.print_em_html, name='print'),  
    #Cursos
    path('listar_curso', views.listarCursos, name = "listarCurso"),
    path('incluir_curso', views.incluirCurso, name = "incluirCurso"),
    path('editar_curso/<int:id>', views.editarCurso, name = "editarCurso"),
    path('excluir_curso/<int:id>', views.excluirCurso, name = "excluirCurso"),
    #Turmas
    path('listar_turma', views.listarTurmas, name = "listarTurma"),



    #Professores
    path('listar_professor', views.listarProfessores, name = "listarProfessor"),
    path('incluir_professor', views.incluirProfessor, name = "incluirProfessor"),
    path('editar_professor/<int:id>', views.editarProfessor, name = "editarProfessor"),
    path('excluir_professor/<int:id>', views.excluirProfessor, name = "excluirProfessor"),
    #Alunos
    path('listar_aluno', views.listarAlunos, name = "listarAluno"),
    path('incluir_aluno', views.incluirAluno, name = "incluirAluno"),
    path('editar_aluno/<int:id>', views.editarAluno, name = "editarAluno"),
    path('excluir_aluno/<int:id>', views.excluirAluno, name = "excluirAluno"),
]