#!/usr/bin/python3
# coding: latin-1
blob = """                 >X=Z��f�|+�<R���UU:G��I�v��L羛�Ds����+�򹵳.�����%E~������!�����y��W�Xjy��S��YsruP�ϏFo��[���������"""
from hashlib import sha256
print(sha256(blob.encode("latin-1")).hexdigest())