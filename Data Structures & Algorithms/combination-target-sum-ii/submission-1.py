class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        results, path = [], []

        # Sort the candidates
        candidates.sort()

        def _combination_sum_2(
            index: int,
            remaining: int,
        ) -> None:
            if remaining < 0:
                return None
            if remaining == 0:
                results.append(path[:])
                return None

            # Now, iter through the choices and explore them
            # off.
            for choice in range(index, len(candidates)):
                if candidates[choice] > remaining:
                    break
                if choice > index and candidates[choice] == candidates[choice - 1]:
                    continue # Skip reoccuring path
                # Add this choice to the path only if the choice is unique in the path
                path.append(candidates[choice])
                # Now, explore the rest. Note that
                # it has to be distinct candidates, we
                # cannot reuse.
                _combination_sum_2(choice + 1, remaining=remaining - candidates[choice])
                # Pop the choice
                path.pop()
            return None

        _combination_sum_2(0, target)
        return results