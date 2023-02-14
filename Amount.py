# Caleb Verstraete
# CS325
# 02/08/2023

def main():
    print(amount([11,1,3,2,6,1,5], 8))

# Code adapted from OSU Canvas module 4.4 CS325 Backtracking peudocode powerset
# 02/08/2023
#https://canvas.oregonstate.edu/courses/1901711/pages/exploration-4-dot-4-backtracking?module_item_id=22792882
def amount(A, S):
    result = []
    A.sort(reverse=True)
    amount_helper(len(A) - 1, [], A, result, S)
    return result


def amount_helper(pointer, choices_made, inputSet, result, target):
    if (pointer < 0 and target == 0 and choices_made not in result):
        result.append([])
        result[len(result) - 1] = choices_made.copy()
        return
    elif (pointer < 0):
        return

    choices_made.append(inputSet[pointer])
    amount_helper(pointer - 1, choices_made, inputSet, result, target - inputSet[pointer])
    choices_made.pop()
    amount_helper(pointer - 1, choices_made, inputSet, result, target)


if __name__ == '__main__':
    main()