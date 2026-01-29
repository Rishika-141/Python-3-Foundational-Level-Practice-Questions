# Questions on Lists
# Print positive and negative elements of a list

L = [10, 230, 4, -4, 802, -111, 0, 90]

print("Positive Elements are as follows:")
for i in L:
    if i >= 0:
        print(i)

print("\nNegative Elements are as follows:")
for i in L:
    if i < 0:
        print(i)

# Mean of the List

list_sum = 0
total = len(L)
for i in L:
    list_sum += i
mean = list_sum / total
print(mean)

# Find the greatest element and print its index too

greatest_elem = L[0]
index = 0
for i in range(1, len(L)):
    if L[i] > greatest_elem:
        greatest_elem = L[i]
        index = i

print(f'The greatest element within the list is {greatest_elem} and its index is {index}')

# Find the second greatest element and print its index as well

largest = L[0]
second_largest = L[0]
for i in range(len(L)):
    if L[i] > largest:
        second_largest = largest
        largest = L[i]
        index = L.index(second_largest)
    elif L[i] > second_largest:
        second_largest = L[i]
        index = i
print(f'The second greatest number within the list is {second_largest} at {index} index')

# Check whether the List is Sorted or Not Sorted

for i in range(len(L) - 1):
    if L[i] < L[i+1]:
        continue
    else:
        print("The List is NOT SORTED")
        break
else:
    print("The List is SORTED")
