from typing import List
def Sort_string(tlist: list[str]) -> list:
    def counting(s: str) -> int:
        count = 0
        for i in s.lower():
            if i in "aeiou":
                count += 1
        return count
    final_list = sorted(tlist, key=lambda s: (len(s), s.lower(), s.isupper(), counting(s)))
    return final_list

def main():
    # Basic cases
	print(Sort_string(["apple", "bat", "car", "ae", "b"]))
	# ['b', 'ae', 'bat', 'car', 'apple']

	# Same vowel count, different lengths
	print(Sort_string(["dog", "cat", "hi", "a"]))
	# ['a', 'hi', 'cat', 'dog']

	# Same vowel count and length → lexicographical order
	print(Sort_string(["bat", "cat", "ant"]))
	# ['ant', 'bat', 'cat']

	# Mixed uppercase and lowercase
	print(Sort_string(["Apple", "banana", "Kiwi", "grape"]))
	# sorted by vowel count (case-insensitive)

	# Edge cases
	print(Sort_string([]))
	# []

	print(Sort_string(["a", "e", "i", "o", "u"]))
	# ['a', 'e', 'i', 'o', 'u']


main()
