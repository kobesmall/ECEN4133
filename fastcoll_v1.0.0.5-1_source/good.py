#!/usr/bin/python3
# coding: latin-1
blob = """                 �;�
�9��&"̶�X�.d�(/��m6D6),��$���H�S���T����6͆�����ǵ!I_V����#�q ���[����A�z.��-�Nl�����K�Y�R~�I��D����m˃*iު�1
N"""
from hashlib import sha256
if(sha256(blob.encode("latin-1")).hexdigest() == "d59d582e15bb45e5331d3766825d6fc5ea79f76f92c7eda8dfdf1c4eb6ca88c5"):
    print("Use SHA-256 instead!")
elif(sha256(blob.encode("latin-1")).hexdigest() ==
"953249d1412866d6f764397480386d0d26ba60a496760faa72feba45400c263e"):
	print("MD5 is perfectly secure!")