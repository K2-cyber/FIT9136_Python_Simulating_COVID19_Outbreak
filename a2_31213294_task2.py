"""
NAME Kapish Kuchroo
STUDENT ID 31213294
START DATE: Sunday, 17 May 2020 at 5:52 pm
LAST MODIFIED: Monday, 8 June 2020 at 1:08 pm
"""
"""
(load patients) will use the concept of inheritance and make "class Patient" using the Person class from the previous task.
it will inherit all the attributes and methods and we have (get_health) ,(set_health),(is_contagious),(infect),(sleep) methods.
(will_infect) function is working in such a way that it we are considering the case of 10 elements in the list,
from which count of them is appended to the list and random index is used to match and return if the value is 1
(run_simulation) it is taking three arguments is used to check if the friend is contagious or not and
if they are then it will transfer the viral load on the health of the contagious person.
If they are contagious then it keeps the count of it in the list and makes the patients
sleep after every day.returns the count of list at the end of simulation

The complete simulation runs on three different days meeting probability and patient zero health
the idea is to run for as many days as asked and the meeting probability is gonna decide upon the
chances of patients meetings friends and setting the first patient's (object) health as patient_zero_health.
finally returning the no of infected people in one entire simulation.

"""

from random import randrange
from a2_31213294_task1 import *



class Patient(Person):


    def __init__(self, first_name, last_name, health):  # constructor for the patient class
        self.first_name = first_name
        self.last_name = last_name
        self.health = health
        self.person_object=[]                           # initialising a list with every object

    def get_health(self):
        return self.health

    def set_health(self, new_health):

        self.health = new_health

    def is_contagious(self):
        if self.health < 50:
            return True
        else:
            return False

    def infect(self, viral_load):                   # method  will infect with the provided viral load

        if self.health <= 29:
            self.health = self.health - (0.1 * viral_load)
        elif 29 < self.health < 50:
            self.health = self.health - (1.0 * viral_load)
        else:
            self.health = self.health - (2.0 * viral_load)

        self.health = max(self.health, 0)

    def sleep(self):                            # adds 5 points to health
        self.health = min(self.health + 5, 100)


def will_meet(meeting_probability):
    no_of_ones = int(meeting_probability*100)
    no_of_zeros = 100 - no_of_ones              # example lst=[1,1,1,1,1,1,1,0,0,0] and so on up to 100 values
    lst_will_meet = []   # list for holding the number of one's and zeros
    for each in range(1,no_of_ones+1):
        lst_will_meet.append(1)
    for each in range(1,no_of_zeros+1):
        lst_will_meet.append(0)

    random_position = randrange(100)    # uses the random function to calculate a value between 0 to 100
    if lst_will_meet[random_position] == 1:
        return True
    else:
        return False


def get_viral_load(hpc):        # takes the health points of contagious person
    viral_load = 5+(hpc-25)**2/62
    return viral_load           # viral load on the contagious person


def run_simulation(days, meeting_probability, patient_zero_health):

    patient_object_array=load_patients(75)   # calling load patient function and initialising health to 75
    file_handle = open('a2_sample_set.txt', 'r')
    patient_first = file_handle.readline()
    patient_zero_list = patient_first.split(':')
    patient_zero = patient_zero_list[0]  # patient zero read from the file
    patient_zero_object = get_friend_object(patient_object_array, patient_zero) # object created using get_friend_object
    patient_zero_object.set_health(patient_zero_health)  # setting the health of the first object from patient_zero_object
    lst_count = []  # meeting count stored inside the list
    for each_day in range(1, days + 1):   # loop for days
        count = 0  # after each day setting count to zero
        for each_patient in patient_object_array:  # patient object
            for each_friend in each_patient.get_friends():  # his friends
                if will_meet(meeting_probability):  # function which will determine the probability of friend and his friends meeting
                    if each_patient.is_contagious():   # is_contagious decides if the patient is contagious or not by looking at the health points
                        each_friend.infect(get_viral_load(each_patient.get_health()))  # infect method is called and viral load is supplied to the current health

            if each_patient.is_contagious():
                count = count+1   # count increment
            each_patient.sleep()    # recovering the infected patient with sleep
        lst_count.append(count)     # count of infected is added to the list after every day

    return lst_count   # count of infected for one complete simulation


def load_patients(initial_health):
    final_names = []                # list declaration
    patient_object_array = []
    patient_friend_map = {}          # dictionary for patient and his friends

    file_handle = open('a2_sample_set.txt', 'r')

    for line in file_handle:
        line = line.split(':')
        final_names.append(line[0])  # people's name into the list

        friend_val = line[1].strip().split(', ')   # friend's name into the list

        patient_friend_map[line[0]] = friend_val  # dictionary map created btw 'people' and their friends

    for person_full_name in final_names:
        person_split_name = person_full_name.split()   # splits the name for first name and last name
        patient_object = Patient(person_split_name[0], person_split_name[1],initial_health)  # object initilisation with first_name and last_name
        patient_object_array.append(patient_object)  # using the list to append the object


    for friend_value in patient_object_array:
        key_map = friend_value.get_name()      # returns first name and last name of friends
        lst_temp = patient_friend_map[key_map]  # temporary list declaration for storing list of strings
        for friend in lst_temp:
            patient_friend_object = get_friend_object(patient_object_array, friend)  # friend object created using the function on line 141
            friend_value.add_friend(patient_friend_object)  # using the class method to add a new friend

    return patient_object_array


def get_friend_object(patient_obj_arr, friend):   # list of objects and friend we want to search in the list
    for friend_obj in patient_obj_arr:
        if friend_obj.get_name() == friend:        # get name method returns string
            return friend_obj                      # if the string name matches then return the object
    return None


if __name__ == '__main__':



    # This is a sample test case. Write your own testing code here.
    test_result = run_simulation(155, 0.7, 49)
    print(test_result)
    # [5, 4, 6, 7, 7, 11, 14, 16, 18, 21, 20, 21, 23, 24, 25, 27, 27, 28, 33, 33, 37, 36, 44, 48, 55,
    # 62, 66, 75, 84, 90, 101, 108, 114, 118, 130, 138, 145, 149, 155, 160, 165, 169, 169, 169, 173,
    # 178, 182, 187, 189, 192, 189, 192, 192, 193, 192, 193, 193, 189, 191, 190, 192, 190, 189, 192,
    # 190, 192, 189, 193, 192, 194, 194, 195, 196, 196, 196, 197, 199, 194, 196, 197, 199, 198, 198,
    # 197, 198, 198, 198, 197, 197, 198, 196, 194, 194, 191, 194, 195, 194, 196, 191, 193, 189, 194,
    # 193, 195, 196, 195, 196, 193, 193, 193, 195, 192, 193, 194, 195, 194, 194, 198, 198, 199, 197,
    # 197, 196, 199, 198, 197, 198, 198, 196, 198, 200, 197, 197, 198, 195, 195, 193, 195, 196, 198,
    # 195, 197, 195, 198, 194, 198, 198, 197, 192, 195, 196, 196, 196, 197, 195]


    test_result = run_simulation(100, 0.1, 49)

    # [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    # 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    # 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    # 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    test_result=run_simulation(50,0.5,49)
    # [2, 1, 2, 2, 2, 1, 2, 2, 3, 3, 4, 3, 4, 4, 4, 4, 4, 3, 5, 7, 6, 7, 6, 6, 7, 6, 6, 7, 6, 8,
    #  8, 10, 11, 13, 13, 15, 14, 16, 16, 20, 23, 29, 28, 33, 36, 42, 41, 42, 42, 49]

    test_result = run_simulation(40, 1, 1)
    # [6, 14, 26, 47, 58, 77, 110, 124, 144, 154, 168, 176, 182, 185, 191, 195, 199, 199, 199, 199,
    # 199, 199, 199, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200]


# do not add code here (outside the main block).


