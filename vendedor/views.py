from django.shortcuts import render,redirect, get_object_or_404
from django.views.decorators.csrf import csrf_protect
from .models import Vendedor, Cliente
from .forms import VendedorForm, ClienteForm

#--------------FUNÇÕES---------------------
# LISTAR TODOS OS VENDEDORES
def list_all_vendors(request):
    vendedor = Vendedor.objects.all()
    return  render(request, 'index.html', {'vendedor': vendedor})

# LISTAR TODOS OS CLIENTES
def list_all_clients(request):
    clientes = Cliente.objects.all()
    return render(request, 'clients.html', {'clients': clientes}) 

# LISTAR CLIENTES DE UM VENDEDOR 
def list_vendor_clients(request, pk):
    cod_vendedor = pk
    clients = Cliente.objects.filter(cod_vendedor=cod_vendedor)
    vendedor = Vendedor.objects.filter(cod_vendedor=cod_vendedor)
    return render(request, 'clients.html', {'clients': clients, 'vendor': vendedor})

# RENDER TELA DE ADICIONAR VENDEDOR
def register_vendor(request):
    return render(request, 'add_vendor.html')

# REGISTRAR NO BANCO O NOVO VENDEDOR
@csrf_protect
def set_vendor(request):
    cod_vendedor = request.POST.get('cod_vendedor')
    nome = request.POST.get('nome')
    cod_tab = request.POST.get('cod_tab')
    data_nasc = request.POST.get('data_nasc')
    vendedor = Vendedor.objects.create(cod_vendedor=cod_vendedor, nome=nome, cod_tab=cod_tab, data_nasc=data_nasc)
    return redirect('/')

# RENDER TELA DE ADICIONAR CLIENTE
def register_client(request):
    vendedor = Vendedor.objects.all()
    return render(request, 'add_client.html', {'vendedor': vendedor})

# REGISTRAR NO BANCO O NOVO CLIENTE
@csrf_protect
def set_client(request):
    cod_cliente = request.POST.get('cod_cliente')
    nome = request.POST.get('nome')
    tipo = request.POST.get('tipo')
    cod_vendedor = Vendedor.objects.get(cod_vendedor = request.POST.get('cod_vendedor'))
    limite = request.POST.get('limite')
    cliente = Cliente.objects.create(cod_cliente=cod_cliente, nome=nome, tipo=tipo, cod_vendedor=cod_vendedor, limite=limite)
    return redirect('/')

# EDITAR VENDEDOR
def edit_vendor(request, pk):
    cod_vendedor = pk 
    vendedor = get_object_or_404(Vendedor, cod_vendedor= cod_vendedor)
    form = VendedorForm(instance=vendedor)
    return render(request, 'edit_vendor.html', {'form': form, 'cod_vendedor': cod_vendedor })

# REGISTRAR O EDIT DO VENDEDOR NO BANCO
def set_edit_vendor(request, pk):
    vendedor = get_object_or_404(Vendedor, cod_vendedor=pk)
    if request.method == "POST":
        form = VendedorForm(request.POST, instance=vendedor)
        if form.is_valid():
            vendedor = form.save(commit=False)
            vendedor.save()
            return redirect('index')
    else:
        form = VendedorForm(instance=vendedor)
    return rendirect('index')

# EDITAR CLIENTE 
def edit_client(request, pk):
    cod_cliente = pk
    cliente = get_object_or_404(Cliente, cod_cliente=cod_cliente)
    form = ClienteForm(instance=cliente)
    return render(request, 'edit_client.html', {'form': form, 'cod_cliente': cod_cliente })

# REGISTRAR O EDIT DO CLIENTE NO BANCO 
def set_edit_client(request, pk):
    cliente = get_object_or_404(Cliente, cod_cliente=pk)
    if request.method == "POST":
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            cliente = form.save(commit=False)
            cliente.save()
            return redirect('index')
    else:
        form = ClienteForm(instance=cliente)
    return rendirect('index')

# DELETAR VENDEDOR 
def delete_vendor(request, pk):
    vendedor = Vendedor.objects.get(cod_vendedor=pk)
    vendedor.delete()
    return redirect('/')

# DELETAR CLIENTE
def delete_client(request, pk):
    cliente = Cliente.objects.get(cod_cliente=pk)
    cliente.delete()
    return redirect('/')