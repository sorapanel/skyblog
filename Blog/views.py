# ListViewとDetailViewを取り込み
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView

from .models import Post

# ListViewは一覧を簡単に作るためのView
class Index(ListView):
    # 一覧するモデルを指定 -> `object_list`で取得可能
    model = Post
    template_name = 'Blog/post_list.html'

# DetailViewは詳細を簡単に作るためのView
class Detail(DetailView):
    # 詳細表示するモデルを指定 -> `object`で取得可能
    model = Post
    template_name = 'blog/post_detail.html'

class Create(CreateView):
    model = Post
    template_name = 'Blog/post_form.html'
    # 編集対象にするフィールド
    fields = ["title", "body", "category", "tags"]

class Update(UpdateView):
    model = Post
    template_name = 'Blog/post_detail.html'
    fields = ["title", "body", "category", "tags"]

class Delete(DeleteView):
    model = Post
    template_name = 'Blog/post_confirm_delete.html'
    success_url = "/blog/list/"