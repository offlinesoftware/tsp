import hashlib

class HashCalculator:
    def run_hasher(text, algorithm):
        hasher = hashlib.new(algorithm)
        hasher.update(text.encode())
        return hasher.hexdigest()