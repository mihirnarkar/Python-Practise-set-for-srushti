# To print avg of three numbers

def avg(a,b,c):
    d = (a+b+c)/3
    return d

avg = avg(10,10,10)
print(f"Average: {avg}")
print(f"Type: {type(avg)}")
newvalue = int(avg)
print(f"Typecast: {newvalue}")
print(f"Type: {type(newvalue)}")


