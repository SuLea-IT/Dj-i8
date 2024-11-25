"""
untitled 项目的 URL 配置。

`urlpatterns` 列表将 URL 路由到视图。有关更多信息，请参见：
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
示例：
函数视图：
    1. 添加导入：  from my_app import views
    2. 将 URL 添加到 urlpatterns 列表： path('', views.home, name='home')
基于类的视图：
    1. 添加导入：  from other_app.views import Home
    2. 将 URL 添加到 urlpatterns 列表： path('', Home.as_view(), name='home')
包含其他 URL 配置：
    1. 导入 include() 函数： from django.urls import include, path
    2. 将 URL 添加到 urlpatterns 列表： path('blog/', include('blog.urls'))
"""

from django.contrib import admin  # 导入 Django 管理后台模块
from django.urls import path  # 导入 path 函数，用于定义 URL 路由

urlpatterns = [
    path("admin/", admin.site.urls),  # 管理后台的 URL 路由
]
