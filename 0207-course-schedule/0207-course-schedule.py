class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courseVisited = set()
        coursePrereq = {i: [] for i in range(numCourses)}
        
        for course, prereq in prerequisites:
            coursePrereq[course].append(prereq)
        
        def canFinishCourse(course):
            if course in courseVisited:
                return False
            if coursePrereq[course] is []:
                return True
            
            courseVisited.add(course)
            for prereq in coursePrereq[course]:
                if not canFinishCourse(prereq):
                    return False
            coursePrereq[course] = []
            courseVisited.remove(course)
            
            return True
        
        for course in range(numCourses):
            if not canFinishCourse(course): return False
        
        return True
        