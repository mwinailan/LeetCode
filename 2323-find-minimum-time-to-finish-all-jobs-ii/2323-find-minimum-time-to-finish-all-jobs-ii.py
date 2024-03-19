class Solution:
    def minimumTime(self, jobs: List[int], workers: List[int]) -> int:
        jobs.sort(reverse=True)
        workers.sort(reverse=True)
        minimum_days = 0
        for i in range(len(jobs)):
            minimum_days = max(minimum_days, math.ceil(jobs[i] / workers[i]))
        
        return minimum_days
        