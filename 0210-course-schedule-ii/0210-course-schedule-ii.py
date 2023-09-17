class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjacencyList = {c : [] for c in range(numCourses)}
        coursesToTake = []
        
        for course, prereq in prerequisites:
            adjacencyList[course].append(prereq)
        
        isVisited, isPath = set(), set()
        def findEligibility(course):
            if course in isPath:
                return False
            if course in isVisited:
                return True
            
            isPath.add(course)
            for prereqs in adjacencyList[course]:
                if not findEligibility(prereqs):
                    return False
            isPath.remove(course)
            
            isVisited.add(course)
            coursesToTake.append(course)
            return True
        
        for course in range(numCourses):
            if not findEligibility(course):
                return []
        
        return coursesToTake
            
        