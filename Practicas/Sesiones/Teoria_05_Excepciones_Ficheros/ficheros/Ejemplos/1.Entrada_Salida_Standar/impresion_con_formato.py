# Fancier Output Formatting¶
# The type can be used with format codes:
# 'd' for integers.
# 'f' for floating-point numbers.
# 'b' for binary numbers.
# 's' for string.
# 'e' for floating-point in an exponent format.

print ("  INICIO  ".center(30, '_')) # Centra usando 30 caracteres.

for x in range(1, 3):
    print("'{0}' {2:10} {1:10.2f}".format(repr(x), x, x * x))

print(30*'-')
for x in range(1, 3):
    print("'{a}' {c:10} {b:10.2f}".format(a=repr(x), b=x, c=x * x))

# !xxx imprime el valor de acuerdo a cierta función. Los valores posibles son:
# !a aplica ascii()
# !s aplica str(),
# !r aplica repr():

print(30*'-')
for x in range(1, 3):
    print(f"{str(x)!r:2} {x * x: 10d} {x: 10.2f}")


print ("  FIN  ".center(30, '_')) # Centra usando 30 caracteres.