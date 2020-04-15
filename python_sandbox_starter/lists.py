# A List is a collection which is ordered and changeable. Allows duplicate members.
numbers = [5, 10, 15, 20, 25]
numbers2 = list((2, 4, 6, 8, 10))
numbers3 = [*numbers2, *numbers]

print(numbers3)

fruits = ["Mango", "Watermelon", "Pineapple", "Coconut"]

fruits.append("Pomegranate")
fruits.insert(2, "Strawberries")
fruits.remove("Pineapple")
fruits.pop(3)
fruits.reverse()
fruits.sort()
fruits.sort(reverse=True)

print(fruits)
