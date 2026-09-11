from collections import deque 

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return False

        d = deque()
        for character in s:
            if character in [')', ']', '}'] and len(d)==0:
                return False
            if character == ')':
                x = d.pop()
                if x != '(':
                    return False
            elif character == ']':
                x=d.pop()
                if x != '[':
                    return False
            elif character =='}':
                x=d.pop()
                if x != '{':
                    return False
            else:
                d.append(character)



        if len(d) !=0: 
            return False 

        return True 
                
            

        