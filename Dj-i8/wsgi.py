"""
WSGI 配置文件，用于 untitled 项目。

它将 WSGI 可调用对象暴露为一个名为 `application` 的模块级变量。

有关此文件的更多信息，请参见：
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# 设置默认的 Django 配置模块
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Dj-i8.settings")

# 获取 WSGI 应用程序
application = get_wsgi_application()
