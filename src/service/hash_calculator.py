import hashlib

class HashCalculator:
    def hash_sha256(text):
        return hashlib.sha256(text.encode()).hexdigest()