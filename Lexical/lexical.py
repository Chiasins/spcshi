import re

keywords = ['if', 'do', 'while', 'for', 'else', 'int', 'float', 'double', 'include']
operators = '+-*/%='

with open("example.txt", 'r') as file:
    for line in file:
        words = re.findall("[a-zA-Z0-9_]+|[+\-\*=%]", line)

        for word in words:
            if word in keywords:
                print(word, "is a keyword")
            elif word in operators:
                print(word, "is an operator")
            elif word[0] in "0123456789":
                print(word, "is an invalid identifier")       
            else:
                print(word, "is an identifier")        
