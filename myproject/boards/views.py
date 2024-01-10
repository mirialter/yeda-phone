from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView
# Create your views here.
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

# from .models import Category

def home(request):
    return HttpResponse('Hello, World!')

# def display_table(request):
#     data = קטגוריות.objects.all()
#     return render(request, 'boards/category_list.html', {'data': data})

# class CategoryList(ListView):
#     model = Category

# class CategoryDetail(DetailView):
#     model = Category  

# def CategoryView(request):
    # model = Category
    # Field must be same as the model attribute
    # objs = Category.objects.all()
    # def objs
    # fields = ['name', 'identityNumber']  
    # return render(request, 'category_list.html', {'objs':{}})       