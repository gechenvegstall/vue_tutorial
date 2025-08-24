from django.shortcuts import render,HttpResponse,reverse
from django.http.response import JsonResponse
from django.urls.base import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from .models import Blog,BlogComment,BlogCategory
from .forms import PubBlogForm
from django.db.models import Q


def index(request):
    blogs = Blog.objects.all()
    return render(request, 'index.html', context={"blogs": blogs})

def blog_detail(request,blog_id):
    try:
        blog = Blog.objects.get(pk=blog_id)
    except Exception as e:
        blog = None
    return render(request, 'blog_detail.html', context={'blog': blog})

@require_http_methods(['GET', 'POST'])
@login_required(login_url=reverse_lazy("blog_auth:login"))
def pub_blog(request):
    if request.method == 'GET':
        categories = BlogCategory.objects.all()
        return render(request, 'pub_blog.html', context={"categories": categories})
    else:
        form = PubBlogForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            content = form.cleaned_data.get('content')
            category_id = form.cleaned_data.get('category')
            blog = Blog.objects.create(title=title, content=content, category_id=category_id, author=request.user)
            return JsonResponse({"code": 200, "message": "博客发布成功！", "data": {"blog_id": blog.id}})
        else:
            print(form.errors)
            return JsonResponse({'code': 400, "message": "参数错误！"})
