class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        res = set()
        for e in emails:
            local, domain = e.split("@")
            local = local.split("+")[0]
            local = local.replace(".", "")
            
            res.add((local, domain))
        
        return len(res)
        