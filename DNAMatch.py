# Caleb Verstraete
# CS 325
# Date 1/27/23


def main():
    DNA1 = 'ATAGTTCCGTCAAA'
    DNA2 = 'BAC'
    print(dna_match_bottomup(DNA1, DNA2))

# Code adapted from OSU Canvas module 3.3 CS325
# 01/27/2023
# https://canvas.oregonstate.edu/courses/1901711/pages/exploration-3-dot-3-dynamic-programming-longest-common-subsequence-problem?module_item_id=22792872
def dna_match_bottomup(DNA1, DNA2):
    cache = [[0 for x in range(len(DNA2) + 1)] for x in range(len(DNA1) + 1)]
    for i in range(len(DNA1) + 1):
        for j in range(len(DNA2) + 1):
            if i == 0 or j == 0:
                cache[i][j] = 0
            elif DNA1[i - 1] == DNA2[j - 1]:
                cache[i][j] = cache[i - 1][j - 1] + 1
            else:
                cache[i][j] = max(cache[i - 1][j], cache[i][j - 1])
    return cache[len(DNA1)][len(DNA2)]


def dna_match_topdown(DNA1, DNA2):
    cache = [[None for x in range(len(DNA1) + 1)] for x in range(len(DNA2) + 1)]
    return dna_topdown_helper(DNA1, DNA2, len(DNA1), len(DNA2), cache)

def dna_topdown_helper(DNA1, DNA2, DNA1_len, DNA2_len, cache):
    if DNA1_len == 0 or DNA2_len == 0:
        cache[DNA2_len][DNA1_len] = 0
        return cache[DNA2_len][DNA1_len]
    elif cache[DNA2_len][DNA1_len] is not None:
        return cache[DNA2_len][DNA1_len]
    elif DNA1[DNA1_len - 1] == DNA2[DNA2_len - 1]:
        cache[DNA2_len][DNA1_len] = 1 + dna_topdown_helper(DNA1, DNA2, DNA1_len - 1, DNA2_len - 1, cache)
        return cache[DNA2_len][DNA1_len]
    else:
        cache[DNA2_len][DNA1_len] = max(dna_topdown_helper(DNA1, DNA2, DNA1_len, DNA2_len - 1, cache), dna_topdown_helper(DNA1, DNA2, DNA1_len - 1, DNA2_len, cache))
        return cache[DNA2_len][DNA1_len]

def lcs_BF_helper(s1, s2, m,n):
    if m < 0 or n < 0:
        return 0;
    elif s1[m] == s2[n]:
        return 1 + lcs_BF_helper(s1, s2 , m-1, n-1)
    else:
        return max(lcs_BF_helper(s1, s2, m-1 , n), lcs_BF_helper(s1, s2, m, n-1))

def lcs_BF(str1, str2):
    return lcs_BF_helper(str1,str2, len(str1)-1, len(str2)-1)

if __name__ == '__main__':
    main()