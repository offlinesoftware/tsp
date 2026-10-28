from service.hash_calculator import HashCalculator

def test_hash_256():
    hash_value = "testing"
    result = HashCalculator.hash_sha256(hash_value)
    assert result == "cf80cd8aed482d5d1527d7dc72fceff84e6326592848447d2dc0b0e87dfc9a90"