def is_palindrome(s: str) -> bool:
    p = ""
    i = 0
    while i < len(s):
        if s[i].isalnum():
            p += s[i].lower()
        i += 1
    return p == p[::-1]

def main():
    # Valid cases
	print(is_palindrome("madam"))                    # True
	print(is_palindrome("racecar"))                   # True
	print(is_palindrome("A man, a plan, a canal: Panama"))  # True
	print(is_palindrome("No 'x' in Nixon"))           # True
	print(is_palindrome(""))                          # True
	print(is_palindrome("a"))                         # True

	# Invalid cases
	print(is_palindrome("hello"))                     # False
	print(is_palindrome("python"))                    # False
	print(is_palindrome("OpenAI"))                    # False

	# Edge cases
	print(is_palindrome("12321"))                     # True
	print(is_palindrome("12345"))                     # False
	print(is_palindrome("Able was I ere I saw Elba")) # True

main()