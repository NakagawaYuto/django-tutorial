from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, View, FormView
from .models import Post
from .forms import PostForm


class HelloView(TemplateView):
    template_name = 'hello.html'


class FrontPageView(View):
    template_name = 'frontpage.html'

    def get(self, request, *args, **kwargs):
        # データベースからすべてのPostオブジェクトを取得
        posts = Post.objects.all()

        # テンプレートにコンテキストを渡してレンダリング
        return render(request, self.template_name, {'posts': posts})


class PostPageView(FormView):
    template_name = 'post.html'
    success_url = '/frontpage/'
    form_class = PostForm

    def form_valid(self, form):
        # フォームのデータが有効な場合の処理
        form.save()
        return super().form_valid(form)
