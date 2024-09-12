from django.db import models
from datetime import date

# Create your models here.
class MateriaisTabela(models.Model):
    qualidadeproduto = [
        ('B', 'Básica'),
        ('M', 'Média')
        ('O', 'Ótima'),
    ]

    encolhimentoproduto = [
        ('P', 'Pouco'),
        ('M', 'Médio')
        ('B', 'Bastante'),
    ]

    solidezproduto = [
        ('P', 'Pouca'),
        ('M', 'Média')
        ('B', 'Bastante'),
    ]

    peelingproduto = [
        ('P', 'Pouco'),
        ('M', 'Médio')
        ('B', 'Bastante'),
    ]

    id = models.IntegerField(verbose_name="Código", null=False, blank=False)
    nome_material = models.CharField(verbose_name="Nome", max_length=100, null=False, blank=False)
    descricao_material = models.CharField(verbose_name="Descrição", max_length=255, null=True, blank=False)
    qualidade = models.CharField(verbose_name="Qualidade", max_length=1, choices=qualidadeproduto, default='B')
    encolhimento = models.CharField(verbose_name="Encolhimento da peça", null=False, choices=encolhimentoproduto, default='P')
    solidez = models.CharField(verbose_name="Solidez da peça", null=False, choices=solidezproduto, default='P')
    peeling = models.CharField(verbose_name="Peeling da peça", null=False, choices=peelingproduto, default='P')
    # custo = models.ForeignKey(RoupasTabela, on_delete=models.CASCADE)

    def _str_(self):
        return self.nome_material


# class RoupasTabela(models.Model):
#     id = models.IntegerField(verbose_name="Código", max_digits=10, null=False, blank=False)
#     nome_roupa = models.CharField(verbose_name="Nome", max_length=100, null=False, blank=False)
#     descricao_roupa = models.CharField(verbose_name="Descrição", max_length=255, null=True, blank=False)
#     categoria = models.CharField(verbose_name="Categoria", max_length=10, null=False, blank=False)
#     tipo = models.CharField(verbose_name="Tipo", max_length=100, null=False, blank=False)
#     material = models.ForeignKey(MateriaisTabela, on_delete=models.CASCADE)
#     custo = models.DecimalField(verbose_name="Custo", max_digits=10, decimal_places=2, null=True, blank=True)

#     def __str__(self):
#         return self.nome_roupa


    
#Nota:
# 1. Descobir como interligar as duas tabelas;
#   -> nome = models.ForeignKey(NomeTabela, on_delete=models.CASCADE)
#   -> "CASCADE" se refere à: Se eu deletar a tabela, todos os itens dentro dela também são deletados, como uma cascata (considerando que seus itens não podem existir sem uma tabela)
# 2. Criar searchbar;
# 3. Criar filtro;
# 4. Somar "Custo" da tabela MateriaisTabela;