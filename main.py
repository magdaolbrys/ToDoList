import datetime as dt
import matplotlib.pyplot as plt

class Task:

    list_of_tasks = []

    def __init__(self, task, category, date_added, deadline, is_done = False):
        self.task = task
        self.category = category
        self.date_added = date_added
        self.deadline = deadline
        self.is_done = is_done
        self.list_of_tasks.append(self)

    # a method to display a given task
    def show_task(self):

        if type(self.category) is list:
            text = 'categories: '
            for a in self.category:
                text += a + ', '
        else:
            text = 'category: {}'.format(self.category) + ', '

        print(f'{(self.task).upper()}, {text} date added: {self.date_added}, deadline: {self.deadline} \n')

    # a method that allows you to mark a task as completed
    def mark_as_done(self):
        self.is_done = True

    # a method that specifies what a class object presented as a string should look like
    def __str__(self):
        if type(self.category) is list:
            text = 'categories: '
            for a in self.category:
                text += a + ', '
        else:
            text = 'category: {}'.format(self.category) + ', '
        return f'{(self.task).upper()}  {text} date added: {self.date_added},  deadline: {self.deadline} \n'



# function - adding a task
def add_task():
    print('Task:')
    task = input()
    print('Category:')
    category = input()
    date_added = dt.date.today()
    print('Time limit: ')
    while True:
        try:
            print('Day: ')
            d = input()
            print('Month: ')
            m = input()
            print('Year: ')
            y = input()
            deadline = dt.date(int(y), int(m), int(d))
            break
        except ValueError:
            print('Enter the due date for the task again. \n'
                  'Use only numbers and make sure the date you enter exists .\n')

    return Task(task, category, date_added, deadline)


#sample tasks:
Task('Take the dog for a walk', ['household duties', 'pets'], dt.date.today(), dt.date(2023, 10, 14)).mark_as_done()
Task('Feed a cat', ['household duties', 'pets'], dt.date.today(), dt.date(2023, 10, 12))
Task('Math homework', 'school',dt.date.today(), dt.date(2023, 10, 14))
Task('Clean the bathroom', 'household duties', dt.date.today(), dt.date(2023, 10, 15))
Task('Grocery shopping', 'household duties', dt.date.today(), dt.date(2023, 10, 14)).mark_as_done()
Task('Fix the bike', 'fixes', dt.date.today(), dt.date(2023, 10, 25))


while True:
    print('Do you want to add new task? Y/N')
    x = input ()
    x = x.lower()
    if x == 'y' or x == 'yes':
        add_task()
    elif x == 'n' or x == 'no':
        break
    else:
        pass


# counting the number of completed and uncompleted tasks
number_of_tasks_done = len([task for task in Task.list_of_tasks if task.is_done])
number_of_tasks_not_done= len(Task.list_of_tasks) - number_of_tasks_done


# saving the list to a txt file
with open('YourToDoList.txt', 'w') as plik:
    plik.write('YOUR TASKS: \n')
    plik.write('-' * 20 + '\n')
    for task in Task.list_of_tasks:
        if task.is_done == False:
            plik.write(str(task))
        else:
            plik.write('//done - ' + str(task))
    plik.write('-' * 20+ '\n')
    plik.write(f'Tasks completed: {number_of_tasks_done} Tasks not completed: {number_of_tasks_not_done}')
    print('A text file named ''YourToDoList'' has been created.')


# ratio of unfinished to completed tasks - pie chart
plt.pie([number_of_tasks_not_done, number_of_tasks_done], labels = ['Tasks completed', 'Tasks not completed:'], colors = ['lightgreen', 'green'],  autopct='%1.1f%%', startangle=90)
plt.title('Your tasks:')
plt.show()