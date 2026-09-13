class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        for token in tokens:
            if token in ['+', '-', '*', '/']:
                item1 = stack.pop()
                item2 = stack.pop()
                if token == '+':
                    stack.append(item2 + item1)
                elif token == '-':
                    stack.append(item2 - item1)
                elif token == '*':
                    stack.append(item2 * item1)
                elif token == '/':
                    stack.append(int(item2 / item1))
            else:
                stack.append(int(token))

        return stack.pop()

        