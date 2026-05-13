class Solution:
    def numDecodings(self, s: str) -> int:
        # At any instance character s[i], we have 2 options - we choose s[i] in which case,
        # we will be focused on the s[i + 1] in the next level or we will choose s[i: i+2] -
        # in which case, we will be focused on s[i + 2] on the next level. We do this until
        # we reach the end of len(s)
        memory: dict[int, int] = dict[int, int]()

        def _num_decodings(
            index: int,
        ) -> int:

            # Base case
            if index >= len(s):
                return 1
            if index == len(s) - 1:
                return 1 if s[index] != "0" else 0
            if s[index] == "0":
                return 0
            # Check memory
            lookup: int | None = memory.get(index, None)
            if lookup is not None:
                return lookup
            else:
                pass
            # Recursive conditions
            result = _num_decodings(index + 1)
            if index + 1 < len(s) and int(s[index : index + 2]) < 27:
                result += _num_decodings(index + 2)
            memory[index] = result
            return result

        return _num_decodings(0)
