import timeit

factor_a = 16807
factor_b = 48271
divisor = 2147483647


def calc_a():
    matches = 0
    for run in range(0, 40_000_000):
        gen_a = (factor_a * 591) % divisor
        gen_b = (factor_b * 591) % divisor

        bin_a = format(gen_a, 'b').zfill(16)
        bin_b = format(gen_b, 'b').zfill(16)

        if bin_a[len(bin_a) - 16:len(bin_a)] == bin_b[len(bin_b) - 16:len(bin_b)]:
            matches += 1

    print(matches)


def calc_b():
    gen_a = 591
    gen_b = 393
    matches = 0
    for run in range(0, 5_000_000):
        while True:
            gen_a = (factor_a * gen_a) % divisor
            if gen_a % 4 == 0:
                break

        while True:
            gen_b = (factor_b * gen_b) % divisor
            if gen_b % 8 == 0:
                break

        bin_a = format(gen_a, 'b').zfill(16)
        bin_b = format(gen_b, 'b').zfill(16)

        if bin_a[len(bin_a) - 16:len(bin_a)] == bin_b[len(bin_b) - 16:len(bin_b)]:
            matches += 1
    return matches


start = timeit.default_timer()

print(calc_b())

stop = timeit.default_timer()

print(stop - start)
