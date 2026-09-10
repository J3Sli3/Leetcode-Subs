class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for i in strs:
            if tuple(sorted(Counter(i).items())) not in dic:
                dic[tuple(sorted(Counter(i).items()))] = [i]
            else:
                dic[tuple(sorted(Counter(i).items()))].append(i)
        return list(dic.values())

