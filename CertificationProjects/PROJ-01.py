#PROJ-01 - Build a User Configuration Manager
def add_setting(dict_setting,tuple_items):
    # Lower letters
    tuple_items = tuple(item.lower() for item in tuple_items)

    if tuple_items[0] in dict_setting:
    
        return f"Setting '{tuple_items[0]}' already exists! Cannot add a new setting with this name."
    else:
        dict_setting.update([tuple_items]) 

        return f"Setting '{tuple_items[0]}' added with value '{tuple_items[1]}' successfully!"

def update_setting(dict_setting,tuple_items):

    tuple_items = tuple(item.lower() for item in tuple_items)

    if tuple_items[0] in dict_setting:
        dict_setting.update([tuple_items]) 
        return f"Setting '{tuple_items[0]}' updated to '{tuple_items[1]}' successfully!"
    else:
        return f"Setting '{tuple_items[0]}' does not exist! Cannot update a non-existing setting."

def delete_setting(dict_setting,keyword):

    keyword = keyword.lower()

    if keyword in dict_setting:
        dict_setting.pop(keyword) 
        return f"Setting '{keyword}' deleted successfully!"
    else:
        return f"Setting not found!"

def view_settings(dict_setting):

    if not dict_setting: 
        return f"No settings available."
    else:
        result = "Current User Settings:"

        for key, value in dict_setting.items():
            result += f"\n{key[0].upper() + key[1:]}: {value}"
        result += f"\n"
        return result

# Main
test_settings = {'theme': 'dark'}

print(add_setting(test_settings, ('volume', 'low')))

print(update_setting(test_settings, ('volume', 'high')))

print(delete_setting(test_settings, 'volume'))

#print(view_settings({'theme': 'dark', 'notifications': 'enabled', 'volume': 'high'}))
print(view_settings(test_settings))

