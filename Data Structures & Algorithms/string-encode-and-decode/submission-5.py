class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs:
            separator = "TABARNAK2234"
            result = separator.join(strs)
            return result
        else:
            return "EMPTY"

    def decode(self, s: str) -> List[str]:
        if s == "EMPTY":
            return []
        else:
            print(s)
            separator = "TABARNAK2234"
            result = s.split(separator)
            return result

