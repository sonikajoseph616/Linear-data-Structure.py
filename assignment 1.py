# que. 1


def getPairsCount(arr, n, sum):
 
    count = 0  # Initialize result
 
    # Consider all possible pairs
    # and check their sums
    for i in range(0, n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == sum:
                count += 1
 
    return count
 
 
# Driver function
arr = [1, 5, 7, -1, 5]
n = len(arr)
sum = 6
print("Count of pairs is",
      getPairsCount(arr, n, sum))

# que 2
# Iterative python program to reverse an array
 
# Function to reverse A[] from start to end
def reverseList(A, start, end):
    while start < end:
        A[start], A[end] = A[end], A[start]
        start += 1
        end -= 1
 
# Driver function to test above function
A = [1, 2, 3, 4, 5, 6]
print(A)
reverseList(A, 0, 5)
print("Reversed list is")
print(A)

# que-3
# Python program to check if strings are rotations of
# each other or not
 
# Function checks if passed strings (str1 and str2)
# are rotations of each other
def areRotations(string1, string2):
    size1 = len(string1)
    size2 = len(string2)
    temp = ''
 
    # Check if sizes of two strings are same
    if size1 != size2:
        return 0
 
    # Create a temp string with value str1.str1
    temp = string1 + string1
 
    # Now check if str2 is a substring of temp
    # string.count returns the number of occurrences of
    # the second string in temp
    if (temp.count(string2)> 0):
        return 1
    else:
        return 0
 
# Driver program to test the above function
string1 = "AACD"
string2 = "ACDA"
 
if areRotations(string1, string2):
    print ("Strings are rotations of each other")
else:
    print ("Strings are not rotations of each other")

# que-4

# Python program to print the first non-repeating character
 
string = "geeksforgeeks"
index = -1
fnc = ""
for i in string:
    if string.count(i) == 1:
        fnc += i
        break
    else:
        index += 1
if index == 1:
    print("Either all characters are repeating or string is empty")
else:
    print("First non-repeating character is", fnc)

# que-5

def TowerOfHanoi(n, from_rod, to_rod, aux_rod):
    if n == 0:
        return
    TowerOfHanoi(n-1, from_rod, aux_rod, to_rod)
    print("Move disk", n, "from rod", from_rod, "to rod", to_rod)
    TowerOfHanoi(n-1, aux_rod, to_rod, from_rod)
  
  
# Driver code
N = 3
  
# A, C, B are the name of rods
TowerOfHanoi(N, 'A', 'C', 'B')

# que-6
# Python program to convert infix expression to postfix
  
  
# Class to convert the expression
class Conversion:
  
    # Constructor to initialize the class variables
    def _init_(self, capacity):
        self.top = -1
        self.capacity = capacity
          
        # This array is used a stack
        self.array = []
          
        # Precedence setting
        self.output = []
        self.precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
  
    # Check if the stack is empty
    def isEmpty(self):
        return True if self.top == -1 else False
  
    # Return the value of the top of the stack
    def peek(self):
        return self.array[-1]
  
    # Pop the element from the stack
    def pop(self):
        if not self.isEmpty():
            self.top -= 1
            return self.array.pop()
        else:
            return "$"
  
    # Push the element to the stack
    def push(self, op):
        self.top += 1
        self.array.append(op)
  
    # A utility function to check is the given character
    # is operand
    def isOperand(self, ch):
        return ch.isalpha()
  
    # Check if the precedence of operator is strictly
    # less than top of stack or not
    def notGreater(self, i):
        try:
            a = self.precedence[i]
            b = self.precedence[self.peek()]
            return True if a <= b else False
        except KeyError:
            return False
  
    # The main function that
    # converts given infix expression
    # to postfix expression
    def infixToPostfix(self, exp):
  
        # Iterate over the expression for conversion
        for i in exp:
              
            # If the character is an operand,
            # add it to output
            if self.isOperand(i):
                self.output.append(i)
  
            # If the character is an '(', push it to stack
            elif i == '(':
                self.push(i)
  
            # If the scanned character is an ')', pop and
            # output from the stack until and '(' is found
            elif i == ')':
                while((not self.isEmpty()) and
                      self.peek() != '('):
                    a = self.pop()
                    self.output.append(a)
                if (not self.isEmpty() and self.peek() != '('):
                    return -1
                else:
                    self.pop()
  
            # An operator is encountered
            else:
                while(not self.isEmpty() and self.notGreater(i)):
                    self.output.append(self.pop())
                self.push(i)
  
        # Pop all the operator from the stack
        while not self.isEmpty():
            self.output.append(self.pop())
  
        for ch in self.output:
            print(ch, end="")
  
  
# Driver code
if _name_ == '_main_':
    exp = "a+b*(c^d-e)^(f+g*h)-i"
    obj = Conversion(len(exp))
  
    # Function call
    obj.infixToPostfix(exp)

# que-7
# Python Program to convert prefix to Infix
def prefixToInfix(prefix):
    stack = []
     
    # read prefix in reverse order
    i = len(prefix) - 1
    while i >= 0:
        if not isOperator(prefix[i]):
             
            # symbol is operand
            stack.append(prefix[i])
            i -= 1
        else:
           
            # symbol is operator
            str = "(" + stack.pop() + prefix[i] + stack.pop() + ")"
            stack.append(str)
            i -= 1
     
    return stack.pop()
 
def isOperator(c):
    if c == "*" or c == "+" or c == "-" or c == "/" or c == "^" or c == "(" or c == ")":
        return True
    else:
        return False
 
# Driver code
if _name=="main_":
    str = "*-A/BC-/AKL"
    print(prefixToInfix(str))

# que-8

# Python3 program to check for
# balanced brackets.
 
# function to check if
# brackets are balanced
 
 
def areBracketsBalanced(expr):
    stack = []
 
    # Traversing the Expression
    for char in expr:
        if char in ["(", "{", "["]:
 
            # Push the element in the stack
            stack.append(char)
        else:
 
            # IF current character is not opening
            # bracket, then it must be closing.
            # So stack cannot be empty at this point.
            if not stack:
                return False
            current_char = stack.pop()
            if current_char == '(':
                if char != ")":
                    return False
            if current_char == '{':
                if char != "}":
                    return False
            if current_char == '[':
                if char != "]":
                    return False
 
    # Check Empty Stack
    if stack:
        return False
    return True
 
 
# Driver Code
if _name_ == "_main_":
    expr = "{()}[]"
 
    # Function call
    if areBracketsBalanced(expr):
        print("Balanced")
    else:
        print("Not Balanced")

# que-9
# create class for stack
class Stack:
 
    # create empty list
    def _init_(self):
        self.Elements = []
         
    # push() for insert an element
    def push(self, value):
        self.Elements.append(value)
       
    # pop() for remove an element
    def pop(self):
        return self.Elements.pop()
     
    # empty() check the stack is empty of not
    def empty(self):
        return self.Elements == []
     
    # show() display stack
    def show(self):
        for value in reversed(self.Elements):
            print(value)
 
# Insert_Bottom() insert value at bottom
def BottomInsert(s, value):
   
    # check the stack is empty or not
    if s.empty():
         
        # if stack is empty then call
        # push() method.
        s.push(value)
         
    # if stack is not empty then execute
    # else block
    else:
        popped = s.pop()
        BottomInsert(s, value)
        s.push(popped)
 
# Reverse() reverse the stack
def Reverse(s):
    if s.empty():
        pass
    else:
        popped = s.pop()
        Reverse(s)
        BottomInsert(s, popped)
 
 
# create object of stack class
stk = Stack()
 
stk.push(1)
stk.push(2)
stk.push(3)
stk.push(4)
stk.push(5)
 
print("Original Stack")
stk.show()
 
print("\nStack after Reversing")
Reverse(stk)
stk.show()
  
# que 10
First = []
num = int(input('How many numbers: '))

for n in range(num):
    numbers = int(input('Enter number: '))
    First.append(numbers)
    
print("Smallest number in the list is :  ", min(First))
