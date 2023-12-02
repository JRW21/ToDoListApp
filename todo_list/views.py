from django.shortcuts import render, redirect
from .models import List #needed to pull in database
from .forms import ListForm 
from django.contrib import messages # djangos ready to go messaging system 
from django.http import HttpResponseRedirect #allows redirection. need this to use redirect
# Create your views here.

def home(request):
    
    if request.method == 'POST':
        form = ListForm(request.POST or None)
        
        if form.is_valid():
            form.save()
            all_items = List.objects.all#This is a query
            messages.success(request, ('Item has been added to list!'))
            return render(request, "home.html",{'all_items':all_items,"form_stuff":form})
    else:
        all_items = List.objects.all#This is a query
        return render(request, "home.html",{'all_items':all_items})

def about(request):
    my_name="Jabari"
    last_name="Washington"
    context = {'first_name':my_name,'last_name':{'name':last_name}}
    return render(request, "about.html",context)# things in the {} can be passed into the HTML page

def delete(request, list_id):
    item = List.objects.get(pk=list_id)
    item.delete()
    messages.success(request, ('Item has been Deleted!'))
    return redirect('home')

def cross_off(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed=True
    item.save()
    messages.success(request, ('Item has been crossed off!'))
    return redirect('home')

def uncross(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed=False
    item.save()
    messages.success(request, ('Item has been uncrossed!'))
    return redirect('home')

def edit(request, list_id):
    if request.method == 'POST':
        item = List.objects.get(pk=list_id)
        form = ListForm(request.POST or None, instance = item)
        
        if form.is_valid():
            form.save()
            all_items = List.objects.all#This is a query
            messages.success(request, ('Item has been edited!'))
            return redirect('home')
    else:
        item = List.objects.get(pk=list_id)#This is a query
        return render(request, "edit.html",{'item':item})