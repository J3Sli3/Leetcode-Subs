class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        mix = sorted(list(zip(position, speed)), reverse=True)
        s = []
        for pos,sp in mix:
            l = (target-pos)/sp
            if not s or (s[-1] < l):
                s.append(l)
        return len(s)

        