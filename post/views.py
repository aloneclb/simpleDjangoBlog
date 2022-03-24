from django.shortcuts import get_object_or_404, render, redirect
from django.views import View
from .models import Post, Category, Comment
from django.contrib import messages


# generic views
from django.views.generic import DetailView
from django.views.generic import ListView


class HomeView(View):
    template_name = 'post/home.html'

    def get(self, request):
        context = dict()
        context['posts'] = Post.objects.all()
        context['stand_posts'] = Post.objects.filter(stand = True)[:3] 
        return render(request, self.template_name, context)


class CategoryListView(View):
    template_name = 'post/category-list.html'

    def get(self, request, slug, pk):
        context = dict()
        context['category_name'] = Category.objects.get(slug = slug, pk=pk).name
        context['posts'] = Post.objects.filter(category__slug=slug, category__id=pk)

        return render(request, self.template_name, context)



class PostDetailView(View):
    template_name = 'post/post-detail.html'

    def get(self, request, slug, pk):
        context = dict()
        context['post'] = Post.objects.get(slug = slug, pk=pk)
        context['comments'] = Comment.objects.filter(post__pk=pk, active = True)
        context['comments_count'] = Comment.objects.filter(post__pk=pk, active = True).count()

        return render(request, self.template_name, context)
        

class SearchView(View):
    template_name = 'post/category-list.html'

    def get(self, request):
        context = dict()
        print(request.GET.get('search_value'))
        context['category_name'] = request.GET.get('search_value')
        context['posts'] = Post.objects.filter(body__icontains = str(request.GET.get('search_value')))

        return render(request, self.template_name, context)
    



def comment_add(request,slug,pk):
    if request.method == 'GET':
        post = get_object_or_404(Post, slug=slug, pk=pk)
        try:
            Comment.objects.create(
                post = post,
                name = request.GET.get('message_name'),
                email = request.GET.get('message_email'),
                body = request.GET.get('message_body'),
                active = False
            )
            messages.info(request, 'Mesajınız Gönderildi. Geri Bildiriminiz İçin Teşekkürler...')
        except:
            messages.info(request, 'Mesajınız Gönderilemedi Lütfen Tekrar Deneyiniz...')
            return redirect('post:post_detail', slug, pk)
            # messages.info('Yorumunuz alındı teşekkür ederiz...')

    return redirect('post:post_detail', slug, pk)



def aboutus(request):
    return render(request, 'post/aboutus.html')