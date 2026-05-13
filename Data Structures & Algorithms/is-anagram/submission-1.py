class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            pass
        hash_map__S: dict = {}
        hash_map__T: dict = {}
        for i, j in zip(s, t):
            hash_map__S[i] = hash_map__S.get(i, 0) + 1
            hash_map__T[j] = hash_map__T.get(j, 0) + 1
        for i, i_value in hash_map__S.items():
            if hash_map__T.get(i, 0) != i_value:
                return False
            else:
                pass
        return True 