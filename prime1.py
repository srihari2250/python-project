num = int(input("enter a num"))
for i in range(2,num):
    if num % i == 0:
        print(f"{num},is not a prime")
        break
else:
    print(f"{num} is prime")


