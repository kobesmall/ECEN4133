#!/usr/bin/python3
# coding: latin-1
blob = """                 >X=Z��f�|+�<R����U:G��I�v��L羛�Ds���+�򹵳.��e���%E~������!������y��W�Xjy��S��YsruP�Ϗ�o��[����������"""
from hashlib import sha256
print(sha256(blob.encode("latin-1")).hexdigest())