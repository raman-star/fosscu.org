##TO CHECK IF A PERSON IS ELIGIBLE TO VOTE##

age=int(input())
is_citizen=input()
if age>=18 and is_citizen=="Y":
    print("You are eligible to vote.")
elif age<18 and is_citizen=="N":
    print("You are not eligible to vote.")
elif age<18 and is_citizen=="Y":
    print("You are not eligible to vote.")
elif age>=18 and is_citizen=="N":
    print("You are not eligible to vote.")
