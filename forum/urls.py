# 从Django导入path和views模块
from django.urls import path
from . import views

# 定义URL模式
urlpatterns = [
    path('', views.post_list, name='post_list'),  # 空路径对应视图post_list，命名为'post_list'
    path('post/<int:pk>/', views.post_detail, name='post_detail'),  # 匹配'post/<数字>/'路径，对应视图post_detail，命名为'post_detail'
    path('post/new/', views.post_new, name='post_new'),  # 匹配'post/new/'路径，对应视图post_new，命名为'post_new'
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),  # 匹配'post/<数字>/edit/'路径，对应视图post_edit# ，命名为'post_edit'
    path('drafts/', views.post_draft_list, name='post_draft_list'),  # 匹配'drafts/'路径，对应视图post_draft_list，命名为'post_draft_list'
    path('post/<pk>/publish/', views.post_publish, name='post_publish'),  # 匹配'post/<数字>/publish/'路径，对应视图post_publish，命名为'post_publish'
    path('post/<pk>/remove/', views.post_remove, name='post_remove'),  # 匹配'post/<数字>/remove/'路径，对应视图post_remove，命名为'post_remove'
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),  # 匹配'post/<数字>/comment/'路径，对应视图add_comment_to_post，命名为'add_comment_to_post'
    path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),  # 匹配'comment/<数字>/approve/'路径，对应视图comment_approve，命名为'comment_approve'
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),  # 匹配'comment/<数字>/remove/'路径，对应视图comment_remove，命名为'comment_remove'
]
