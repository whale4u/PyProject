#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os

def is_abs(path):
    try:
        abs_header = "/"
        s = os.fspath(path)
        return s.startswith(abs_header)
    except Exception:
        return False


print(is_abs("/xxx/xxx/xxx/../../../etc/passwd"))