import hashlib
import re
# Hash functions for different algorithms
def md5_hash(string):
    return hashlib.md5(string.encode('utf-8')).hexdigest()

def sha1_hash(string):
    return hashlib.sha1(string.encode('utf-8')).hexdigest()

def sha224_hash(string):
    return hashlib.sha224(string.encode('utf-8')).hexdigest()

def sha256_hash(string):
    return hashlib.sha256(string.encode('utf-8')).hexdigest()

def sha384_hash(string):
    return hashlib.sha384(string.encode('utf-8')).hexdigest()

def sha512_hash(string):
    return hashlib.sha512(string.encode('utf-8')).hexdigest()

# Function to determine the algorithm based on the hash length
def ret_algo(hash):
    if hash is None:
        return None
    check =  bool(re.match(r'^[a-fA-F0-9]+$', hash))
    if not check:
        return "unknown"
   
    hash_lengths = {
    "md5": 32,
    "sha1": 40,
    "sha224": 56,
    "sha256": 64,
    "sha384": 96,
    "sha512": 128
    }
    for algo, length in hash_lengths.items():
        if len(hash) == length:
            return algo
            
    return "unknown"
