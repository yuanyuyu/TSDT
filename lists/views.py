from django.shortcuts import render, redirect
from django.http import HttpResponse
from lists.models import Item, List

def new_list(request):
	list_user = List.objects.create()
	Item.objects.create(text=request.POST['item_text'], list=list_user) 
	return redirect(f'/lists/{list_user.id}/')

def home_page(request):
	return render(request, 'home.html')

def view_list(request, list_id):
	list_user = List.objects.get(id=list_id)
	return render(request, 'list.html', {'list': list_user})

def add_item(request, list_id):
	list_user = List.objects.get(id=list_id)
	Item.objects.create(text=request.POST['item_text'], list=list_user)
	return redirect(f'/lists/{list_user.id}/')


# Create your views here.
