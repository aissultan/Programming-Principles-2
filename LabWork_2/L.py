line = input()
brackets = []

for i in line:
    if i == "[" or i == "{" or i == "(":
        brackets.append(i)
    else:
        if len(brackets) == 0:
            print("No")
            quit()
        if i == ")" and brackets[-1] == "(":
            brackets.pop(-1)
        if i == "}" and brackets[-1] == "{":
            brackets.pop(-1)
        if i == "]" and brackets[-1] == "[":
            brackets.pop(-1)

if len(brackets) == 0:
    print("Yes")
else:
    print("No")