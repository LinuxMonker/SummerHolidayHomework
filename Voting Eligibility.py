print("Voting Eligibility Checker")
age=int(input("Please enter your age: "))

if age >= 18:
    print("Yes, you can vote.")
else:
    print("No, you will have to wait for", 18-age, "years.")
