class ListNode:
    def __init__(self, val="", prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class BrowserHistory:
    def __init__(self, homepage):
        self.cur = ListNode(homepage)
    
    def visit(self, url):
        self.cur.next = ListNode(url, self.cur, None)
        self.cur = self.cur.next
    
    def back(self, steps):
        while self.cur.prev and steps > 0:
            self.cur = self.cur.prev
            steps -= 1
        return self.cur.val
    
    def forward(self, steps):
        while self.cur.next and steps > 0:
            self.cur = self.cur.next
            steps -= 1
        return self.cur.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)

#init(homepage)
#visit(url)
#back(steps)
#forward(steos)