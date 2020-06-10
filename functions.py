def hello_func():
    print ("Hello Function!")

def greeting(string):
    return "{} ".format(string)

def sum(a, b):
    return a+b

def largestNum(array):
    lar = array[0]
    for i in array:
        if i > lar:
            lar = i
    return lar


hello_func()
print(greeting("hi"))
print(sum(24,12))
array = [1,3,5,7,2,4,7,3,6,0,7,8,9,6,4,2,8,23]
print(largestNum(array))