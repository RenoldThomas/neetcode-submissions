class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        parts = []
        for s in str:
            parts.append(f"{len(s)}#{s}")
        return "".join(parts)
