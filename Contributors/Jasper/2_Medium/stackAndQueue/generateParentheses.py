class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        # Pseudo--
        # 1. Initialize an empty result list.
        # 2. Define a recursive helper function that builds the string:
        #   > If the current string is complete (open == close == n):
        #     >> Add the current string to result.
        #   > If open < n:
        #     >> Add "(" and recurse with open + 1.
        #   > If close < open:
        #     >> Add ")" and recurse with close + 1.
        # 3. Call the helper function starting with an empty string and 0 open/close.
        # 4. Return the result list.

        res = []

        def backtrack(curr: str, open_count: int, close_count: int):
            if open_count == close_count == n:
                res.append(curr)
                return
            if open_count < n:
                backtrack(curr + "(", open_count + 1, close_count)
            if close_count < open_count:
                backtrack(curr + ")", open_count, close_count + 1)

        backtrack("", 0, 0)
        return res
