num = float(input("Enter a decimal number: "))
integer_part = int(num)
binary_int = ""
if integer_part == 0:
    binary_int = "0"
else:
    n = integer_part
    while n > 0:
        binary_int = str(n % 2) + binary_int
        n //= 2
fraction_part = num - integer_part
binary_frac = ""
count = 0
while fraction_part > 0 and count < 20:
    fraction_part *= 2
    bit = int(fraction_part)
    binary_frac += str(bit)
    fraction_part -= bit
    count += 1
if binary_frac:
    print("Binary:", binary_int + "." + binary_frac)
else:
    print("Binary:", binary_int)