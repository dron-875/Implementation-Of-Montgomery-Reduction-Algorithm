class Barrett:
    BASE = 2

    def __init__(self, m):
        self.m = m
        self.n = m.bit_length()
        # Calculate Barrett constant
        self.k = (1 << (2 * self.n)) // m

    # Reduction method
    def reduce(self, t):
        q = (t * self.k) >> (2 * self.n)
        a = t - q * self.m
        if a < 0:
            a += self.m
        return a

# Modulus m and two operands x1 and x2 for modular exponentiation operation ((x1^x2) % m)
m = 750791094644726559640638407699
x1 = 540019781128412936473322405310
x2 = 515692107665463680305819378593

# Instantiating Barrett Reduction and Performing Reduction:
barrett = Barrett(m)
t1 = x1 * Barrett.BASE
t2 = x2 * Barrett.BASE

r1 = barrett.reduce(t1)
r2 = barrett.reduce(t2)
r = 1 << barrett.n

# Printing Information:
print("b:", Barrett.BASE)
print("n:", barrett.n)
print("m:", barrett.m)
print("t1:", t1)
print("t2:", t2)
print("r1:", r1)
print("r2:", r2)
print("")
print("Original x1       :", x1)
print("Recovered from r1 :", barrett.reduce(r1))
print("Original x2       :", x2)
print("Recovered from r2 :", barrett.reduce(r2))

# Checking Barrett constant
print("k:", barrett.k)

# Exponentiation and Result Verification:
prod = barrett.reduce(Barrett.BASE)
base = barrett.reduce(x1 * Barrett.BASE)
exp = x2

while exp.bit_length() > 0:
    if (exp & 1) == 1:
        prod = barrett.reduce(prod * base)
    exp >>= 1
    base = barrett.reduce(base * base)

print("\nBarrett exponentiation:", prod)

