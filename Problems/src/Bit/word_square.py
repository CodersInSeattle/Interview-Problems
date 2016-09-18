"""
Word Square definition, 0<=k<n(width/length), row k and column k are idenitcal
eg: row 1: ABCD and column 1:ABCD are the same
"""
from copy import deepcopy


def word_square(strs, k):
    """
    :type strs: List[str], k: int
    :rtype: List[List[str]]
    """
    strs_filtered = [s for s in strs if len(s) <= k]
    path, res = [], []
    for i, string in enumerate(strs_filtered):
        if len(string) == k:
            path.append(string)
            strs_filtered.remove(string)
            dfs(strs_filtered, k, path, 1, res)
            strs_filtered.insert(i, string)
            path.pop()
    return res


def validate(step, path, string):
    """
    :type ....
    :rtype: boolean
    """
    for i in range(min(len(string), len(path))):
        if len(path[i]) <= step or string[i] != path[i][step]:
            return False
    return True


def dfs(strs, k, path, step, res):
    """
    :type tickets: List[List[str]]
    :rtype: List[str]
    """
    if step == k:
        res.append(deepcopy(path))
        return
    min_length = 0
    while min_length < len(path):
        if len(path[min_length]) < step:
            break
        min_length += 1
    strs_filtered = [s for s in strs if len(s) >= min_length]
    for i, string in enumerate(strs_filtered):
        if validate(step, path, string):
            path.append(string)
            strs.remove(string)
            dfs(strs, k, path, step + 1, res)
            strs.insert(i, string)
            path.pop()


TEST = ["ABCD", "BNRT", "CRMY", "DTYE", "CRM", "DT", "DTY"]
print word_square(TEST, 4)
