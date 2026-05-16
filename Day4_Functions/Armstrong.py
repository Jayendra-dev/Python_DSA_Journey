# ARMSTRONG NUMBER-LOGIC BUILDING
# Concept :Multiple operations ek function mei
# USE:Number ke digits pe kaam karna sikhata hai 
#Problem :is_armstrong(num) banao.153=1^3+5^3+3^3---True
def is_armstrong(num):
    # Number ko string me badlo taaki digit count nikale
    order = len(str(num))
    temp = num
    sum = 0
    
    # Har digit ka cube jodo
    while temp > 0:
        digit = temp % 10  # Last digit nikalo
        sum += digit ** order  # Cube karke jodo
        temp //= 10  # Last digit hata do
    
    return sum == num

print(is_armstrong(153))  # True
print(is_armstrong(9474)) # True, kyunki 9⁴+4⁴+7⁴+4⁴=9474


# Important points
temp%10   # Number ka last duigit deta h
temp//10  #last digit hata deta h.
order      # Digit kitne h ye batata hai.153=3 digits,9474=4 digits.
