class RingBuffer:
    def __init__(self, capacity):
        # Set self.capacity to capacity argument
        self.capacity= capacity
        # Set self.data to and empty list
        self.data=[]
        # Set self.index to 0
        self.index= 0

    def append(self, item):
        # If the length of the self.data list is less than the capacity
        if len(self.data) < self.capacity: 
            # Append the item to the end of the list
            self.data.append(item)

        # Otherwise if the self.data list is the same size as or larger than capacity
        else:
            # Set the value of self.data at index to item
            self.data[self.index] = item
            # Incrament the value of self.index
            self.index += 1

            # if the value of self.index is less than capacity -1
            if self.index > (self.capacity) - 1:
                # Reset index to one
                self.index = 0

    def get(self):
        # Return value in self.data if the value is not None
        return [value for value in self.data if value is not None]


# Runtime Complexity of this solution is O(n)
# Runtime time of this solution is 0.0000 seconds

#Testing
a=RingBuffer(5)
for i in range(10):
    a.append(i)
    print(a.get())

buffer = RingBuffer(3)

print(buffer.get())   # should return []

buffer.append('a')
buffer.append('b')
buffer.append('c')

print(buffer.get())   # should return ['a', 'b', 'c']

# 'd' overwrites the oldest value in the ring buffer, which is 'a'
buffer.append('d')

print(buffer.get())   # should return ['d', 'b', 'c']

buffer.append('e')
buffer.append('f')

print(buffer.get())   # should return ['d', 'e', 'f']