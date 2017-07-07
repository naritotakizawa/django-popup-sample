from django.views import generic
from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Post, Category, Tag


class PostList(generic.ListView):
    model = Post


class PostCreate(generic.CreateView):
    model = Post
    fields = '__all__'
    success_url = reverse_lazy('app:post_list')


class CategoryCreate(generic.CreateView):
    model = Category
    fields = '__all__'

    def form_valid(self, form):
        form.save()
        return render(self.request, 'app/close.html')


class TagCreate(generic.CreateView):
    model = Tag
    fields = '__all__'

    def form_valid(self, form):
        form.save()
        return render(self.request, 'app/close.html')