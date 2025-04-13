class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        # Pseudo--
        # 1. Zip together each car's position and speed, then sort by position in descending order.
        # 2. Initialize an empty stack to keep track of fleet arrival times.
        # 3. Traverse the sorted cars:
        #   > Compute the time it takes for each car to reach the destination.
        #   > If the stack is empty or current time > time at top of stack:
        #     >> Push current time to stack (new fleet).
        #   > Else:
        #     >> Current car joins fleet ahead (do nothing).
        # 4. Return the size of the stack as the number of fleets.

        cars = sorted(zip(position, speed), reverse=True)
        stack = []

        for pos, spd in cars:
            time = (target - pos) / spd
            if not stack or time > stack[-1]:
                stack.append(time)

        return len(stack)
