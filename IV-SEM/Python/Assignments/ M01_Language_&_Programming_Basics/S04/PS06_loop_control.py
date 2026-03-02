''' password retry system(max 3 attempts) ,if password is correct show login successful '''
p1 = "abc123"
for i in range(3):
    p2 = input("Enter your password: ")
    if p1 == p2:
        print("Login successful")
        break
else:
    print("Account locked") 