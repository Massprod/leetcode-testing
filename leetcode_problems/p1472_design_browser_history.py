# You have a browser of one tab where you start on the homepage
#  and you can visit another url, get back in the history number of steps
#  or move forward in the history number of steps.
# Implement the BrowserHistory class:
#  - BrowserHistory(string homepage) Initializes the object with the homepage of the browser.
#  - void visit(string url) Visits url from the current page.
#    It clears up all the forward history.
#  - string back(int steps) Move steps back in history.
#    If you can only return x steps in the history and steps > x,
#     you will return only x steps. 
#    Return the current url after moving back in history at most steps.
#  - string forward(int steps) Move steps forward in history.
#    If you can only forward x steps in the history and steps > x,
#     you will forward only x steps.
#    Return the current url after forwarding in history at most steps.
# -----------------------
# 1 <= homepage.length <= 20
# 1 <= url.length <= 20
# 1 <= steps <= 100
# homepage and url consist of  '.' or lower case English letters.
# At most 5000 calls will be made to visit, back, and forward.


class BrowserHistory:
    # working_sol (77.90%, 79.53%) -> (29ms,  20.04mb)

    def __init__(self, homepage: str):
        self.history: list[str] = [homepage]
        self.cur_index: int = 0

    def visit(self, url: str) -> None:
        self.history = self.history[:self.cur_index + 1]
        self.history.append(url)
        self.cur_index = len(self.history) - 1

    def back(self, steps: int) -> str:
        self.cur_index = max(0, self.cur_index - steps)
        return self.history[self.cur_index]
    
    def forward(self, steps: int) -> str:
        self.cur_index = min(len(self.history) - 1, self.cur_index + steps)
        return self.history[self.cur_index]
