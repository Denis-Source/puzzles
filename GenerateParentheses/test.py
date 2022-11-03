import pytest

from GenerateParentheses.solution import Solution

TEST_CASES = [
    (1, ["()"]),
    (2, ["()()", "(())"]),
    (2, ["(())", "()()"]),
    (3, ["((()))", "(()())", "()(())", "(())()", "()()()"]),
    (3, ["((()))", "(()())", "()(())", "()()()", "(())()"]),
    (4, ["()()()()", "()()(())", "()(())()", "()(()())", "()((()))", "(())()()", "(())(())", "(()())()", "(()()())",
         "(()(()))", "((()))()", "((())())", "((()()))", "(((())))"]),
    (8, ["(((()))()(()))()", "()(()()(((()))))", "(())(())(()())()", "(())()()(())()()", "(((((())()()))))",
         "(()()((()(()))))", "((((()()()()))))", "((((())((())))))", "(())((())()(()))", "()()()()(())()()",
         "()()(())((()()))", "(()()(((()()))))", "((()()))(()()())", "((((())()))(()))", "()()((((()))()))",
         "((())(())()()())", "((((()()))())())", "(())(())((()))()", "(()(()()())(()))", "((((())())()()))",
         "()((()(())))(())", "((())((()(()))))", "()()((()()())())", "((()(())(()())))", "()((()))()()(())",
         "((())(())(()()))", "()(()(()))(())()", "()((((()())())))", "(()()()()())(())", "(((()(()))(())))",
         "()(()(()))(()())", "((()(()())))()()", "((()))(()()(()))", "(()()(())())(())", "(((())(()))()())",
         "(())()()((()()))", "((()(())()())())", "()()()(((())))()", "(()((()))()()())", "((())()((())()))",
         "(())()()(((())))", "()(((())(()())))", "()(((())())(()))", "(())(()())((()))", "((())(()()())())",
         "()(()())(()()())", "(()()())()(()())", "(()((()())))()()", "((((())()))())()", "(()((())()))()()",
         "(((())()(())))()", "(()()(())(()))()", "(())()((())()())", "((((())(()()))))", "(()()((()))()())",
         "(()())()(())(())", "(())(((())()))()", "(((()())()))()()", "()((()(())))()()", "(()((())))()()()",
         "(())()((()))()()", "(()(()(()()))())", "()(())(()((())))", "()(()()((()())))", "()(((((())))))()",
         "((((()))()())())", "((()()(()))(()))", "(()((()(()))()))", "((((())))(())())", "((()((())(()))))",
         "(((()())()()()))", "(()((()(()))))()", "()()()(()()())()", "(())((())()())()", "()(((()()())))()",
         "()(((())))(())()", "((()(())()(())))", "(((()))(()()))()", "((()))()(()()())", "((((()(())()))))",
         "()(()())((()))()", "(()())(()())(())", "(((())()()()()))", "((()((())))()())", "(((())))(((())))",
         "(((()())((()))))", "(()()(())()()())", "()()(()(()))(())", "()(())((()())())", "()((())()((())))",
         "((((()))(()())))", "(()(()()))((()))", "()(()(()()()()))", "((())()((()))())", "(())(()(()()()))",
         "((())(())((())))", "(()((()))(())())", "((((()())))()())", "()(()()(()())())", "(()(()))(())(())",
         "(((()(()))))(())", "((())(()())())()", "()((()())()()())", "((()(())(())))()", "(())()(())()()()",
         "(())(())()()()()", "((((())())))(())", "()(()(())()(()))", "()()()(()((())))", "(())(())(((())))",
         "((()))()(())()()", "()(())(((())()))", "(())(())(()()())", "((((())()())))()", "(()(()())()()())",
         "(())()((()()()))", "((()())(((()))))", "()((())(()))()()", "()(()()((())))()", "()((())(())(()))",
         "(((())()((()))))", "((())(()))((()))", "(()(()()()()))()", "()(()(())(())())", "(((()(())())))()",
         "()((()))((()()))", "()((()((()()))))", "((((()(())))()))", "((()()))(((())))", "((())(()()(())))",
         "(((()()))()()())", "()((()())())()()", "(()(((()))(())))", "()(()())(())(())", "()(((()))(()))()",
         "(())(()()()()())", "((()(())())(()))", "(()()((()()())))", "(()(((())))()())", "(()()()()((())))",
         "((()))(()())(())", "(((())((())))())", "()(())()()(()())", "((((()))))((()))", "((())()()()(()))",
         "(()(()))()(())()", "((((())())))()()", "(()()((())()))()", "((()()))(())()()", "()()((()()()))()",
         "()((((())()))())", "((((()()())))())", "()()()((((()))))", "()(()()())(())()", "((()(()())(())))",
         "()(())()()(())()", "(((()))()()(()))", "(()(()((())())))", "((()()())())()()", "()(()()(()()()))",
         "((())(()())()())", "(()()(())((())))", "()()()()((())())", "()()()(()())()()", "(())()()(())(())",
         "((()((()(())))))", "((((()())())()))", "((()()()))()(())", "((((()()))(())))", "((((()))))()(())",
         "(((()()((())))))", "()(()())()(()())", "(())()((()())())", "()()(()())(())()", "((())(()()()))()",
         "()((())(()(())))", "(()(((((()))))))", "(()())(()((())))", "(()(()()(()))())", "(()((())()()))()",
         "(()())((()()()))", "((()()((())))())", "()(((()(()))()))", "()(()()()(()))()", "((((())(())))())",
         "(()(()))()(()())", "()((())((())()))", "(()(()())())(())", "((())(()(())))()", "(()(((()()()))))",
         "((((()))()()))()", "((()((())))(()))", "(()()(()()())())", "()()()((()))()()", "()((()()(()))())",
         "((()()())()(()))", "((((()())()))())", "(())()((())())()", "((())((()())()))", "(()((()()()())))",
         "(((())))(()(()))", "(()((())(()))())", "()(())()((()()))", "()(((()()()())))", "((()(())()))(())",
         "(()()(())()())()", "((()))()(())(())", "((((()())())))()", "(())(()()()(()))", "(()()()()()())()",
         "(()((()))()())()", "((((()())()())))", "()(((()()())()))", "(((())(())))()()", "(()(((()))()))()",
         "()()((()()))()()", "(()(((()))()()))", "(()(()(()()())))", "(((((()))))())()", "(()((()()()))())",
         "((()))((())())()", "(()((()())(())))", "(()(()()))()(())", "(((()(()))()()))", "(()((())())(()))",
         "(()())(())((()))", "((((())()))()())", "()(())()(()(()))", "(()(()(()))())()", "(()()(()))(()())",
         "(()()((()))(()))", "()(()((()()())))", "(()(())(()))()()", "(()()()(())())()", "()()()((()())())",
         "()()(())()((()))", "((((())))())(())", "((()))()((()()))", "(((((()()))())))", "(()(())()())()()",
         "()()((()))((()))", "(()((()()))())()", "(()())()((())())", "((()()()(()())))", "()((())()())(())",
         "(()(())(())())()", "(())((()()(())))", "(()(((())))(()))", "(()(()()()()()))", "(())(((()())()))",
         "(((()((())()))))", "(((((())())())))", "(()((())))(()())", "()()(((())))()()", "()((())((())))()",
         "(())((()()))()()", "((()())(()))()()", "(()(())()())(())", "(((()((())))()))", "(()(()()))()()()",
         "(((()(())))(()))", "((()()())((())))", "(()(())())(())()", "((())())()()()()", "(((())()))(())()",
         "((()(())(()))())", "(((()()()())()))", "(((((())))))()()", "(((())((()()))))", "(()(()())(()()))",
         "(()())((())()())", "((()(()(())())))", "()(()((()(()))))", "(((()))(())(()))", "(()()((()())))()",
         "(()(()()()))()()", "()((()))()()()()", "()(())((())()())", "()(())(()())(())", "((())((()))())()",
         "()()(()(())(()))", "(((()()()))())()", "()(()())(()())()", "(((()(()()))()))", "((()()())())(())",
         "((()))((()()()))", "((())((())()()))", "(()(()()()(())))", "(()((())))((()))", "((())())((()()))",
         "(()()(((())))())", "(()(((())(()))))", "(()()(()(()))())", "(()((())()(())))", "()(()(()()))()()",
         "()()((()((()))))", "(()()(())(())())", "(()()()()(())())", "()()()((())())()", "((()(()(())))())",
         "()((()))(()(()))", "()()(()(())()())", "()((())()())()()", "()(())(()()())()", "(())((()()))(())",
         "(()()())(())()()", "(((()(())()())))", "((())()(((()))))", "((()()(()))()())", "(())(()(()())())",
         "()((()())(())())", "(()((()())()))()", "(((()())))()()()", "(((())()()))(())", "((()())())((()))",
         "((()))(((())))()", "(())((()))()(())", "((()())())()(())", "((())()(()))()()", "(()((()))()(()))",
         "((())((()))(()))", "(())(()()())(())", "(((()())(())))()", "((((())(()))()))", "(()(()))()()()()",
         "(())(((((())))))", "()((()))()(()())", "()((()))(((())))", "((())())(())(())", "(()(()))(()()())",
         "()()((()))(()())", "()(()((())())())", "()()(((())(())))", "((()()(((())))))", "()(()(())()()())",
         "(())((((()))()))", "(())((())(()))()", "(((()())(()())))", "((())(()())(()))", "((()(()))(())())",
         "()(()()())(()())", "()(()((())))(())", "((((((()))()))))", "((((()()(())))))", "()()(())((())())",
         "(()()((())())())", "(()(()((()))()))", "((()()())(())())", "(()(()(()())()))", "()(()())()((()))",
         "(()())()()(()())", "(()()()(())()())", "()()(((()))())()", "()((())()(())())", "((()(()()())()))",
         "((((()))))(()())", "(())()()()(()())", "(()()()((()))())", "((()(()(()))()))", "(()(())((()())))",
         "()(())((()()()))", "(()())(((())))()", "((((())))((())))", "()()((((())())))", "(((()()())()))()",
         "()()()()(())(())", "((()())()())()()", "()(()(()))()()()", "(()()(()((()))))", "()((()()))((()))",
         "()()(((()())()))", "((())(()()()()))", "()()()(())(()())", "()()()()()(()())", "()(()((()))())()",
         "()(((())))(()())", "(()(()()))(())()", "()(()(()))()(())", "()(()((())(())))", "()()()((()()()))",
         "()()((()())()())", "()(()()(()))(())", "()()((()()()()))", "(((()()))())()()", "(()()((()())()))",
         "(((()))(())())()", "()()(())(((())))", "()(()())()()()()", "()(()(((()))()))", "(((()(())()))())",
         "()(()()(()()))()", "(()((()(())())))", "((()(((())()))))", "(()((())(())()))", "(()(()))()()(())",
         "((())(())(()))()", "(()(()()(()())))", "(((())())(())())", "((())((()()))())", "((((()(())))))()",
         "((()(()()))(()))", "()()()(())(())()", "()(()(((())())))", "(())()(()())(())", "(())(()()(()()))",
         "()((())()()(()))", "((((())()()())))", "()()((()(()())))", "()()(((((())))))", "((()((()))(())))",
         "()(()(((())))())", "(((()(()))())())", "((())(((()()))))", "()()()((())(()))", "()((((())())()))",
         "((((())))()()())", "(()(()))((()))()", "()(()(())())()()", "((((()())))(()))", "(()(()(()())))()",
         "(()())(((())()))", "(())(((())()()))", "(((())))()(())()", "(((()()()()))())", "(())(((())))(())",
         "((()()))((())())", "()(())((()()))()", "()(()(()(())()))", "()((())()()())()", "(((()))()()())()",
         "(())(()()(()))()", "()((()()))()()()", "(((()(())))())()", "(((()))(()))()()", "(()()())((())())",
         "(())(()((()())))", "(((((())()))()))", "(())((((())))())", "(()()()()())()()", "(()())(()()())()",
         "(())(()((()))())", "(())()(()()()())", "(())((()(()))())", "((()))()(()())()", "(()(())())(()())",
         "(((()()()(()))))", "((()()()())())()", "()(((()))(()()))", "((()((())()))())", "(((((()())()))))",
         "()((()))(())(())", "(()()()(())(()))", "((())()())()()()", "(((()((()))())))", "()(((()))()())()",
         "(())(()(()(())))", "(())((()()()))()", "()(((((()))())))", "((()))(())()()()", "((()())()((())))",
         "(()(()))(())()()", "()()(()(()(())))", "()((()(()()))())", "()((())(((()))))", "()((()()(())))()",
         "()()(())(()())()", "((())())()(())()", "()()()(()(()()))", "(()()())()()()()", "((()(()()(()))))",
         "()(()()(()))()()", "(()((()()())))()", "((()(()))()()())", "()(()()()())()()", "()((()(())(())))",
         "(()()(()))(())()", "()(((())()())())", "()(()(()())()())", "((((()))((()))))", "(((()()())()()))",
         "(()(((())))())()", "(()())(())()()()", "((()))()()((()))", "()((((())(()))))", "(()())((())())()",
         "((()))((()())())", "()()((())(())())", "()()()(()(()))()", "()(())()()()()()", "(())(((()()())))",
         "((()((()))))(())", "((()))(())(()())", "()(())()((()))()", "(())(())()()(())", "(()((((()))())))",
         "(()()()()(()()))", "((())())(()(()))", "((()(()())()()))", "(())()()((()))()", "(()(())()()(()))",
         "(())()()()((()))", "()(((())())()())", "(((())))()()(())", "()((()))((())())", "((()()))((()()))",
         "()((((()))()()))", "((())()())((()))", "()(((())())())()", "(((((())(())))))", "(())(((()))())()",
         "()()()(())((()))", "()((()(())()()))", "(((()))(()())())", "(()((((())()))))", "()((()()()))()()",
         "()()(())((()))()", "(()((((()())))))", "((()(()(()))))()", "((((()()()))))()", "(((((())))))(())",
         "(()(()))()((()))", "()((()()())()())", "()(()(())(()))()", "(()(((()))))()()", "((()(()))((())))",
         "(()()())((()))()", "(()()(()()(())))", "(())()((())(()))", "((()()()()())())", "(())()(()((())))",
         "(((())())(()()))", "((())(((())))())", "(()(())((())))()", "((((()()))()()))", "()()()()((()()))",
         "()(((()())()))()", "((()(()())()))()", "(()())()((()))()", "((())(())()(()))", "((())()()()()())",
         "()(((()())(())))", "((())(()()))(())", "(()())(()())()()", "(())()(((())()))", "((()((())()())))",
         "(()(())(()()))()", "(())()(())()(())", "(()(()))(()())()", "(())(()((())()))", "((()))()(()(()))",
         "((((())))(()))()", "((())())()(()())", "()((())())(())()", "()(()(()(()))())", "(((()(()))()))()",
         "(())(()(()))()()", "(()(()())(())())", "(()()((())(())))", "()()()()(((())))", "(()(())(())(()))",
         "()((()()())(()))", "()((()(()))()())", "(((()())())(()))", "(()(()))(((())))", "()(((()()))()())",
         "()(()(())(()()))", "(((()((())))))()", "()(())((()))(())", "(((((()()())))))", "(())()(()())()()",
         "(())(()())()()()", "()(((())()))()()", "()()(()())()(())", "((()(())))((()))", "((()(((())))()))",
         "(())(()()())()()", "(((())()()())())", "((())()(()))(())", "((())(()((()))))", "(((())((())())))",
         "(()()(((())())))", "()()()()(()())()", "()()(()(((()))))", "(())((()()())())", "(()()(()))((()))",
         "(())()(()()(()))", "((()))(()(()()))", "()()((()))()(())", "(())((()))(()())", "(()((()()())()))",
         "()(((())()()()))", "(((())()())()())", "((()((((()))))))", "()()(()())()()()", "(()())()()()()()",
         "((()())((())))()", "()()((()))(())()", "((((((())))))())", "(()()())(((())))", "(((()()))(())())",
         "(()())(()(())())", "()(((())()))(())", "(()((())()))(())", "((()()))()()()()", "(()())(())()(())",
         "(())()()(()())()", "(((())))(()()())", "(((()((()())))))", "()(()((()))()())", "()()(((()()())))",
         "(()())((())(()))", "(()(()()(())()))", "(())(()()(())())", "()()(()(())())()", "(((())(()))(()))",
         "((()()()))((()))", "(((()(())(()))))", "(((((((())))))))", "(())((()))(())()", "(((()()())(())))",
         "(())((((()()))))", "((()))(()((())))", "(())(()(()))(())", "(((((()))())()))", "()()((()(()))())",
         "((())())(()())()", "(((())(())()))()", "(((()))(())()())", "()((()(((())))))", "((()()()))()()()",
         "()((()((())())))", "(())(((()))(()))", "()((()()(()())))", "()(((())(()))())", "(()(()()())())()",
         "((()(())))(())()", "((()()(()))())()", "(()()()()(()))()", "()((())())()()()", "(((()))()())(())",
         "((())()(())())()", "()()(((())()))()", "((((())())()))()", "(((()(((()))))))", "(((())()())())()",
         "()(((()(())))())", "()(())(())()()()", "((()()(())(())))", "(())()(())((()))", "((((())())())())",
         "((()))(()()())()", "(((()()(()))))()", "(((())(()))())()", "(())()()()(())()", "()((()(())()))()",
         "(((()())))((()))", "(((()))()(())())", "(((()()())())())", "((((())(())())))", "((()()(()())))()",
         "((())(()()))()()", "((()()())(()()))", "()((())((()))())", "((((())()()))())", "(((())(((())))))",
         "(((()()())))(())", "(()((()()))()())", "()()(((())))(())", "()(())(((()))())", "()((()())((())))",
         "((((((()))))))()", "((()(()())))(())", "(()(())()(())())", "()((()()())())()", "()(())(()()()())",
         "(()(()(())))()()", "()((()()()))(())", "()(()()()((())))", "(((()))(()()()))", "(((()()()))()())",
         "((())()()())()()", "((())()())(()())", "((()())())(()())", "(()())((()))()()", "(((((())())))())",
         "(()())()(()()())", "((()((())())()))", "((()))((()()))()", "(())()()(()()())", "(()((())())())()",
         "(()())()(()(()))", "(())(())()(())()", "((())(())(())())", "(())(()(())()())", "((())(())()())()",
         "(()()(()()))()()", "((()))((((()))))", "((()(()()()))())", "((()))(()())()()", "()()(())()()()()",
         "(()())()(())()()", "(()()(())())()()", "()(()(()))((()))", "((()()(())))()()", "()()(((()))(()))",
         "(()())(((()))())", "((())()()()())()", "()(()(())((())))", "(())((()(())))()", "(())(())()((()))",
         "(()(()(())))(())", "((()))()()()()()", "((((()))(())))()", "(()()(()))()(())", "(()(()(((())))))",
         "(((())())((())))", "(()(()()))(()())", "()()((()()(())))", "(())((((()))))()", "()(()()()())(())",
         "((()()()()()()))", "()((())((()())))", "()(()())((())())", "(()(()(())()()))", "((((((()))))()))",
         "(((()())))(())()", "()()(()(()))()()", "(((())(()())()))", "()(()()())()()()", "((())()()(()))()",
         "(()()()())(())()", "()()(()()(()()))", "()((()))((()))()", "(((())()))()()()", "()()(()()())()()",
         "(()())()((()()))", "()()((())()())()", "((()))((()))()()", "()(()(((()))))()", "(((()())()()))()",
         "(((()())))(()())", "(())((()())(()))", "(((())(())()()))", "((()))(()(())())", "(()(()()((()))))",
         "((()())(())())()", "(())(((()()))())", "()(())()((())())", "(((())()(())()))", "(((())(()(()))))",
         "(()(()()(())))()", "((()(()()))())()", "(()()()(()))(())", "(((()())())()())", "()()((())()()())",
         "((()())(()()()))", "((())((()())))()", "()((())(()()()))", "(((()())()())())", "(((())))((()()))",
         "()((((()())))())", "((())()()(()()))", "(()(())(()()()))", "((()((()))()()))", "((()()((()))))()",
         "(()()())()((()))", "((((()))())()())", "(((())()))()(())", "((()((()())))())", "((()))()((()))()",
         "((()))((())()())", "()(()(()()))(())", "(()((())((()))))", "((()()()()))()()", "(())(())((()()))",
         "(()(())())((()))", "()((()()((()))))", "()(((()((())))))", "(((())))()(()())", "()()()((()()))()",
         "(()(())(())()())", "()(())(())(())()", "(()((()())())())", "()()(()())((()))", "()((()(()(()))))",
         "((())(()(()))())", "()(((((())()))))", "()((()()))(()())", "(()(()))((()()))", "(())()(((())))()",
         "((()((()()()))))", "(()((()(())))())", "(()(((())())))()", "(((()))()((())))", "()()()()(()(()))",
         "(((((())))(())))", "()(()()(()(())))", "()()()(()()(()))", "(())(())(())(())", "((((()))())(()))",
         "()(())()(())()()", "((())()(()(())))", "(()()(()()()()))", "(()((()()(()))))", "((()))((()(())))",
         "(((())))(())()()", "(()()(()()))(())", "(()((()(()()))))", "()()((()()))(())", "((((()())(()))))",
         "(((()))())((()))", "((((()))()))(())", "()(())(())()(())", "((((((())())))))", "((()(())())()())",
         "((()(())))()()()", "((())())()((()))", "()((())(())()())", "(()()((()()))())", "(()())(()(()()))",
         "(((()()))()(()))", "((())(()(()())))", "((()()()((()))))", "()()()()()()(())", "()(()(()()()))()",
         "()((((()()))()))", "(((())()())(()))", "()(()(()((()))))", "(((())())()())()", "()(())()(()()())",
         "(())()()()()()()", "()((()()))(())()", "()()()((()(())))", "()(()(())())(())", "(())()(())(())()",
         "((()))(())()(())", "()(()(()(())))()", "()()((()))()()()", "(()(())(()))(())", "()((()())())(())",
         "()(((()()))(()))", "()((()((()))))()", "((())()(())()())", "(()((()))())()()", "()()()(((()))())",
         "()()(()())(()())", "()()((())())(())", "()(())()(())(())", "()(()(()()(())))", "()((((()(())))))",
         "(()((((())))()))", "(((()))((()))())", "((())((())))(())", "(())((()))((()))", "()()()()()()()()",
         "()((((())))(()))", "((())()(()()))()", "()(((())))()()()", "((())((())()))()", "((()(((()))))())",
         "()((())(()))(())", "()(()((()())))()", "((()()()())(()))", "(((((()())))))()", "(()()(((()))()))",
         "()(()()()()())()", "((())(())())()()", "()()()()()(())()", "((()(())))(()())", "((()(())))()(())",
         "(()(((())())()))", "()()()(())()(())", "((()(())((()))))", "(((()()))(()()))", "((()(()))()(()))",
         "((()())()()(()))", "(())(((()))()())", "(()()()())((()))", "(((()(()())))())", "(((()(())())()))",
         "(())()(()(()()))", "((())()())()(())", "(()()()())()(())", "()()(()()(())())", "()((()()()(())))",
         "()(()((()()))())", "(((()(())))()())", "(()((())(()())))", "()(((())((()))))", "((((()(()())))))",
         "()(((())))((()))", "(((((()))()))())", "((()()((()))()))", "()(()())((()()))", "(())((())(()()))",
         "((()()(())))(())", "((()())()(())())", "()(())(()(()()))", "()(()(())()())()", "((())()(())(()))",
         "()((()))(()())()", "(((())()()(())))", "((()())()(()))()", "(((()(()(())))))", "(()()()()()()())",
         "()((((()()()))))", "()(((()))()(()))", "((())())(()()())", "(((()(()))))()()", "()()()(())()()()",
         "()()(((())()()))", "((()()()())()())", "(())()((()(())))", "(((()())()))(())", "()()(()()((())))",
         "(()((()()))(()))", "(()()())(()()())", "()(((((()())))))", "((())(()))(())()", "((()()()()(())))",
         "()(((()))())(())", "((()))(())(())()", "((())()()())(())", "(())()()((())())", "((()((()))())())",
         "(())((()(())()))", "()()()()(()()())", "()(())((()(())))", "(()()((())))()()", "((()()(()(()))))",
         "(())(())(()(()))", "(()()()(()))()()", "(((())(())(())))", "(()(()((())))())", "(())(((())(())))",
         "()(())(()(())())", "((()))()()(()())", "((()((()()))))()", "((()))((())(()))", "()((()())()(()))",
         "((())(()))()()()", "((()()))(()(()))", "(((((()))))()())", "((()()(())()()))", "(((()()()())))()",
         "()(((()(())())))", "((())()())(())()", "((()()((())())))", "(((())(()()))())", "(((()()(())))())",
         "()((())(())())()", "()(()()((()))())", "((((()))()()()))", "(()()()()()(()))", "(()()()(()())())",
         "(()(((()()))))()", "(((())())()(()))", "(((()))())()(())", "(()()((())()()))", "((()()))(()())()",
         "(())(((()())))()", "(()((())()())())", "(()(()(()))()())", "(()((())())()())", "(()(()()()())())",
         "((()()(())())())", "(()(()(())(())))", "(()())()()((()))", "(()()())(()())()", "()((((())()())))",
         "()(())(()())()()", "(()()(()())()())", "(((()())())())()", "()()(()((()())))", "(()(()()())()())",
         "(()(()()()))(())", "()(())()()()(())", "(((()))((()())))", "((()))()()(())()", "(())((())(())())",
         "()(()()())()(())", "(()((((()))))())", "()((())())((()))", "((()(())()()()))", "()(((()())()()))",
         "()(()())()(())()", "(())(())((())())", "((()((())())))()", "(((())))()()()()", "((((()((()))))))",
         "(((((())))())())", "(()())((()(())))", "(()((()))(()))()", "()((())()(()))()", "(((((()(()))))))",
         "(((())))(()())()", "((())((())())())", "(((())())(()))()", "((()(()))()())()", "((())())(())()()",
         "(())((()(()())))", "(()()()())(()())", "((((()))()(())))", "((((()())))())()", "()(())()()((()))",
         "()(())(())((()))", "(((()()))(()))()", "(()((()())))(())", "()()((())()(()))", "((((((())))())))",
         "((()(((()())))))", "(()(())()()()())", "(((()())))()(())", "(()(()(()(()))))", "((()()())()()())",
         "((()((()()))()))", "(())()()()()(())", "()()((())(()))()", "((())()((()())))", "((()()()()))(())",
         "((()))(((()))())", "((()((()())())))", "()(())((())(()))", "()(((()(()))))()", "()()(()(()()()))",
         "(()()(()(())()))", "()()(()()()(()))", "(()(()((()()))))", "((())())((()))()", "()(((())))()(())",
         "((()()()(())))()", "((()(())(())()))", "(()())((((()))))", "(()())(())(()())", "(((((())()))))()",
         "((()())(()()))()", "()()((())((())))", "((((()))())())()", "(((((()))(()))))", "(((())()()()))()",
         "()((((()))())())", "(())()(((()))())", "(()(()())(()))()", "(((())()(()())))", "((((()()))()))()",
         "(((()())(())()))", "()()((((()()))))", "(()(())(()(())))", "()()()()()((()))", "()()(((()())))()",
         "((((()()())())))", "()()(()()()()())", "((())(((())())))", "((((())())(())))", "(())()(())(()())",
         "()()(()()()())()", "((())(()(())()))", "((((((()()))))))", "()(())()(((())))", "()(()((()())()))",
         "()()(())(()()())", "((((()()()))()))", "(((((())))()()))", "((()()))()(()())", "((()()(())()))()",
         "()(()(()())(()))", "()(())(())(()())", "(()())(()()()())", "()()(()(()()))()", "()(((()))(())())",
         "(((())))(())(())", "()(())(()(()))()", "(()(((())()))())", "(()(()))(()(()))", "(((((()))())))()",
         "((()())()()())()", "((()))(())((()))", "(()(()())((())))", "()()()()((()))()", "(()()(()))()()()",
         "()((()(()())))()", "((()()())(()))()", "(((()()))((())))", "(()(())()((())))", "(((()))())(())()",
         "(())(()(()()))()", "((()(((()))())))", "((((())))(()()))", "((()())(()())())", "(((())((()))()))",
         "()((()()()()))()", "((())()(()()()))", "()((()())(()))()", "(((()()(()))()))", "()(((()())))()()",
         "((()(())()()))()", "((((())(()))))()", "(((())())())(())", "()()((()(())()))", "(()()())((()()))",
         "((()())((()))())", "()(((()))())()()", "((()(()((())))))", "(((())()(()))())", "()((()(()))())()",
         "(()())(()()(()))", "(()()((())))(())", "((()())(())(()))", "()(((()))()()())", "()((()(())())())",
         "((()())()()()())", "((()(()(()()))))", "(((((()())))()))", "((((()))()))()()", "()(((()()))())()",
         "((())())(((())))", "(()(((()())))())", "(())()((()()))()", "(())((())((())))", "((()(((())))))()",
         "(()()())()(())()", "(()(())())()()()", "((()())())()()()", "((()(())()))()()", "()((()(()())()))",
         "()(((()())())())", "()()()(()()()())", "((((()(()))())))", "((()))((()))(())", "()()(()()())(())",
         "()((()()()()()))", "()((()(()))(()))", "(((())))()((()))", "()(()()((())()))", "(()()()(()(())))",
         "()((())(()()))()", "(((())(()())))()", "(()(((()))))(())", "()((())())()(())", "(((((()()))))())",
         "()()()((())()())", "()()(()()(()))()", "((()))(((())()))", "(()()((((())))))", "()((()))()(())()",
         "((())()(()())())", "()(((()(()()))))", "(((()())(()))())", "()()(()((()))())", "(((()(()()))))()",
         "(()()()(()()))()", "()()(((()))()())", "()()(())(()(()))", "(((()())()(())))", "(((()))((())()))",
         "((((()()))))(())", "((()))()((())())", "()(()())()()(())", "((()()))((()))()", "()(()((((())))))",
         "(()())()()()(())", "((()()))()((()))", "(()()())(()(()))", "(()())()(((())))", "(()()((()))())()",
         "(()((()))())(())", "((()((())))())()", "((((()))(())()))", "(((()()())))()()", "(()(()((()))))()",
         "(())(())()(()())", "(()(()())())()()", "(())((())())(())", "(()())(())(())()", "()((((())))()())",
         "(((((()))))(()))", "(()(()(())())())", "(())(((())))()()", "()(((())()()))()", "(()())()(()())()",
         "(())(()())()(())", "((())((()()())))", "()()(()((())()))", "((())((())(())))", "(()()(())()(()))",
         "(((()(()()()))))", "((())((()))()())", "()(((()()(()))))", "((()))(()(()))()", "(()(())()(()()))",
         "()((()()(())()))", "(((()((()))))())", "(()(()())()())()", "(()())()()(())()", "(((()()()()())))",
         "(()(((()()))()))", "(((((()))()())))", "()(()((())()()))", "(()())((()))(())", "()()()(()())(())",
         "(()(())((()))())", "((()()()))(())()", "()((((()()))))()", "()((())()(()()))", "(()()()((())()))",
         "()()((())())()()", "()(())((()))()()", "()((())(()())())", "(()()()())()()()", "(()()(((()))))()",
         "((())((())))()()", "((())()()((())))", "()(()(()())())()", "(()((())(())))()", "(())(()())(()())",
         "(()()())()()(())", "(((())()))(()())", "(())(()()((())))", "((()((()))()))()", "(())(())(())()()",
         "(()()()(((()))))", "()(()()())((()))", "((()()()(()))())", "(((()()()))(()))", "(((())(())())())",
         "()((((())())))()", "()()(((()()))())", "()(())(()()(()))", "()()(((()(()))))", "(()(((()())())))",
         "(((())(())))(())", "(((()()(())())))", "()(()()()(()()))", "((()))()()()(())", "(()((())))()(())",
         "((())(()))(()())", "(()(()))((())())", "(((()))(()(())))", "((()((()))))()()", "(())(()(())())()",
         "(()()()(()()()))", "((()(()()())))()", "()((()))(()()())", "()((()(()()())))", "()(()((()))(()))",
         "()(()()(())()())", "()(((((()))))())", "(((()(()())())))", "()((()())(()()))", "()(()()(())())()",
         "(()())((()())())", "(()(()(()))(()))", "(((()))())(()())", "(((())))((())())", "()()(()(()())())",
         "(())((()())())()", "()(()())(())()()", "((((()))))(())()", "()()((()())())()", "()(()(()()())())",
         "(()((())))(())()", "((()())(())()())", "(())()((((()))))", "((()())(()))(())", "(()())(()(()))()",
         "(())()((()))(())", "()()(())(())()()", "((())(())())(())", "(()()()((())))()", "()()((((())))())",
         "()()()(((())()))", "()(())((((()))))", "(((())((()))))()", "()(((())()(())))", "()((()()))()(())",
         "(()((()())()()))", "((()))(((()())))", "((())())((())())", "(((((())))()))()", "(()()()((()())))",
         "(((())())()()())", "(())((()()()()))", "((()(()()()())))", "((()())((())()))", "(((())()))((()))",
         "(()(())(((()))))", "(((()))((())))()", "(())(((())())())", "((()))()(((())))", "()()()((()))(())",
         "(())()()(()(()))", "(()(()())()(()))", "((()(()))(()()))", "(((()))()()()())", "((()()))(())(())",
         "(((()))(((()))))", "(((()))()(()()))", "()(((())(())()))", "((((())))()(()))", "((())((((())))))",
         "((()()()(())()))", "()(())()(()())()", "()((()))()((()))", "()()(())()(()())", "((()(()))())(())",
         "(())(()())(())()", "(())(()(((()))))", "()((()((())))())", "()(()()()(())())", "()(()()(())(()))",
         "()()((()(())))()", "((((()))(()))())", "(())(()(())(()))", "()(((()()()))())", "((((()()))))()()",
         "((()())()(()()))", "((()()()()()))()", "(())(((()(()))))", "((())(()))()(())", "()((((((()))))))",
         "()()((()())(()))", "(()(())(()())())", "((())())()()(())", "()(((((())))()))", "((()())((()())))",
         "()(((())(())))()", "((()()(()()))())", "(()(((()(())))))", "(((())))((()))()", "(()()(())(()()))",
         "(()(())((())()))", "((((()))))()()()", "(()(()(())()))()", "()(()(()(()())))", "(((()()))()())()",
         "()((((())))())()", "(()((((())))))()", "()(()()()()(()))", "((((())()())()))", "(()((()))(()()))",
         "()()((((()))))()", "()(())((())())()", "()(()(((()()))))", "((((())))())()()", "((()()(()())()))",
         "(()(((()))())())", "()()()(()(())())", "(((()()))())(())", "(())((()())()())", "()()(((())())())",
         "(()(())()(()))()", "(())((((())())))", "((())(((()))))()", "(((())())())()()", "(())((())())()()",
         "((()(()()))()())", "(())()(()(()))()", "(()(((())()())))", "(()()(()())())()", "()((()()()())())",
         "(())((()((()))))", "(()((())()()()))", "()((()))(())()()", "(((())()()))()()", "(())(()((())))()",
         "((())()((())))()", "((()())(()(())))", "()(((()))((())))", "((()()((()()))))", "()(()((())))()()",
         "(())(()()()())()", "()()(())(())(())", "((((())()(()))))", "()((())()()()())", "(((()()(()()))))",
         "()(())(((())))()", "(())()(()()())()", "((()()(()()())))", "((()(()))())()()", "()()(())()()(())",
         "()()()(((()())))", "()((((()))))(())", "((((()(()))))())", "()(())(((()())))", "(())()(()(())())",
         "()(()()()()()())", "()((((()))()))()", "(()(())()()())()", "((()()())()())()", "(((()))())()()()",
         "((()(())())())()", "(()()(()(())))()", "()((()())()())()", "(()((()))((())))", "()(()())(((())))",
         "()(()((())()))()", "()()(()((())))()", "()((((()))))()()", "(()()())(())(())", "(()()(()())(()))",
         "(()(())())()(())", "((())()()(())())", "((()(()))(()))()", "((()()))()()(())", "()()(())()(())()",
         "(()()(()()()))()", "((()(()())())())", "(())((())()()())", "((((())))()())()", "(((())(()()())))",
         "(()()(()(()())))", "((()()))()(())()", "()((()((()))()))", "((()())()())(())", "()()((())(()()))",
         "(((()))()())()()", "()(((()())))(())", "()((((()))(())))", "(()())((()()))()", "((())(((()))()))",
         "(((()))(()))(())", "(()((()((())))))", "((()()()))(()())", "(())((()))()()()", "()(()())(()(()))",
         "()((())())(()())", "((()())())(())()", "((()))(()()()())", "(())()(((()())))", "(()())(((()())))"]
     )
]


@pytest.mark.parametrize("n, expected_result", TEST_CASES)
def test_solution(n, expected_result):
    assert set(Solution.generate_parenthesis(n)) == set(expected_result)
