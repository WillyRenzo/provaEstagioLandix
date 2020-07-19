from django.db import models

#Objeto - Vendedor

class Vendedor(models.Model):
    cod_vendedor = models.AutoField(primary_key=True, unique=True)
    nome = models.CharField(max_length=50)
    cod_tab = models.IntegerField()
    data_nasc = models.DateField()

    def __str__(self):
        return str(self.cod_vendedor)

#Objeto - Cliente

class Cliente(models.Model):
    #Tipos de campo - tipo
    TYPES = (
        ('PF', 'Pessoa Física'),
        ('PJ', 'Pessoa Jurídica'),
    )
    cod_cliente = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)
    tipo = models.CharField(max_length=2, choices=TYPES, default='PF')
    cod_vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE) #Foreign Key p/ tabela Vendedor, caso algum vendedor for deletado, automaticamente todos os produtos relacionados a ele também são.
    limite = models.DecimalField(max_digits=17, decimal_places=2)

    def __str__(self):
        return str(self.cod_cliente)