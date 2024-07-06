def set_union(set1, set2):
    return set1.union(set2)

def set_intersection(set1, set2):
    return set1.intersection(set2)

def set_difference(set1, set2):
    return set1.difference(set2)

# Example usage
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print("Set 1:", set1)
print("Set 2:", set2)

union_result = set_union(set1, set2)
print("Union of Set 1 and Set 2:", union_result)

intersection_result = set_intersection(set1, set2)
print("Intersection of Set 1 and Set 2:", intersection_result)

difference_result = set_difference(set1, set2)
print("Difference of Set 1 and Set 2 (Set 1 - Set 2):", difference_result)
