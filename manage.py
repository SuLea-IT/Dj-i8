#!/usr/bin/env python
"""Django 的命令行工具，用于执行管理任务。"""
import os
import sys


def main():
    """执行管理任务。"""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Dj-i8.settings")  # 设置默认的 Django 配置模块
    try:
        from django.core.management import execute_from_command_line  # 从 Django 导入命令行管理工具
    except ImportError as exc:
        raise ImportError(
            "无法导入 Django。你确定它已安装并且 "
            "在你的 PYTHONPATH 环境变量中吗？你是否 "
            "忘记激活虚拟环境？"
        ) from exc  # 如果导入失败，抛出异常并给出提示
    execute_from_command_line(sys.argv)  # 执行命令行任务


if __name__ == "__main__":
    main()  # 运行管理任务
