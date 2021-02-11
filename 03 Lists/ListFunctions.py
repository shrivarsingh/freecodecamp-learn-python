
lucky_numbers = [42, 4, 8, 15, 16, 23]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends2 = friends.copy()

print(friends)
print(friends2)

friends.extend(lucky_numbers)
print(friends)

friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends.append("Creed")
friends.insert(1, "Kelly")
friends.remove("Jim")
print(friends)
print(friends.index("Kevin"))

friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends.pop()
print(friends)

friends = ["Kevin", "Karen", "Jim", "Jim", "Oscar", "Toby"]
print(friends.count("Jim"))

friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends.sort()
print(friends)
lucky_numbers.sort()
print(lucky_numbers)
lucky_numbers.reverse()
print(lucky_numbers)

friends.clear()
print(friends)