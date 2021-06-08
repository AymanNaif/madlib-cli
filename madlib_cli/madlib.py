import re


def welcome():
    print("""
Welcome to Video Game
Here we goooooooooo!!
""")


user_list = ['Adjective', 'Adjective', 'A First Name',
             'Past Tense Verb', 'A First Name', 'Adjective', 'Adjective', 'Plural Noun', 'Large Animal', 'Small Animal', "A Girl's Name", 'Adjective', 'Plural Noun', 'Adjective', 'Plural Noun', 'Number 1-50', "First Name's", 'Number', 'Plural Noun', 'Number', 'Plural Noun']


def user_input():
    user_answer = []
    for i in range(len(user_list)):
        user_answer.append(input(f'Enter {user_list[i]}: '))

    return user_answer


# user_input()
# user_list_answer = user_input()  # list of user answer


def read_template():

    with open('./assets/script.txt') as file:
        file_content = file.read()
    return file_content


file_contents = read_template()  # file content as a string


def parse_template(texts):
    list_template = re.findall("{[^]+}", texts)
    str_template = re.sub("{[^]+}", texts)
    return str_template, list_template


str_and_list = parse_template(file_contents)
print(str_and_list)


def merge(template, lst):
    pass


def write_template():
    pass
