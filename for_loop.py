import questionary
# for i in range(0, 11):
#     print(i)
    
    

# details = []
# question = ["What is your first name", "What is your last name", "What is your age", "What is your nationality"]
# for i in range(0,4):
#     result = input(f"{question[i]}: ")
#     details.append(result)
    
# print(details)

ask = True
result = []

while ask:
    a = input("Kindly input the score: ")
    result.append(a)
    score_continue = questionary.confirm("Will you like to add another student's score: ").ask()
    if not score_continue:
        ask = False
        
print(result)