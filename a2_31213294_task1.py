"""
NAME Kapish Kuchroo
STUDENT ID 31213294
START DATE:Sunday, 17 May 2020 at 5:52 pm
LAST MODIFIED: Monday, 8 June 2020 at 1:08 pm
"""
""" In this task, we are creating a class from the provided template.
The name of the class is Person class , methods of the class are as follows : add_friend(appends the friends
 of the class object to the list),get_name(returns teh string value as first name and last name)
 ,get_friends(returns the list of friends object).

In the load people function we have read the data from the file and cleaned the data using strip and returning it to the
list(friends on the left side of the colon).
and creating a map between the friend and his friends using dictionary.Creating a object of person class
each class must be provided a first and last name and we are supplying a list as well which will hold the object friends
for every class, wit the help of get_friend object function.
Finally returning a list of 200 objects where all friends are mapped onto the objects.

"""


class Person:
    person_object = []

    def __init__(self, first_name, last_name):  # object constructor first name last name and array of objects for friends
        self.person_object = []
        self.first_name = first_name
        self.last_name = last_name

    def add_friend(self, friend_person):        # adds the friend to person_object array
        self.person_object.append(friend_person)

    def get_name(self):                             # returns the first name and last name
        return self.first_name + ' ' + self.last_name

    def get_friends(self):          # returns the array /list of friends objects
        return self.person_object


def load_people():
    final_names = []    # list declaration
    person_object_array = []
    person_friend_map = {}  # dictionary for friend and his friends

    file_handle = open('a2_sample_set.txt', 'r')

    for line in file_handle:
        line = line.split(':')
        final_names.append(line[0])  # people's name into the list

        friend_val = line[1].strip().split(', ')   # friend's name into the list

        person_friend_map[line[0]] = friend_val  # dictionary map created btw 'people' and their friends

    for person_full_name in final_names:
        person_split_name = person_full_name.split()   # splits the name for first name and last name
        person_object = Person(person_split_name[0], person_split_name[1])  # object initilisation with first_name and last_name
        person_object_array.append(person_object)  # using the list to append the object


    for friend_value in person_object_array:
        key_map = friend_value.get_name()      # returns first name and last name of friends
        lst_temp = person_friend_map[key_map]   # temporary list declaration for storing list of strings
        for friend in lst_temp:
            friend_object = get_friend_object(person_object_array, friend)  # friend object created
            friend_value.add_friend(friend_object)  # using the class method to add a new friend

    return person_object_array    # returns the list of objects



def get_friend_object(people_obj_arr, friend):  # list of objects and friend we want to search in the list
    for friend_obj in people_obj_arr:
        if friend_obj.get_name() == friend:     # get name method returns string
            return friend_obj                   # if the string name matches then return the object
    return None


if __name__ == '__main__':
    print(load_people())




