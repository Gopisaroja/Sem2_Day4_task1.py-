# List, maximum value, even_count, sum of the elements, reverse of a list
num = []
total = 0
n = int(input("Enter how many elements: "))
even = 0

if n > 0:
    for i in range(n):
        nums = int(input("Enter element %d: " % (i+1)))
        num.append(nums)
        total += num[i]

    maximum = num[0]
    minimum = num[0]

    delete = int(input("Enter a number to delete: "))

    print("Even numbers:")

    for i in range(n):
        if num[i] > maximum:
            maximum = num[i]

        if num[i] < minimum:
            minimum = num[i]

        if num[i] % 2 == 0:
            print(num[i])
            even += 1

    print("Maximum value:", maximum)
    print("Minimum value:", minimum)
    print("List:", num)
    print("Total:", total)
    print("Even numbers:", even)

    print("Reverse of the list:")
    for i in range(n-1, -1, -1):
        print(num[i])

    if delete in num:
        num.remove(delete)
    else:
        print("Element not present in list.")

    print("After deleting a number:")
    print(num)

else:
    print("Enter a positive number!")