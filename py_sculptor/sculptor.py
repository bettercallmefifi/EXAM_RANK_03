def sculptor(s: str) -> str:
    tolist = ""
    i = 0
    p = True
    while i < len(s):
        if s[i].isalpha():
            if p:
                tolist += s[i].lower()
            else:
                tolist += s[i].upper()
            p = not p
        else:
            tolist += s[i]
        i += 1
    return tolist

def main():
    # Basic case
	print(sculptor("Hello world"))
	# "hElLo WoRlD"

	# With punctuation
	print(sculptor("Hello, world!"))
	# "hElLo, WoRlD!"

	# With numbers
	print(sculptor("123abcDEF"))
	# "123aBcDeF"

	# Mixed characters
	print(sculptor("a-bC-dEf-ghIj"))
	# "a-Bc-DeF-gHiJ"

	# Edge cases
	print(sculptor(""))
	# ""

	print(sculptor("12345"))
	# "12345"

	print(sculptor("A"))
	# "a"

	print(sculptor("ab"))
	# "aB"

main()