total = 4
original = total
print("You have", total ,"Homework tasks to finish today")
count = 0
task_number = 1
while task_number <= total:
    if task_number == 1:
        next = "Math Worksheet"
    elif task_number == 2:
        next = "Science Reading"
    elif task_number == 3:
        next = "English Writing"
    else:
        next = "Coding Practice"
    answer = input(f"Are you done with the {next} task(yes, no): ")
    if answer == "yes":
        print("Great Job, task completed!")
        count += 1
        task_number += 1
        d = total - count
        print("You have", d ,"homework tasks left")
    elif answer == "no":
        d = total - count
        print("Okay, finish the task and check again")
        print("You have", d ,"homework tasks left")
    else:
        print("INVALID CHOICE")
print("===========ALL TASKS COMPLETED===========")
print("Great job completing all your homework tasks")
print("Now lets look into an infinite loop")
test = 0
sat = 0
while test == 0:
    print("This sentence is going to go on forever!")
    sat += 1
    if sat == 3:
        print("Stopping here on purpose to avoid crash")
        break
print("============TASK CHECKLIST============")
print("Total tasks assigned today:", total)
print("Total tasks completed today:", count)
print("Total tasks remaining today:", d)
print("======================================")