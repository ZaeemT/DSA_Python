"""
# Stack implemented using list

s = []
s.append("22")
s.append("21213")
s.append("223")

print(s)

s.pop()

print(s)

print(s[-1])
"""

# Stack implemented using collections
from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        return self.container.append(val)
    
    def pop(self):
        return self.container.pop()
    
    def peek(self):
        return self.container[-1]
    
    def size(self):
        return len(self.container)
    

def rev_string(text):
    s = Stack()

    for char in text:
        # inserting element in stack
        s.push(char)

    reverse_text = ""
    while (s.size() >= 1):
        reverse_text += s.pop()

    print(reverse_text)

    
def is_match(ch1, ch2):
    match_dict = {
        ")" : "(" ,
        "]" : "[" ,
        "}" : "{" 
    }
    if match_dict[ch1] == ch2:
        return True
    else:
        return False

def is_balanced(string):
    s = Stack()

    for char in string:
        if char=="(" or char=="[" or char=="{":
            s.push(char)
        if char==")" or char=="]" or char=="}":
            if s.size()== 0:
                return False
            if not is_match(char, s.pop()):
                return False
    return True    


if __name__ == "__main__":
    rev_string("We will conquere COVID-19")
    print(is_balanced("({a+b})"))
    print(is_balanced("))((a+b}{"))
    print(is_balanced("((a+b))"))
    print(is_balanced("((a+g))"))
    print(is_balanced("))"))
    print(is_balanced("[a+b]*(x+2y)*{gg+kk}"))

