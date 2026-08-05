#!/usr/bin/env python
import os
import sys

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

try:
    from django.core.management import execute_from_command_line
except ImportError as e:
    raise ImportError(
        "No module named 'django.core.management'"
    ) from e

execute_from_command_line(sys.argv)