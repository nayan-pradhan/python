smartphones = [] #this is my list

print (smartphones)

#append data to my list
smartphones.append("nokia")
smartphones.append("samsung")
smartphones.append("apple")
smartphones.append("huwaei")
smartphones.append("xiomi")
smartphones.append("LG")
smartphones.append("Sony")
smartphones.append("Google Pixel")

for smartphone in smartphones:
    print (smartphone.strip().title())

print (smartphones)

#delete sth
del smartphones[0] #deletes nokia

print (smartphones)

#overwrite/change data
smartphones[1] = "asus"

print (smartphones)

poped_value = smartphones.pop()
print(smartphones)
print(poped_value)

smartphones.insert(0, "Carbon")
smartphones.append("Blackberry")
smartphones.append("Apple")
print ("The first smartphone I owned was " + smartphones.pop(0) + ".")

print(smartphones)

ios = "Apple"
smartphones.remove(ios)

print(smartphones)

smartphones.sort()
print(smartphones)

smartphones.sort(reverse = True)
print(smartphones)

prices = [4,5,7,2,4,54,2,4,6,54,563,432]       #just random numbers I want to sort
print(prices)
prices.sort()
print(prices)
prices.sort(reverse = True)
print(prices)

print (len(prices))

print(prices[-1])

for numbers in prices:
    print(numbers)

for brands in smartphones:
    print(brands)

for numbers in range(1, 10):
    print(numbers)

numbers = list(range(1, 12))

print(max(numbers))

squares = [value**2 for value in range(1, 11)]
print (squares)

#sum numbers upto 100

ssuumm = 0
for value in range(1, 101):
    ssuumm += value 
print(ssuumm)