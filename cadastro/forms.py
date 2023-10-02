from django.forms import ModelForm

from cadastro.models import Curso, Turma, Professor, Aluno

class CursoForm(ModelForm):
    class Meta:
        model = Curso
        fields = '__all__'

class ProfessorForm(ModelForm):
    class Meta:
        model = Professor
        fields = '__all__'

class AlunoForm(ModelForm):
    class Meta:
        model = Aluno
        fields = '__all__'