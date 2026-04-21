
def bracket_validator(string: str) -> bool:
	overed = ['(', '{', '[']
	fermed = [')', '}', ']']
	tolist = []
	i = 0
	while i < len(string):
		if string[i] in overed:
			tolist.append(string[i])
		elif string[i] in fermed:
			if not tolist:
				return False
			t = tolist.pop()
			if string[i] == ')' and t != '(':
				return False
			if string[i] == '}' and t != '{':
				return False
			if string[i] == ']' and t != '[':
				return False
		i += 1

	return len(tolist) == 0


def main():
    # Valid cases
	print(bracket_validator("()"))         # True
	print(bracket_validator("()[]{}"))      # True
	print(bracket_validator("{[()]}"))       # True
	print(bracket_validator(""))             # True  (empty string is valid)
	print(bracket_validator("hello(hhhh)world{ho}w are"))  #True

	# Invalid cases
	print(bracket_validator("(]"))           # False
	print(bracket_validator("([)]"))         # False
	print(bracket_validator("((("))          # False
	print(bracket_validator("())"))          # False
	print(bracket_validator("{[(])}"))       # False

main()
