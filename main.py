import random

# Generators
# 1.1 simple generator that lists nums from 1 to 10000 with step = 2
gen = (i for i in range(1, 10000, 2))


# testing
# print(next(gen))
# print(next(gen))


# 1.2. simple generator function using yield statement to generate IDs that starts from 34***
# it can be used for creating custom IDs for the system/program
def gen_id():
    initial_id = 34000
    while True:
        yield initial_id
        initial_id += 1


id_generator = gen_id()
user_id1 = next(id_generator)
user_id2 = next(id_generator)


# testing
# print(user_id1)
# print(user_id2)

# 2. Decorators
# 2.1. simple decorator function that can be used in the application for health tracking
# when the user will set height and weight, the code will calculate body mass index
# and print out IBM with recommendations

def IBM_check(min_constraint, max_constraint):
    def check(function):
        def new_function():
            params = function()
            IBM = params[0] / params[1] ** 2
            if IBM <= min_constraint or IBM >= max_constraint:
                print(f'Your body mass index is {round(IBM, 2)}. You should better go to the doctor as it '
                      f'doesn\'t seem to be good.')
            else:
                print(f'Your body mass index is {round(IBM, 2)}. It seems ok.')

        return new_function

    return check


@IBM_check(18.5, 25)
def set_body_params():
    height = float(input('Please insert height in m: '))
    weight = float(input('Please insert your weight in kg: '))
    return [weight, height]


# testing
# set_body_params()

# 2.2. Examples of using property decorator within a class to access
class Worker:

    def __init__(self, access="private", salary=10000):
        self.__access = access
        self.__salary = salary

    def __get_access(self):
        return self.__access

    def __set_access(self, access):
        if access == 'public':
            raise ValueError('No public access allowed.')
        else:
            self.__access = access

    def del_access(self):
        del self.__access

    access = property(__get_access, __set_access, del_access)

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        if value < 10000:
            print('It\'s not too much, we deserve more!')
        else:
            self.__salary = value

    @salary.deleter
    def salary(self):
        del self.__salary


worker1 = Worker()


# testing
# worker1.access = 'public'
# worker1.salary = 1000

# 3. Iterator for the task manager that iterates over random tasks from the inserted
class TaskManager:
    def __init__(self, *tasks):
        self.tasks = []
        for task in tasks:
            self.tasks.append(task)

    def add_task(self):
        self.tasks.append(str(input('Please insert the next task: ')))

    def __iter__(self):
        return self

    def __next__(self):
        random.shuffle(self.tasks)
        if not self.tasks:
            raise StopIteration('Great job! There are no tasks anymore!')
        task = self.tasks[0]
        del self.tasks[0]
        return task


'''
# testing
tasks_to_do = TaskManager('sleep', 'work', 'cry', 'cook')
tasks_to_do.add_task()
print(next(tasks_to_do))
print(next(tasks_to_do))
print(next(tasks_to_do))
print(next(tasks_to_do))
print(next(tasks_to_do))
print(next(tasks_to_do))
'''


# 4. Context manager to work with files
class ContextManager:

    def __init__(self, filepath, mode='r+', *contents):
        self.filepath = filepath
        self.mode = mode
        self.file = open(self.filepath, self.mode)
        for i in contents:
            self.file.write(i)

    def __enter__(self):
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


'''
# testing
# read file contents
with ContextManager('test_file_cont_manager') as file:
    print(file.read())

# write file content
with ContextManager('test_file1', 'a') as file:
    file.write('Best test11')

# create new file and write a message
file = ContextManager('test_file2', 'x', 'test messages', 'test message 1', 'test message 2')
'''
