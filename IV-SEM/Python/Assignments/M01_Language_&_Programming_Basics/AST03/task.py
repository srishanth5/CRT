def Student_Grade_System(name: str, n1: int, n2: int, n3: int) -> str:
    # Calculate the average
    average = (n1 + n2 + n3) / 3
    
   
    status = "Pass" if average >= 50 else "Fail"
    
    
    return f"Average grade: {average:.2f}, Status: {status}"

if __name__ == '__main__':
    
    name = input().strip()
    
    try:
        n1, n2, n3 = list(map(int, input().split()))
        print(Student_Grade_System(name, n1, n2, n3))
    except ValueError:
        print("Please enter three numerical grades separated by spaces.")
