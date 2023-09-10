# def marcsCakewalk(calorie):
#     sorted(calorie, reverse=True)
#     return sum([(2 ** i) * cupCake for i, cupCake in enumerate(calorie)])

def marcsCakewalk(calorie):
    # Write your code here
    minCalorie = float('inf')
    for i, _ in enumerate(calorie):
        calories = 2**0 * i
        for j, _ in enumerate(calorie[:i] + calorie[i+1:]):
            print(calorie[:i] + calorie[i+1:])
            print(f'i: {i}, j: {j}')
            calories += 2**j * i
        minCalorie = min(calories, minCalorie)  
    return minCalorie  

print(marcsCakewalk([5,10,7])) # 
