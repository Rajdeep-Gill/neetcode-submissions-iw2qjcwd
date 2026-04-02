class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        largest_left = [0]
        largest_right = [0] * n

        for i in range(1, n):
            largest_left.append(
                max(largest_left[i-1], height[i-1])
            )

        for i in range(n-2, -1, -1):
            largest_right[i] = max(
                largest_right[i+1],
                height[i+1]
            )

        ans = 0 

        for i in range(n):
            left_wall = largest_left[i]
            right_wall = largest_right[i]
            curr_wall = height[i]

            ans += max(
                0,
                min(left_wall, right_wall) - curr_wall 
            )

        return ans