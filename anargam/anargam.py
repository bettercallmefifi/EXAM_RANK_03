def Anagram(s:str, t:str) -> bool:
    if len(s) != len(t):
        return False
    return sorted(s) == sorted(t)

def main():
	print(Anagram("racecar","carrace"))
	print(Anagram("racecar","carace"))
	print(Anagram("Conversation", "Voices rant on"))

main()