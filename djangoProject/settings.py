from pathlib import Path
import os

# 获取当前文件的绝对路径，然后解析其父目录的父目录，即项目的根目录。
BASE_DIR = Path(__file__).resolve().parent.parent

# Django 快速开发设置，不适用于生产环境。
# 有关详细信息，请参阅 Django 文档：https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# 安全警告：在生产环境中必须保持秘密的密钥。
SECRET_KEY = 'django-insecure-h$t%&qp2to$^wgunjnuzoift(rv6@)8ei5%)j6m-$t6sgqfd+='

# 安全警告：在生产环境中不应运行调试模式。
DEBUG = True

# 允许访问该 Django 项目的主机/域名列表。
ALLOWED_HOSTS = []

# 应用程序定义，列出项目中安装的所有 Django 应用。
INSTALLED_APPS = [
    'django.contrib.admin',  # Django 的管理后台应用
    'django.contrib.auth',  # Django 的认证系统应用
    'django.contrib.contenttypes',  # Django 的内容类型框架
    'django.contrib.sessions',  # Django 的会话框架
    'django.contrib.messages',  # Django 的消息传递框架
    'django.contrib.staticfiles',  # Django 的静态文件处理应用
    'forum',  # 用户自定义的论坛应用
    'userapp',  # 用户自定义的用户应用
]

# Django 中间件配置，定义请求/响应处理的钩子。
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',  # 管理安全相关的中间件
    'django.contrib.sessions.middleware.SessionMiddleware',  # 管理会话的中间件
    'django.middleware.common.CommonMiddleware',  # 处理常见任务的中间件
    'django.middleware.csrf.CsrfViewMiddleware',  # 提供跨站请求伪造保护的中间件
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # 处理用户认证的中间件
    'django.contrib.messages.middleware.MessageMiddleware',  # 处理消息传递的中间件
    'django.middleware.clickjacking.XFrameOptionsMiddleware',  # 防止点击劫持的中间件
]

# 根 URL 配置，指向项目的 URL 配置模块。
ROOT_URLCONF = 'djangoProject.urls'

# 模板配置，定义 Django 如何加载和渲染模板。
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',  # 使用 Django 的模板引擎
        'DIRS': [BASE_DIR / 'templates'],  # 指定模板文件存放的目录
        'APP_DIRS': True,  # 允许 Django 在每个应用的 templates 子目录中查找模板
        'OPTIONS': {
            # 定义模板上下文处理器，添加额外的上下文变量到模板中。
            'context_processors': [
                'django.template.context_processors.debug',  # 添加调试相关的上下文
                'django.template.context_processors.request',  # 添加请求对象到模板上下文
                'django.contrib.auth.context_processors.auth',  # 添加用户认证相关的上下文
                'django.contrib.messages.context_processors.messages',  # 添加消息框架的上下文
            ],
        },
    },
]

# WSGI 应用配置，指向 Django 项目的 WSGI 入口点。
WSGI_APPLICATION = 'djangoProject.wsgi.application'

# 数据库配置，定义如何连接到数据库。
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',   # 使用 MySQL 数据库引擎
        'NAME': 'forum',                         # 数据库名
        'USER': 'root',                         # 数据库用户名
        'PASSWORD': '123456',                # 数据库密码
        'HOST': '127.0.0.1',                    # 数据库服务器地址
        'PORT': '3306',                         # 数据库服务器端口
    }
}

# 密码验证器配置，定义密码强度验证规则。
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# 国际化配置。
LANGUAGE_CODE = 'en-us'  # 网站的默认语言代码，这里设为英语（美国）。

TIME_ZONE = 'Asia/Shanghai'  # 网站的默认时区，这里设为亚洲/上海时区。

USE_I18N = True  # 启用 Django 的国际化功能。

USE_TZ = True  # 启用时区支持。

# 静态文件配置，定义静态文件（如 CSS、JavaScript）的服务方式。
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'forum' / 'static'  # 静态文件的存放路径
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  # 媒体文件的存放路径
MEDIA_URL = '/media/'  # 媒体文件的 URL 前缀

# 默认的主键字段类型，用于模型中未指定主键时。
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# 用户模型配置，指定自定义的用户模型。
AUTH_USER_MODEL = 'userapp.CustomUser'  # 使用 userapp 应用中的 CustomUser 模型作为用户模型
