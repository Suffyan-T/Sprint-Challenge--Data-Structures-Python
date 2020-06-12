import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# -----ORIGINAL----- 
# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# This Implimentaion is O(n^2)
# Runtime is  4.47686505317688 seconds





# -----ATTEMPT 1-----
# for item in names_1:
#   if item in names_2:
#     duplicates.append(item)

# This Implimentaion is O(n)
# Runtime is  0.8600955009460449 seconds





# -----ATTEMPT 2-----
# [duplicates.append(item) for item in names_1 if item in names_2]

# This Implimentaion is also O(n), but with code cleaned up and a slightly faster runtime
# Runtime is  0.8572025299072266 seconds





# -----ATTEMPT 3-----

# CREATE Binary Search Tree
class BinarySearchTree:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left == None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        else:
            if self.right == None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    def contains(self, target):
        if self.value == target:
            return True
        elif target < self.value:
            if self.left is not None:
                return self.left.contains(target)
            else:
                return False
        elif target > self.value:
            if self.right is not None:
                return self.right.contains(target)
            else:
                return False

# IMPLEMENT SOLUTION

# Create a BST with names_1[0]
BST = BinarySearchTree(names_1[0])

# For each name in names_1
for name in names_1:
    # Insert name into BST 
    BST.insert(name) 

# For each name in names_2
for name in names_2:
    # If the name from names_2 matches name in BST made with names_1 
    if BST.contains(name):
        # Add the name to duplicates list 
        duplicates.append(name)

# This Implimentaion is O(log n)
# Runtime is  0.08483457565307617 seconds








end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
