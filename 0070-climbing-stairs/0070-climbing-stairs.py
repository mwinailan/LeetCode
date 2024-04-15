class Solution:
    def climbStairs(self, n: int) -> int:
        # top to bottom approach
        one_step_up = 1
        two_steps_up = 1
        
        for i in range(n - 2, -1, -1):
            current_options = one_step_up + two_steps_up
            two_steps_up = one_step_up
            one_step_up = current_options
        
        return one_step_up
            