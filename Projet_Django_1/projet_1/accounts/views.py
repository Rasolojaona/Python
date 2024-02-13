from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from .models import *
from .forms import OrderForm


# Create your views here.
def home(request):
    # on récupère tous les commandes
    orders = Order.objects.all()
    # on récupère tous les client
    customers = Customer.objects.all()

    # maintenant nous allons récupérer le total de tous les commandes et les clients
    # total des clients
    total_customers = customers.count()

    # total des commandes
    total_orders = orders.count()

    # le total des commandes delivrés
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    context = {
        'orders': orders, 
        'customers': customers,
        'total_orders': total_orders,
        'total_customers': total_customers,
        'delivered': delivered,
        'pending': pending,
    }

    return render(request, 'accounts/dashboard.html', context)

def customer(request, pk):
    customer = Customer.objects.get(id=pk)
    
    orders = customer.order_set.all()
    total_orders = orders.count()

    context = {
        'customer': customer,
        'orders': orders,
        'total_orders': total_orders
    }

    return render(request, 'accounts/customer.html', context)

def products(request):
    products = Product.objects.all()
    return render(request, 'accounts/products.html', {'products': products})

# create a view called createOrder
def createOrder(request, pk):
    # natao importation ilay inlineformset_factory hi_créer_na multiple form miaraka model parent sy modele child dia autorizer_na hoe iza ny champ ampiasaina
    OrderFormSet = inlineformset_factory(Customer, Order, fields=('product', 'status'), extra=10)

    customer = Customer.objects.get(id=pk)
    # raha tia tsika hoe champ tsisy an'ilay produit efa misy dia manao querySet
    formset = OrderFormSet(queryset=Order.objects.none(), instance=customer)
    # we pass the instance of customer
    # form = OrderForm(initial={'customer':customer})
    if request.method == 'POST':
        # print('Printing post: ', request.POST)
        # form = OrderForm(request.POST)
        # ovaine formset ilay form tsotra
        # passer_na ilay request.POST
        formset = OrderFormSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('home')

    context = {'formset' : formset}
    return render(request, 'accounts/order_form.html', context)

# update method
def updateOrder(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        # precise that we want the instance of order not an new object
        # miteny tsika hoe tiko passer_na ao anatin'ilay instance=order nalaiko ity le izy fa tsy mi_creer vao2
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('home')
        
    context = {'form':form}
    return render(request, 'accounts/order_form.html', context)

# delete logic et passer la clé primaire pour spécifier l'order à supprimer
def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('home')

    context = {'item':order}

    return render(request, 'accounts/delete.html', context)