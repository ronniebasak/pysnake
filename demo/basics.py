
## this below code takes two variables and adds them
a = 5
b = 6
print(a+b)


## this below code asks for two inputs and adds the results
a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
print(a+b)



## this is a list 
a = [11,2,3,4]

## lists support an index
print("a[0]", a[0])
print("a[1]", a[1])
print("a[2]", a[2])
print("a[3]", a[3])

## we can append an item to a list
a.append(5)
print(a)

## we can calculate the length of an array
print("length of the array is: ",len(a))

## we can take negative indices to access items from the last
print("last item is", a[-1])
print("second to last item is", a[-2])
print("third to last item is", a[-3])


### This is a dictionary, dictionary can store items by arbitrary keys 
### so that we can remember them easily
person = {
    'first_name': 'Sohan',
    'last_name': 'Basak',
    'phone': '1234567890',
    'email': 'xyz@gmail.com',
    'mood': 'happy',
}

person2 = {
    'phone': '0123456789',
    'last_name': 'Dubey',
    'email': 'abc@gmail.com',
    'first_name': 'Rohit',
}

person2['mood'] = input('how is rohit feeling? ')

print("Person 1 First name", person['first_name'])
print("Person 2 First name", person2['first_name'])
print("Person 1 Mood", person['mood'])
print("Person 2 Mood", person2['mood'])



### List slicing
a = [1,2,3,4,5,6]

## we can "slice" a list by giving two numbers
## first is the start index, second is the last index

print("a[0:3]", a[0:3])

## Lists support a "step" key, which is the number of items skipped after every selected items
print("all the even indexed items",a[0::2])
print("all the odd indexed items",a[1::2])

## reverse a list
print("Reversing a list",a[::-1])

# ## last element of an item
print(a[-1])



## Checking if account is opened or not
age = 17
signature = True

if (age > 18) or (age > 16 and signature == True):
    print("Account opened")
else:
    print("Account not opened")



## Checking if a number is small, medium or large
n = int(input("Enter number: "))

if n < 10:
    print("small")
elif n < 100:
    print("medium")
else:
    print("large")



## Finding squares of all numbers till 9 using while loop
start = 1
while start <= 9:
    print(f"Square of {start} is {start**2}")
    start += 1

## FInding squares till 9 using for loop
for start in range(1,10):
    print(f"Square of {start} is {start**2}")


## Above logic using a function
def is_eligible(age, signature):
    if age > 18:
        return True
    elif age > 16 and signature == True:
        return True
    else:
        return False


for age in range(10, 20):
    print(f"Age: {age}, signature True", is_eligible(age, True))
    print(f"Age: {age}, signature False", is_eligible(age, False))
