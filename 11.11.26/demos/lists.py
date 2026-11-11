numbers = [1, 2, 3, 4, 5]
print(numbers[0])  # Output: 1

# print(numbers[len(numbers)-1])  # Output: 5
print(numbers[-1])  # Output: 5

print(numbers[0:3])  # Output: [1, 2, 3]
print(numbers[:3])  # Output: [1, 2, 3]
print(numbers[2:5])  # Output: [3, 4, 5]


copy_of_numbers = numbers[:]


# ref to the same list
n = numbers


names = ["Alice", "Bob", "Charlie"]


names.append("David")
names += ["Eve", "Frank"]


names.insert(1, "Eve")


names.remove("Charlie")
del names[0]
names.pop(0)

names[0] = "Zoe"


x = 1
y = 2

x, y = y, x


name1, *rest = ["Alice", "Bob", "Charlie", "David"]

print(name1)  # Output: Alice
print(rest)  # Output: ['Bob', 'Charlie', 'David']


numbers = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]

print(sorted(numbers))

print(sorted(numbers, reverse=True))
