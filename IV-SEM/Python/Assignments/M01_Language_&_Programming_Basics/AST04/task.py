
def Reverse_String(s: str) -> str:
    reversed_s = ""
    
    for char in s:
        
        reversed_s = char + reversed_s
    return reversed_s

if __name__ == '__main__':
    
    s = input()
    print(Reverse_String(s))