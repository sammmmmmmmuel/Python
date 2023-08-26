# x = int(input("first num:"))     # String
# y = int(input("second num:"))    # String

# print(x + y)

##########################

# Comparison : result (True/False)
# == != > < >= <=
# and or not

a = 3
b = 5
print (a == b and a > b or a >= 3)  # And has higher priority than or

##########################

age = 20

age = float(input("Your age : "))  # instead of int(input("Your age : ")) use float which includes decimals
result = ""

if age > 20 :
    result = "beer"
elif 20 >= age and age > 1 : 
    result = 'juice'
else:
    result = 'milk'     # both (') and (") works the same doesn't matter

print(result)