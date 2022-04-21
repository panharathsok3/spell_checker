from spell_checker import Spellchecker, open_file


finish = 0
spell = Spellchecker()
file_name = input('Enter the name of your file: ')

while not finish:
    try:
        print('')
        print(spell.find_incorrect_word(open_file(file_name)))
        print('These were the errors we found in your text.')
        finish = 1
    except FileNotFoundError:
        file_name = input('Please enter the correct name of your file: ')
