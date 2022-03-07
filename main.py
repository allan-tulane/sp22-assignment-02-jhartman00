import time

import tabulate as tabulate


class BinaryNumber:
    """ done """

    def __init__(self, n):
        self.decimal_val = n
        self.binary_vec = list('{0:b}'.format(n))

    def __repr__(self):
        return 'decimal=%d binary=%s' % (self.decimal_val, ''.join(
            self.binary_vec))

    def __add__(self, other):
        return BinaryNumber(self.decimal_val + other.decimal_val)

    def __mul__(self, other):
        return BinaryNumber(self.decimal_val * other.decimal_val)

    def __sub__(self, other):
        return BinaryNumber(self.decimal_val - other.decimal_val)


## Implement multiplication functions here. Note that you will have to
## ensure that x, y are appropriately sized binary vectors for a
## divide and conquer approach.
def binary2int(binary_vec):
    if len(binary_vec) == 0:
        return BinaryNumber(0)
    return BinaryNumber(int(''.join(binary_vec), 2))


def split_number(vec):
    return binary2int(vec[:len(vec) // 2]), binary2int(vec[len(vec) // 2:])


def bit_shift(number, n):
    # append n 0s to this number's binary string
    return binary2int(number.binary_vec + ['0'] * n)


def pad(x, y):
    # pad with leading 0 if x/y have different number of bits
    # e.g., [1,0] vs [1]
    if len(x) < len(y):
        x = ['0'] * (len(y) - len(x)) + x
    elif len(y) < len(x):
        y = ['0'] * (len(x) - len(y)) + y
    # pad with leading 0 if not even number of bits
    if len(x) % 2 != 0:
        x = ['0'] + x
        y = ['0'] + y
    return x, y


def subquadratic_multiply(x, y):
    xvec = x.binary_vec
    yvec = y.binary_vec

    if x.decimal_val <= 1 and y.decimal_val <= 1:
        return x * y

    xvec, yvec = pad(xvec, yvec)

    xL, xR = split_number(xvec)
    yL, yR = split_number(yvec)

    left = subquadratic_multiply(xL, yL)
    right = subquadratic_multiply(xR, yR)
    mid = subquadratic_multiply(xL, yR) + subquadratic_multiply(
        xR, yL)
    mid = bit_shift(mid, len(xvec) // 2)
    left = bit_shift(left, len(xvec))

    return left + right + mid


def test_multiply():
    print("2x2:")
    print(subquadratic_multiply(BinaryNumber(2), BinaryNumber(2)))
    print("4*4:")
    print(subquadratic_multiply(BinaryNumber(4), BinaryNumber(4)))
    print("5*9")
    print(subquadratic_multiply(BinaryNumber(5), BinaryNumber(9)))


def time_multiply(x, y, f):
    start = time.time()
    print("running timer:")
    x = f(x, y)
    return (time.time() - start) * 1000


# Bellow functions imported from recitations 2 and 3 for testing purposes

"""Below functions imported from recitation 2 for testing purposes"""


def compare_time(num_sets):
    result = []
    for x, y in num_sets:
        curr_nums = "X: {} Y: {}".format(x.decimal_val, y.decimal_val)
        time = "Time in ms: {}".format(time_multiply(x, y, subquadratic_multiply))
        result.append((
            curr_nums,
            # subquadratic_multiply(x, y),
            time
        ))
    return result


def print_results(results):
    """ done """
    print(tabulate.tabulate(results,
                            headers=['nums', 'sub quadratic', 'sub quadratic time'],
                            floatfmt=".10f",
                            tablefmt="github"))


if __name__ == "__main__":
    num_sets = [(BinaryNumber(5), BinaryNumber(5)), (BinaryNumber(25), BinaryNumber(25)),
                (BinaryNumber(125), BinaryNumber(125)), (BinaryNumber(625), BinaryNumber(625)),
                (BinaryNumber(3125), BinaryNumber(3125)), (BinaryNumber(15625), BinaryNumber(15625)),
                (BinaryNumber(78125), BinaryNumber(78125)), (BinaryNumber(390625), BinaryNumber(390625)),
                (BinaryNumber(1953125), BinaryNumber(1953125)),  (BinaryNumber(9765625), BinaryNumber(9765625)),
                (BinaryNumber(48828125), BinaryNumber(48828125)), (BinaryNumber(244140625), BinaryNumber(244140625))]
    print_results(compare_time(num_sets))