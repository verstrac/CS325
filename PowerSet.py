# Caleb Verstraete
# CS325
# 02/03/2023

def main():
    print(powerset([2,2,3,6]))
    #permutations_backtracking("ABC")

def powerset(inputSet):
    result = []
    powerset_helper(len(inputSet) - 1, [], inputSet, result)
    return result


def powerset_helper(pointer, choices_made, inputSet, result):
    if (pointer < 0):
        result.append([])
        result[len(result) - 1] = choices_made.copy()
        return

    choices_made.append(inputSet[pointer])
    powerset_helper(pointer - 1, choices_made, inputSet, result)
    choices_made.pop()
    powerset_helper(pointer - 1, choices_made, inputSet, result)

def permutations(result, str):
    #base Case, print the result when we obtain the result using all characters
    if(len(result) == len(str)):
        print(''.join(result))

    for i in range(len(str)):
        current_choice = str[i]
        # If the choice was not already made we chose it to include in our result
        if(current_choice not in result):
            result.append(current_choice)
            #recursively calling permutations function until we obtain our result
            permutations(result, str)
            #Once we have exhausted all possible paths we backtrack
            result.pop()

def permutations_backtracking(str):
    permutations([],str)



if __name__ == '__main__':
    main()