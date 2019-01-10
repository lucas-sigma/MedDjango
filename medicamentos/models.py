from django.db import models

class Categoria(models.Model):
    categoria = models.CharField(max_length=50)

class Medicamento(models.Model):
    medicamento           = models.CharField(max_length=50)
    para_que_serve        = models.TextField()
    contraindicacao       = models.TextField()
    como_usar             = models.TextField()
    precaucoes            = models.TextField()
    reacoes_adversas      = models.TextField()
    riscos                = models.TextField()
    interacao_med         = models.TextField()
    interacao_alimenticia = models.TextField()
    acao_da_substancia    = models.TextField()
    #categoria

    def __str__(self):
        return self.medicamento