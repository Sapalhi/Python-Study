#LAB-03 - Build an RPG Character
full_dot = '●'
empty_dot = '○'

def create_character(name, strength, smart, charisma):
    if not isinstance(name, str):
        return 'The character name should be a string'
    elif not name or not name.strip():
        return 'The character should have a name'
    elif len(name) > 10:
        return 'The character name is too long'
    elif ' ' in name:
        return 'The character name should not contain spaces'
    elif not isinstance(strength, int) or not isinstance(smart, int) or not isinstance(charisma, int):
        return 'All stats should be integers'
    elif strength < 1 or smart < 1 or charisma < 1:
        return 'All stats should be no less than 1'
    elif strength > 4 or smart > 4 or charisma > 4:
        return 'All stats should be no more than 4'
    elif (strength + smart + charisma) != 7:
        return 'The character should start with 7 points'
    else:
        return f'{name}\nSTR {full_dot*(strength)+empty_dot*(10-strength)}\nINT {full_dot*(smart)+empty_dot*(10-smart)}\nCHA {full_dot*(charisma)+empty_dot*(10-charisma)}'

print(create_character('ren', 3, 2, 2))