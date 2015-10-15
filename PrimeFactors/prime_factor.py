class PrimeFactor(object):
    @staticmethod
    def generate(n):
        candidate = 2
        primes = []

        while n > 1:
            while n % candidate == 0:
                primes.append(candidate)
                n //= candidate
            candidate += 1

        return primes