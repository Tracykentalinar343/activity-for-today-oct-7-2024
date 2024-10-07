choice = input("Remove by index or value?(index/value):")
numbers = [12,34,43,56,8,78]

if choice.lower() == "index":
    index = int(input("Enter the index of the element to remove: "))
    if 0 <= index < len(numbers):
        numbers.pop(index)
        print("Element at index {} removed.".format(index))
    else:
        print("Invalid index.")
elif choice.lower() == "value":
    value = int(input("Enter the value of the element to remove: "))
    if value in numbers:
        numbers.remove(value)
        print("Element with value {} removed.".format(value))
    else:
        print("Value not found in the list.")
else:
    print("Invalid choice.")