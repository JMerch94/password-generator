import string
import secrets
import inquirer
from inquirer.themes import GreenPassion
import configparser

# read config file
config = configparser.ConfigParser()
config.sections()
config.read('config.ini')

config_rules = {
    'max_length': config['password_options']['max_length'],
    'default_length': config['password_options']['default_length']
}


class bcolors:
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'


# assign max_length from config
print(f'{bcolors.WARNING}\nThe maximum password length is ' + config_rules['max_length'] + ' characters.')
print(f'This can be altered in the config file.\n{bcolors.ENDC}')

# prompts for desired password complexity
options = [
    inquirer.Text('password_length',
                  message='Password Length'),
    inquirer.Checkbox('character_categories',
                      message='Character Categories',
                      choices=['Uppercase', 'Lowercase', 'Numbers', 'Symbols']
                      )
]

selected_options = inquirer.prompt(options, theme=GreenPassion())

password_length = selected_options["password_length"]
character_categories = selected_options["character_categories"]

selected_characters = ''
for i in character_categories:
    if i == 'Uppercase':
        selected_characters = selected_characters + string.ascii_uppercase
    elif i == 'Lowercase':
        selected_characters = selected_characters + string.ascii_lowercase
    elif i == 'Numbers':
        selected_characters = selected_characters + string.digits
    elif i == 'Symbols':
        selected_characters = selected_characters + string.punctuation


# validation rules
def validation(rules):
    if password_length == '':
        print(f'{bcolors.FAIL}No password length was defined.{bcolors.ENDC}')
        print(password_length)
        return
    elif selected_characters == '':
        print(selected_characters)
        print(f'{bcolors.FAIL}No character categories were defined.{bcolors.ENDC}')
        return
    elif int(password_length) > int(rules['max_length']):
        print(f'{bcolors.FAIL}A password length of ' + password_length + ' is not allowed.')
        print('The maximum password length is ' + rules['max_length'] + f' characters.{bcolors.ENDC}')
        return
    else:
        # create and print password
        print('Generated Password:')
        password = ''.join(secrets.choice(selected_characters) for i in range(int(password_length)))
        print(password)


# run validation function
validation(config_rules)

print('\nBuilt using the Python Secrets module.\n')
