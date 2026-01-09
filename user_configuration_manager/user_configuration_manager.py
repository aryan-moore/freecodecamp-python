def add_setting(settings, to_add):
    key = to_add[0].lower()
    val = to_add[1].lower()
    if key in list(settings.keys()):
        return (f"Setting '{key}' already exists! Cannot add a new setting with this name.")
    else:
        settings[key] = val
        return (f"Setting '{key}' added with value '{val}' successfully!")

def update_setting(settings, to_update):
    key = to_update[0].lower()
    val = to_update[1].lower()
    if key in list(settings.keys()):
        settings[key] = val
        return (f"Setting '{key}' updated to '{val}' successfully!")
    else:
        return (f"Setting '{key}' does not exist! Cannot update a non-existing setting.")

def delete_setting(settings, to_delete):
    key = to_delete.lower()
    if key in list(settings.keys()):
        del settings[key]
        return (f"Setting '{key}' deleted successfully!")
    else:
        return (f"Setting not found!")

def view_settings(settings):
    if not settings:
        return ("No settings available.")
    else:
        ans = "Current User Settings:\n"
        for key in settings.keys():
            ans += key.title() + ": " + settings[key] + "\n"
        return ans

test_settings = {
    'theme' : 'pirates',
    'volume' : '300',
    'user' : 'grandma'
}

def main(test_settings):
    print(view_settings(test_settings))
    print(add_setting(test_settings, ('wifi', 'off')))
    print(delete_setting(test_settings, 'theme'))
    print(view_settings(test_settings))

main(test_settings)
