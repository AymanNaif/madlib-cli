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


def read_template(path):
    try:
        with open(path) as file:
            file_content = file.read()
        return file_content
    except FileNotFoundError:
        raise FileNotFoundError('ERORR:: file not found')


def parse_template(texts):
    str_template = re.sub('{[^}]+}', '{}', texts)
    list_template = tuple(re.findall("{(.*?)}", texts))
    return str_template, list_template


def merge(blank, full_text):
    return blank.format(*full_text)


# if __name__ == "__main__":
#     welcome()
#     user_answerss = user_input()
#     file_content = read_template('./assets/script.txt')
#     print(file_content)
#     blanks = parse_template(file_content)
#     print(blanks)
#     merge(blanks, user_answerss)
