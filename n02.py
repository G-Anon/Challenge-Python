#python3
#temperature converter
input = input("Enter a temperature, e.g 24C or 30.2F: ")
temp = float(input[:-1])
scale = input[-1]

if scale.lower() == 'f':
    temp = (temp - 32) * 5.0 / 9.0
    print("%s --> %dC" % (input,temp))
elif scale.lower() == 'c':
    temp = temp * 9.0 / 5.0 + 32
    print("%s --> %dF" % (input,temp))
else:
    print("Can\'t convert to scale '%s'" % scale)\
