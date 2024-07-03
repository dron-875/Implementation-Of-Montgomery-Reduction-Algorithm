# importing time module
import time

# calc is the function to determine the computational time
def calc(z):
    return z ** 2

# tracks the start time
st = time.perf_counter()

# calling the function

class Montgomery:
    BASE = 2

# Calculating rrm
    def __init__(self, m):
        self.m = m
        self.n = m.bit_length()
        self.rrm = (1 << (self.n * 2)) % m
# .rrm is = 1 is left shifted by 2n then modulo m
# hence .rrm = (1* 2 to power 2n)  % m

# Reduce method
    def reduce(self, t):
        a = t
        for i in range(self.n):
            if (a & 1) == 1:
                a = a + self.m
            a = a >> 1
        if a >= self.m:
            a = a - self.m
        return a

# These are the modulus m and two operands x1 and x2 for the modular exponentiation operation ((x1^x2) % m)
m =  75079109464472655964063840763895
x1 = 54001978112841293647332240533245
x2 = 51569210766546368030581937854555

# Instantiating Montgomery and Performing Reduction:
mont = Montgomery(m)
t1 = x1 * mont.rrm
t2 = x2 * mont.rrm


# r1 & r2 are reduced form of t1 & t2.
r1 = mont.reduce(t1)
r2 = mont.reduce(t2)
r = 1 << mont.n
#mont.n is the number of bits in binary form of m

#Printing Information:
print ("b : ", Montgomery.BASE)
print ("n : ", mont.n)
print ("r : ", r)
print ("m : ", mont.m)
print("mont.rrm:",mont.rrm);
print ("t1: ", t1)
print ("t2: ", t2)
print ("r1: ", r1)
print ("r2: ", r2)
print("")
print ("Original x1       :", x1)
print ("Recovered from r1 :", mont.reduce(r1))
print ("Original x2       :", x2)
print ("Recovered from r2 :", mont.reduce(r2))

print ("\nMontgomery computation of x1 ^ x2 mod m:")
print("")
prod = mont.reduce(mont.rrm)
base = mont.reduce(x1 * mont.rrm)
exp = x2
# Checking initialized values
print("precomputed-prod",prod)
print("precomputed-base",base)
print("precomputed-exp",exp)

# Exponentiation and Result Verification:
while exp.bit_length() > 0:
    if (exp & 1) == 1:
        prod = mont.reduce(prod * base)
    exp = exp >> 1
    base = mont.reduce(base * base)
print ("\nMontgomery exponentiation:",mont.reduce(prod))

# Alternate method for computation of x1 ^ x2 mod m :
print ("\nAlternate computation of x1 ^ x2 mod m :",pow(x1, x2, m))

# tracks the end time
e = time.perf_counter()

# find elapsed time in seconds
ms = (e - st) * 10 ** 6
# print(f"Computational time {ms:.03f}microsecs.")