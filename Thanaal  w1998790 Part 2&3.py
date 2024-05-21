# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: 20220062     
# Date: 04/19/2023


#Part 1 - Main Version
#Create Variables
Pass=0
Defer=0
Fail=0
#Creating a list for credits.
list = []
credit_list=[]

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
#open file
stu=open("Student","a")
while run:
    pass_credits,defer_credits,fail_credits = get()
    Value = Progress(pass_credits,defer_credits,fail_credits)
    if Value == "Progress":
        credit_list = [f'Progress -{pass_credits},{defer_credits},{fail_credits}']
        list.append(credit_list)
        progress_count += 1
        stu.write("\n%s" % credit_list)
        
    elif Value == "Progress (module trailer)":
        credit_list = [f'Progress (module trailer) -{pass_credits},{defer_credits},{fail_credits}']
        list.append(credit_list)
        trailer_count += 1
        stu.write("\n%s" % credit_list)
        
    elif Value == "Exclude":
        credit_list =[f'Exclude -{pass_credits},{defer_credits},{fail_credits}']
        list.append(credit_list)
        excluded_count += 1
        stu.write("\n%s" % credit_list)
    else:
        credit_list = [f'Module retriever -{pass_credits},{defer_credits},{fail_credits}']
        list.append(credit_list)
        retriever_count += 1
        stu.write("\n%s" % credit_list)
        
    print(Value + "\n")
    user = input("Would you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results: ")
    print("\n")
    if user.lower() == 'q':
        run = False
for d in list:
    for k in d:
        print(k,end='')
    print()
stu.close()

#If the staff don't want to enter another set of data.
if user.lower() == 'q':
        run = False
print("-----------------------------------------------------------")

#Histogram

print("Histogram")

print("Progress ", progress_count, ": ", end="")
for i in range(progress_count):
    print("*", end=" ")
    
print("\nTrailer  ", trailer_count, ": ", end="")
for i in range(trailer_count):
    print("*", end=" ")

print("\nRetriever", retriever_count, ": ", end="")
for i in range(retriever_count):
    print("*", end=" ")
    
print("\nExcluded ", excluded_count, ": ", end="")
for i in range(excluded_count):
    print("*", end=" ")

#Counting Total Outcome
total_outcome = progress_count + trailer_count + retriever_count + excluded_count
print("\n")
#Print total outcome
print(total_outcome, "outcomes in total.")
print("----------------------------------------------------------")
