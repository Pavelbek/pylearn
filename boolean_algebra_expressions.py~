
# We should check if expressions True or False depends on values of variables and type of operation


# This is my not perfect solution

def bool_algebra(x,y,operation):
    if operation == "conjunction":
        if x == y and y == 1:
            return 1
        else:
            return 0
    if operation == "disjunction":
        if x == 1 or y == 1:
            return 1
        else:
            return 0
    if operation == "implication":
        if x == 1 and y == 0:
            return 0
        else:
            return 1
    if operation == "exclusive":
        if x != y:
            return 1
        else:
            return 0
    if operation == "equivalence":
        if x == y:
            return 1
        else: return 0
            
print(bool_algebra(1,1,"disjunction"))
            
# Good solution, but not mine

OPERATION_NAMES = ("conjunction", "disjunction", "implication", "exclusive", "equivalence")
?
def boolean(x, y, operation):
    results = {"conjunction" : x and y,
               "disjunction" : x or y,
               "implication" : y or not x,
               "exclusive"   : x ^ y,
               "equivalence" : x == y
    }
    return results[operation]