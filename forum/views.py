from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.contrib.auth.decorators import user_passes_test
from django.core.paginator import Paginator
# Create your views here.


def post_list(request):
    request.session['last_view'] = 'post_list'
    # 获取所有的帖子
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')

    # 创建一个Paginator对象，每页显示5个帖子
    paginator = Paginator(posts, 5)

    # 获取请求中的页码参数，默认为1
    page_number = request.GET.get('page')

    # 获取特定页的帖子
    page = paginator.get_page(page_number)

    # 判断是否没有帖子
    no_posts = not page.object_list.exists()

    # 计算总页数减一的值
    num_pages_minus_one = paginator.num_pages - 1

    # 将所有需要的变量传递给模板
    return render(request, 'forum/post_list.html', {
        'page': page,
        'no_posts': no_posts,
        'num_pages_minus_one': num_pages_minus_one
    })


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'forum/post_detail.html', {'post': post})


def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'forum/post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'forum/post_edit.html', {'form': form})


def post_draft_list(request):
    request.session['last_view'] = 'post_draft_list'
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'forum/post_draft_list.html', {'posts': posts})


def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)


def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    last_view = request.session.get('last_view')
    if last_view == 'post_draft_list':
        return redirect('post_draft_list')
    else:
        return redirect('post_list')


def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'forum/add_comment_to_post.html', {'form': form})


@user_passes_test(lambda user: user.is_superuser)
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)


def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('post_detail', pk=comment.post.pk)
