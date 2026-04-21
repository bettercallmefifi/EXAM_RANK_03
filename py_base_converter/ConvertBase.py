def convertbase(num: str ,from_base: int, to_base: int):
    digit = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    try:
        if not 2 <= from_base <= 36:
            return "ERROR"
        if not 2 <= to_base <= 36 :
            return "ERROR"
		
        n = int(num, from_base)
        if n == 0:
            return "0"

        res = ""
        while n:
            res += digit[n % to_base]
            n = n // to_base
        return res[::-1]
    except Exception:
        return "ERROR"

def main():
    print(convertbase("Ff", 16, 10)) # "255"
    print(convertbase("00FF", 16, 2)) # "11111111"
    print(convertbase("z", 36, 10)) # "35"
    print(convertbase("0000", 7, 10)) # "0"
    print(convertbase("0001", 2, 10)) # "1"
    print(convertbase("1010", 2, 16)) # "A"
    print(convertbase("133742", 8, 42)) #ERROR

main()