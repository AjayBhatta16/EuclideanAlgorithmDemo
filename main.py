def gcd(a,b):
  if a < 0 or b < 0:
    return gcd(abs(a),abs(b))
  if b > a:
    return gcd(b,a)
  if b == 0:
    return a
  if a%b == 0:
    return b
  return gcd(b, a%b)

m = int(input("Enter the first integer: "))
n = int(input("Enter the second integer: "))
print()
print(f"The GCD of your numbers is {gcd(m,n)}")
