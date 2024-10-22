def calculate(a, b):
    union = list(set(a) | set(b))
    intersect = list(set(a) & set(b))
    a_b = list(set(a) - set(b))
    b_a = list(set(b) - set(a))
    return union, intersect, a_b, b_a


a = [1, 2, 3, 4, 5, 6]
b = [2, 3, 23, 5, 46]
union, intersect, a_b, b_a = calculate(a, b)
print("Union: " + str(union) +
      "\nIntersection: " + str(intersect) +
      "\nA/B: " + str(a_b) +
      "\nB/A: " + str(b_a))