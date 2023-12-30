class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # Create an adjacency list for the courses
        coursePrerequisites = { i : [] for i in range(numCourses)}
        for course, prerequisite in prerequisites:
            coursePrerequisites[course].append(prerequisite)
        
        isVisited = set()
        # DFS solution to find eligibility
        def findEligibility(course):
            # TODO: Stopping Criterias
            if course in isVisited:
                return False
            if coursePrerequisites[course] == []:
                return True
            
            isVisited.add(course)
            for prerequisite in coursePrerequisites[course]:
                if not findEligibility(prerequisite): return False
            
            isVisited.remove(course)
            coursePrerequisites[course] = []
            return True
        
        # Loop through every course
        for course in range(numCourses):
            if not findEligibility(course): return False
        
        return True
        
