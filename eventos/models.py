from django.db import models
from django.contrib.auth.models import User 
 
class Pessoa(models.Model):
    nome = models.CharField(max_length=128)
    email = models.TextField()
    
    def __str__(self):
        return self.nome

class PessoaFisica (Pessoa):
    cpf = models.CharField(max_length=20)
    
    class Meta ():
        verbose_name = 'Pessoa Física'
        verbose_name_plural = 'Pessoas Físicas'

class PessoaJuridica (Pessoa):
    cnpj = models.CharField(max_length=20)
    razaoSocial = models.TextField()

class Autor (Pessoa):
    curriculo = models.TextField()
    artigos = [].models.ForeignKey(Artigo, related_name='Artigos',null=True, blank=False) 

class Evento(models.Model):
    nome = models.CharField(max_length=128)
    eventoPrincipal = models.CharField(max_length=128)
    sigla = models.CharField(max_length=8)
    dataHoraInicio = models.DateTimeField()
    palavraChave = models.TextField()
    logotipo = models.TextField()
    realizador = models.ForeignKey(PessoaFisica, related_name='pessoasFisicas',null=True, blank=False)
    cidade = models.CharField(max_length=128)
    uf = models.CharField(max_length=128)
    endereco = models.CharField(max_length=128)
    cep = models.CharField(max_length=8)

class EventoCientifico (Evento):
    issn = models.TextField()

class ArtigoCientifico (models.Model):
    titulo = models.TextField()
    autores = [].models.ForeignKey(Artigo, related_name='autores',null=True, blank=False)
    evento = models.ForeignKey(EventoCientifico, related_name='eventosCientificos',null=True, blank=False)


    
