"""
Django 设置文件，用于 "untitled" 项目。

由 'django-admin startproject' 创建，使用 Django 4.2.16。

有关此文件的更多信息，请参见：
https://docs.djangoproject.com/en/4.2/topics/settings/

完整的设置列表及其值，请参见：
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
from pathlib import Path

# 在项目中构建路径，类似 BASE_DIR / '子目录'
BASE_DIR = Path(__file__).resolve().parent.parent


# 快速开始开发设置 - 不适合生产环境
# 请参见 https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# 安全警告：在生产环境中，请保持 secret key 的保密！
SECRET_KEY = "django-insecure-p(v24^1gq2ef%snntp0c(3f37c7aym2e%x&$ty@lp_az-=gf3f"

# 安全警告：在生产环境中，请不要开启调试模式！
DEBUG = True

ALLOWED_HOSTS = []  # 允许访问的主机列表


# 应用程序定义

INSTALLED_APPS = [
    "django.contrib.admin",  # 管理后台应用
    "django.contrib.auth",  # 身份认证应用
    "django.contrib.contenttypes",  # 内容类型应用
    "django.contrib.sessions",  # 会话管理应用
    "django.contrib.messages",  # 消息框架应用
    "django.contrib.staticfiles",  # 静态文件处理应用
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",  # 安全中间件
    "django.contrib.sessions.middleware.SessionMiddleware",  # 会话中间件
    "django.middleware.common.CommonMiddleware",  # 常规中间件
    "django.middleware.csrf.CsrfViewMiddleware",  # CSRF 防护中间件
    "django.contrib.auth.middleware.AuthenticationMiddleware",  # 身份验证中间件
    "django.contrib.messages.middleware.MessageMiddleware",  # 消息中间件
    "django.middleware.clickjacking.XFrameOptionsMiddleware",  # 点击劫持防护中间件
]

ROOT_URLCONF = "Dj-i8.urls"  # 项目的 URL 配置

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",  # 使用 Django 的模板引擎
        "DIRS": [os.path.join(BASE_DIR, 'templates')],  # 模板文件的目录
        "APP_DIRS": True,  # 是否启用应用目录中的模板
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",  # 调试信息
                "django.template.context_processors.request",  # 请求信息
                "django.contrib.auth.context_processors.auth",  # 身份验证信息
                "django.contrib.messages.context_processors.messages",  # 消息框架信息
            ],
        },
    },
]

WSGI_APPLICATION = "Dj-i8.wsgi.application"  # WSGI 应用

# 数据库设置
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",  # 使用 SQLite 数据库
        "NAME": BASE_DIR / "db.sqlite3",  # 数据库文件的路径
    }
}

# 密码验证
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",  # 用户属性相似度验证器
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",  # 密码最小长度验证器
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",  # 常见密码验证器
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",  # 数字密码验证器
    },
]

# 国际化设置
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"  # 语言代码

TIME_ZONE = "UTC"  # 时区

USE_I18N = True  # 启用国际化

USE_TZ = True  # 启用时区支持


# 静态文件（CSS、JavaScript、图片）
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"  # 静态文件的 URL 路径

# 默认的主键字段类型
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"  # 使用大整数自增主键
