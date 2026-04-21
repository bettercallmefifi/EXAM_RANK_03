def pattern_tracker(s:str) -> int:
    count = 0
    for i in range(1, len(s)):
        if s[i].isdigit() and s[i - 1].isdigit():
            if int(s[i]) == int(s[i - 1]) + 1:
                count += 1
    return count

def main():
    print(pattern_tracker("123a345"))
    print(pattern_tracker("1a2b3c4d5"))
    print(pattern_tracker("12asd34hkh45kjhj56jhj67kjhjh78kjhjh89kjhkhj110"))
    print(pattern_tracker("111111"))
    print(pattern_tracker("012345"))

main()
    