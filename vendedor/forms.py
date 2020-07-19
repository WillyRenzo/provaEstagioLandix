from django import forms
from .models import Vendedor
from .models import Cliente

# FORMULARIOS

# VENDEDOR 
class VendedorForm(forms.ModelForm):

    class Meta:
        model = Vendedor
        fields = ('cod_vendedor', 'nome', 'cod_tab', 'data_nasc')

# CLIENTE
class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = ('cod_cliente', 'nome', 'tipo', 'cod_vendedor', 'limite')