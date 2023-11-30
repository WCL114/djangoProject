"""
URL configuration for djangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views
from django.conf import settings
from django.conf.urls.static import static

# 定义URL模式
urlpatterns = [
    path('admin/', admin.site.urls),  # Django管理面板的URL
    path('accounts/logout/', views.LogoutView.as_view(next_page='/'), name='logout'),  # 用户注销的URL
    path('', include('forum.urls')),  # 包含'forum'应用的URL
    path('user/', include('userapp.urls')),  # 包含'userapp'应用的URL
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # 在开发模式下提供媒体文件服务
