# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: 20220062     
# Date: 04/19/2023



#Part 1 - Main Version
#Create Variables
pass_credits=0
defer_credits=0
fail_credits=0

def Progress(pass_credits,defer_credits,fail_credits):
    if (pass_credits==120):
        return("Progress")
    elif (pass_credits==100 and (defer_credits==20 or fail_credits==20)):
        return("Progress (module trailer)")
    elif(fail_credits<80):
        return("Module retriever ")
    elif(fail_credits>=80):
        return("Exclude")
def get():
    valid=[0,20,40,60,80,100,120]
    while True:
        try:
            pass_credits=int(input("Enter your total PASS credits :"))
            if pass_credits not in valid:
                print("Out of range.\n")
                continue
            defer_credits=int(input("Enter your total DEFER credits:"))
            if defer_credits not in valid:
                print("Out of range.\n")
                continue
            fail_credits=int(input("Enter your total FAIL credits:"))
            if fail_credits not in valid:
                 print("Out of range.\n")
                 continue
        except:
            print("Integer required.\n")
            continue
        else:
            if(pass_credits+defer_credits+fail_credits)!=120:
                print("Total incorrect.\n")
                continue
            else:
                return pass_credits,defer_credits,fail_credits


#Creat Variables

trailer_count=0
progress_count=0
excluded_count=0
retriever_count=0

run = True
while run:
    pass_credits,defer_credits,fail_credits = get()
    Value = Progress(pass_credits,defer_credits,fail_credits)
    if Value == "Progress":
        progress_count += 1
    elif Value == "Progress (module trailer)":
        trailer_count += 1
    elif Value == "Exclude":
        excluded_count += 1
    else:
        retriever_count += 1
    print(Value + "\n")
    user = input("Would you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results: ")
    print("\n")

#If the staff don't want to enter another set of data.
    if user.lower() == 'q':
        run = False
print("-----------------------------------------------------------")

#Counting Total Outcome
total_outcome = progress_count + trailer_count + retriever_count + excluded_count
print("\n")
#Print total outcome
print(total_outcome, "outcomes in total.")
print("----------------------------------------------------------")
