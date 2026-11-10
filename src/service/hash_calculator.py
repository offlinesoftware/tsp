import hashlib

class HashCalculator:
    def hash_sha256(text, algorithm):
        hasher = hashlib.new(algorithm)
        hasher.update(text.encode())
        return hasher.hexdigest()