# enter number of people
# enter names
# enter name you want to check
# does the name exist in database?

print("Number of members: ", end = '')
n = int(input())
message = [0] * n

print("Enter names: ")
for i in range(n):
    print(i+1, ": ", end = '')
    message[i] = str(input())

print("Check for name: ", end = '')
checkName = str(input())

bool = False

for i in range(n):
    if (checkName.upper() == message[i].upper()):
        print(checkName.title(), "exists in database!")
        bool = True
        break

if (bool == False):
    print(checkName.title(), "does not exist in database")