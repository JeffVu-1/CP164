"""
-------------------------------------------------------
Assignment 3 functions.py
-------------------------------------------------------
Author:  Jeff Vu
ID:      169058539
Email:   vuxx8539@mylaurier.ca
__updated__ = "0000-00-00"
-------------------------------------------------------
"""
from Stack_array import Stack

def stack_combine(source1, source2):
    """
    -------------------------------------------------------
    Combines two source stacks into a target stack.
    When finished, the contents of source1 and source2 are interlaced
    into target and source1 and source2 are empty.
    Use: target = stack_combine(source1, source2)
    -------------------------------------------------------
    Parameters:
        source1 - a stack (Stack)
        source2 - another stack (Stack)
    Returns:
        target - the contents of the source1 and source2
            are interlaced into target (Stack)
    -------------------------------------------------------
    """
    target = Stack()
    while not source1.is_empty() and not source2.is_empty():
        target.push(source1.pop())
        target.push(source2.pop())
    while not source1.is_empty():
        target.push(source1.pop())
    while not source2.is_empty():
        target.push(source2.pop())
    return target


def stack_reverse(source):
    """
    -------------------------------------------------------
    Reverses the contents of a stack.
    Use: stack_reverse(source)
    -------------------------------------------------------
    Parameters:
        source - a Stack (Stack)
    Returns:
        None
    -------------------------------------------------------
    """
    array = []
    
    while not source.is_empty():
        value = source.pop()
        array.insert(0, value)

    for index in range(len(array) - 1, -1, -1):
        value = array.pop(index)
        source.push(value)
        
    return

def is_palindrome_stack(s):
    """
    -------------------------------------------------------
    Determines if string is a palindrome. Ignores case, digits, spaces, and
    punctuation in string.
    Use: palindrome = is_palindrome_stack(string)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
    Returns:
        palindrome - True if string is a palindrome, False otherwise (bool)
    -------------------------------------------------------
    """

    stack = Stack()
    palindrome = True
    reverse_index = len(s) - 1
    add = True
    index = 0
    
    while index < len(s) and palindrome == True and reverse_index > 0 :
        if s[index].isalpha() and add == True:
            stack.push(s[index].lower())
    
        elif s[reverse_index].isalpha() and add == True:
            reverse_index += 1
    
        else:
            add = True
    
        if reverse_index < len(s):
    
            if s[reverse_index].isalpha():
                if (not stack.is_empty()):
                    if s[reverse_index].lower() != stack.pop():
                        palindrome = False
            elif s[index].isalpha():
                add = False
                index -= 1
    
        reverse_index -= 1
        index += 1

    return palindrome
  
# Constants
OPERATORS = "+-*/"

def postfix(string):
    """
    -------------------------------------------------------
    Evaluates a postfix expression.
    Use: answer = postfix(string)
    -------------------------------------------------------
    Parameters:
        string - the postfix string to evaluate (str)
    Returns:
        answer - the result of evaluating string (float)
    -------------------------------------------------------
    """    
    stack = Stack()
    tokens = string.split()

    for token in tokens:
        if token in OPERATORS:
            operand2 = stack.pop()
            operand1 = stack.pop()
            if token == "+":
                result = operand1 + operand2
            elif token == "-":
                result = operand1 - operand2
            elif token == "*":
                result = operand1 * operand2
            elif token == "/":
                result = operand1 / operand2
            stack.push(result)
        else:
            stack.push(float(token))
    
    answer = stack.pop()
    return answer

def stack_maze(maze):
    """
    Solves a maze using Depth-First search.
    Use: path = stack_maze(maze)
    """
    stack = Stack()
    path = []
    visited = set()

    stack.push(('Start', maze['Start']))
    visited.add('Start')

    while not stack.is_empty():
        current_point, branches = stack.peek()

        if current_point == 'X':
            path.append(current_point)
            return path

        unvisited_branches = [branch for branch in branches if branch not in visited]

        if unvisited_branches:
            next_branch = unvisited_branches[0]
            stack.push((next_branch, maze[next_branch]))
            visited.add(next_branch)
            path.append(current_point)
        else:
            stack.pop()
            path.pop()

    return None

