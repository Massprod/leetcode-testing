# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.


def gen_parentheses(n: int) -> list[str]:
    combos = []
    origin = "("
    counter = ")"
    temp = []

    def back_tracking(tempo: list, opened: int = 0, closed: int = 0):
        if len(tempo) == 2 * n:
            combos.append("".join(tempo))
            return
        if opened < n:
            tempo.append(origin)
            back_tracking(tempo, opened + 1, closed)
            tempo.pop()
        if closed < opened:
            tempo.append(counter)
            back_tracking(tempo, opened, closed + 1)
            tempo.pop()
    back_tracking(temp)
    return combos


test1 = 3
test1_out = ["((()))", "(()())", "(())()", "()(())", "()()()"]
print(gen_parentheses(test1))
assert test1_out == gen_parentheses(test1)
