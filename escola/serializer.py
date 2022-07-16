from rest_framework import serializers
from escola.models import Aluno, Curso, Matricula

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ['id', 'nome', 'rg' ,'cpf', 'data_nascimento']

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'

class MatriculaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Matricula
        # traz todas as informacoes quando vazio, mas pode utilizar para excluir os campos que não deseja incluir
        exclude = []

class ListaMatriculasAlunoSerializer(serializers.ModelSerializer):

    # exibe o campo do curso pela descricao dele
    curso = serializers.ReadOnlyField(source='curso.descricao')

    #outra forma de exibir pela descricao (busca get_periodo())
    periodo = serializers.SerializerMethodField()
    class Meta:
        model = Matricula
        #filds = ['curso', 'periodo']
        fields = '__all__'

    def get_periodo(self, obj):
        # pega da mesma forma que é exibida no admin
        return obj.get_periodo_display()

class ListaAlunosMatriculadosSerializer(serializers.ModelSerializer):

    aluno_nome = serializers.ReadOnlyField(source='aluno.nome')

    class Meta:
        model = Matricula
        #filds = ['aluno_nome']
        fields = '__all__'