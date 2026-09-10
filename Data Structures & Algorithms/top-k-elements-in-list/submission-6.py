class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numi = Counter(nums)
        dic = {}
        l = []
        l2 = []
        for i in numi.items():
            if i[1] not in dic:
                dic[i[1]] = [i[0]]
            else:
                dic[i[1]].append(i[0])
        h = sorted(dic.keys(), reverse=True)
        print(dic)
        print(h)
        i = 0
        while len(l2) != k:
            l.append(dic[h[i]])
            l2 = sum(l, [])
            i+=1
            
        return l2
