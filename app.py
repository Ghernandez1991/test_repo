#importing this from a python file because it is a list of dictionaries. 
from data import data

#view type of data- it is a list
type(data)

#see how many items are in the list- there are 7
len(data)

#grab the first list item. 
data[0]

#type of each item in the list
type(data[0])

#view the keys of the dictionary
data[0].keys()

#view the values of the dictionary

data[0].values()

#create empty array to append salary to
salary_array = []
#loop down each dictionary inside list data
for item in data:
    #grab the value associated with key salary and create individual salary variable
    individual_salary = item['salary']
    #append the individual salary variable to the empty array 
    salary_array.append(individual_salary)

#use sum to add all items in the array 
print(sum(salary_array))


#create a class for employees in the company 
class Employees:
    #capture a class object of how may employees(how many times we instantiate a class object)
    num_of_emps = 0
    #create class variable lists(blank) so we can append each employee instance
    instances_of_class = []
    # #create class variable lists(blank) so we can append each employee salary 
    company_salary_list = []
    

    #init method instantiates the class, default takes self, we also want to include first_name, id, manager and salary as arguements
    def __init__(self, first_name, id, manager, salary):
        #each instance of the class will have a first_name, id, manager and salary, and that self arguement will be equal to the arguements pass when creating the object. 
        self.first_name = first_name
        self.id = id
        self.manager = manager
        self.salary = salary
        #add one to our class variable as we just instantiated a class object
        Employees.num_of_emps += 1
        #append the class object(self) to list(class variable) so we can see all instances of the class
        self.instances_of_class.append(self)
        #append the class object.salary to list(class variable) so we can lump all the salaries together and sum 
        self.company_salary_list.append(self.salary)

    #class method decorator takes the class as an arguement. 
    #using this because I want access to the class variable(list-company_salary_list) so we can sum them together
    @classmethod
    #take in the class as an arguement
    def calculate_total_salary(cls):
        #then use company_salary_list and sum returns an integer
        return sum(cls.company_salary_list)

    #class method decorator takes the class as an arguement. 
    @classmethod
    #we also want to pass id as an argument
    #if we have an id, we can find a manager id, if we have a manager_id, we can find manager name
    def get_manager_name(cls, id):
        #loop through list of employee instances
        for employee in cls.instances_of_class:
            #if the passed id = the current employee id
            if id == employee.id:
                #capture the managers id from employee object properties
                employees_manager_id =  employee.manager
            #if you cant find the manager name in this item in the list, dont do anything
            else:
                pass
        #loop again down each employee
        for employee in cls.instances_of_class:
            #now that we have the manager id, we can match manager id, to employee id
            if employees_manager_id == employee.id:
                #use this to return the manager name
                return employee.first_name


#user enumerate because we want the index and the value of the list(data) we are iterating over
for i,v in enumerate(data):
    #the id  is the dictionary value associated with key 'id'
    id = v['id']
    #the first_name  is the dictionary value associated with key 'first_name'
    first_name = v['first_name']
    #the manager  is the dictionary value associated with key 'manager'
    manager = v['manager']
    #the salary  is the dictionary value associated with key 'manager'
    salary = v['salary']

    #create a class object by passing the existing first_name, id, and manager to the employees class
    employee = Employees(first_name,id,manager,salary)
    

#we can print off the number of employees we have based on the class variable
print(Employees.num_of_emps)
#we can print off the all class instances(stored as a list) based on the class variable
print(Employees.instances_of_class)

#print off a list of all salaries 
print(Employees.company_salary_list)


#get manager name for employee id 9
Employees.get_manager_name(9)


#define out main function that will execute when the program is run as a script 
def main():
    #use f string to print Employees.calculate_total_salary method. This calls the class method which returns the sum of employees salary from the list
    print(f'The total salary for the company is {Employees.calculate_total_salary()}')
    ##iterate over employee object list
    for employee in Employees.instances_of_class:
        #print off each employees name, id and their managers name
        print(f'employees first name is {employee.first_name}, employees id is  {employee.id}, and employees manager is  {Employees.get_manager_name(employee.id)}')
    #create a blank dictionary to store managers, and their employees 
    org_dictionary = {}
    #iterate over the list of employees 
    for employee in Employees.instances_of_class:
        #grab the manager name for each employee by calling class method get_manager_name and passing the current employee id
        manager_name = Employees.get_manager_name(employee.id)
        #set current employee name to employee first name
        employee_name = employee.first_name

        #check if the current managers name already exists in the dictionary
        if manager_name in org_dictionary:
            #if it does, append the employee name to the existing key 
            org_dictionary[manager_name].append(employee_name)
            #if not create a new key(manager name) with a new list of values(employee_name)
        else:
            org_dictionary[manager_name] = [employee_name]
        
    #print off the existing manager dictionary
    print(org_dictionary)

    #use list comprehensions to create lists of each key in org_dictionary and for the list(of values) associated with those keys 
    manager_list = [x for x in org_dictionary.keys()]
    employee_list = [x for x in org_dictionary.values()]


    #print off all managers using dictionary.keys
    print(f'all managers in the company are, {org_dictionary.keys()}')
    #print off all employees by printing off dictionary.values
    print(f' all employees of the company are {org_dictionary.values()}')




    #this will print off the manager and his subordinates, although would not work without knowing how many keys we have specifically. Can be improved. 
    print(f'Manager {manager_list[0]} has employees {employee_list[0]}')
    print(f'Manager {manager_list[1]} has employees {employee_list[1]}')
    #.sort sorts the list in place, can't really use it in this context. Sort actually returns the new object, so using here.  
    print(f'Manager {manager_list[2]} has employees {sorted(employee_list[2])}')


#if the file is run as a script, if __name__ == "__main__": is true and the code under fires
#if imported from another library, this will not fire

if __name__ == "__main__":
    print('This file is being run as a script')
    main()






