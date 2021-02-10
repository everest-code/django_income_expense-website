from django.shortcuts import render
from .models import Item

# Create your views here.

def  index(request):
    items = Item.objects.all()
    item_no = Item.objects.count()
    context = {'items':items, 'item_no':item_no}
    return render(request, 'expenses/index.html', context)

def add_expense(request):
    return render(request, 'expenses/add_expense.html')