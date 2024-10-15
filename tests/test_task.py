from src.bdmle_cicd_hw.task import is_prime, get_primes, get_primes_fast, primes, checksum, pipeline

def test_is_prime():
    assert is_prime(0) == False
    assert is_prime(1) == False
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(4) == False
    assert is_prime(5) == True
    assert is_prime(9) == False
    assert is_prime(29) == True

def test_get_primes():
    assert get_primes(1, 10) == [2, 3, 5, 7]
    assert get_primes(10, 20) == [11, 13, 17, 19]
    assert get_primes(0, 5) == [2, 3, 5]

def test_get_primes_fast():
    assert len(get_primes_fast(2, 3)) == 2

def test_primes():
    assert primes(5) == [2, 3, 5, 7, 11]
    assert len(primes(5)) == 5
    assert primes(10) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    assert len(primes(10)) == 10
    assert len(primes(1000)) == 1000

def test_checksum():
    assert checksum([1, 2, 3]) == 380
    assert checksum([]) == 0

def test_pipeline():
    assert pipeline() == 7785816

if __name__ == "__main__":
    test_is_prime()
    test_get_primes()
    test_get_primes_fast()
    test_primes()
    test_checksum()
    test_pipeline()
    print("All tests passed!")