from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render
from cadastro.forms import AlunoForm, CursoForm, ProfessorForm

from cadastro.models import Aluno, Curso, Professor, Turma

# Create your views here.

def index(request):
    return render(request, "inicio.html")

def print_em_html(request):
    return HttpResponse("<h2>Um título</h2>")

def listarCursos(request):
    cursos = Curso.objects.all().order_by('nome')
    return render(request, "listar_cursos.html", {'lista':cursos})

def incluirCurso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                return redirect('listarCurso')
            except:
                pass
    else:
        form = CursoForm()
    return render(request, "incluir_curso.html", {'form': form})

def editarCurso(request, id):
    curso =  Curso.objects.get(id = id)
    form = CursoForm(instance=curso)

    if request.method == 'POST':
        form = CursoForm(request.POST, instance=curso)
        if form.is_valid():
            try:
                form.save()
                return redirect('listarCurso')
            except:
                pass

    return render(request, "incluir_curso.html", {'form': form})

def excluirCurso(request, id):
    curso = Curso.objects.get(id = id)
    try:
        curso.delete()
    except: 
        messages.error(request, "Não é possível excluir! (Curso vinculado com turma)")
    return redirect("listarCurso")

def listarTurmas(request):
    turmas = Turma.objects.all()
    return render(request, "listar_turmas.html", {'lista':turmas})







def listarProfessores(request):
    professores = Professor.objects.all().order_by('nome')
    return render(request, "listar_professores.html", {'lista':professores})

def incluirProfessor(request):
    if request.method == 'POST':
        form = ProfessorForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                return redirect('listarProfessor')
            except:
                pass
    else:
        form = ProfessorForm()
    return render(request, "incluir_professor.html", {'form': form})

def editarProfessor(request, id):
    professor =  Professor.objects.get(id = id)
    form = ProfessorForm(instance=professor)

    if request.method == 'POST':
        form = ProfessorForm(request.POST, instance=professor)
        if form.is_valid():
            try:
                form.save()
                return redirect('listarProfessor')
            except:
                pass

    return render(request, "incluir_professor.html", {'form': form})

def excluirProfessor(request, id):
    professor = Professor.objects.get(id = id)
    try:
        professor.delete()
    except: 
        messages.error(request, "Não é possível excluir!")
    return redirect("listarProfessor")

def listarAlunos(request):
    alunos = Aluno.objects.all().order_by('nome')
    return render(request, "listar_alunos.html", {'lista':alunos})

def incluirAluno(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                return redirect('listarAluno')
            except:
                pass
    else:
        form = AlunoForm()
    return render(request, "incluir_aluno.html", {'form': form})

def editarAluno(request, id):
    aluno =  Aluno.objects.get(id = id)
    form = AlunoForm(instance=aluno)

    if request.method == 'POST':
        form = AlunoForm(request.POST, instance=aluno)
        if form.is_valid():
            try:
                form.save()
                return redirect('listarAluno')
            except:
                pass

    return render(request, "incluir_aluno.html", {'form': form})

def excluirAluno(request, id):
    aluno = Aluno.objects.get(id = id)
    try:
        aluno.delete()
    except: 
        messages.error(request, "Não é possível excluir!")
    return redirect("listarAluno")


