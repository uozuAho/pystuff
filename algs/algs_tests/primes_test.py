from algs.primes import prime_factors, primes, is_prime


def test_prime_factors():
    assert prime_factors(630085147213) == [17, 2243, 16524223]


def test_primes():
    assert list(primes(10)) == [2, 3, 5, 7]


def test_is_prime():
    assert all(is_prime(x) for x in primes(20))
