# Operators 

x = 5
y = 8

print(x + y)
print(x - y)
print(x * y)
print(x / y)

# // % divmod() **
print(x // y)
print(x % y)        # % : modulars (remainder) 5 / 8 = 0 ... 5
                    # level up
print(divmod(x,y))  # result type: list
print(x ** y)       # ** : power (to the power of ... )

x += 3      # x = x + 3

x, y = 10 + x, 18 + x
print(x)    # 18
print(y)    # 26
