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
    success_url = reverse_lazy('app:post_list')


class TagCreate(generic.CreateView):
    model = Tag
    fields = '__all__'
    success_url = reverse_lazy('app:post_list')


class PopupCategoryCreate(CategoryCreate):
    model = Category
    fields = '__all__'

    def form_valid(self, form):
        category = form.save()
        context = {
            'object_name': str(category),
            'object_pk': category.pk,
            'function_name': 'add_category'
        }
        return render(self.request, 'app/close.html', context)


class PopupTagCreate(TagCreate):
    model = Tag
    fields = '__all__'

    def form_valid(self, form):
        tag = form.save()
        context = {
            'object_name': str(tag),
            'object_pk': tag.pk,
            'function_name': 'add_tag'
        }
        return render(self.request, 'app/close.html', context)