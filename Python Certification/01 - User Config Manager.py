test_settings = {"theme":"light", "notifications":"enabled"}

def add_setting(dctSettings, tupKV):
    key, value = tupKV
    key = key.lower()
    value = value.lower()

    if key in dctSettings.keys():
        return f"Setting \'{key}\' already exists! Cannot add a new setting with this name."
    else:
        dctSettings[key] = value
        return f"Setting \'{key}\' added with value '{value}' successfully!"

def update_setting(dctSettings, tupKV):
    key, value = tupKV
    key = key.lower()
    value = value.lower()

    if key in dctSettings:
        dctSettings[key] = value
        return f"Setting \'{key}\' updated to \'{value}\' successfully!"
    else:
        return f"Setting \'{key}\' does not exist! Cannot update a non-existing setting."

def delete_setting(dctSettings, key):
    key = key.lower()

    if key in dctSettings:
        del dctSettings[key]
        return f"Setting \'{key}\' deleted successfully!"
    else:
        return "Setting not found!"

def view_settings(dctSettings):
    if not dctSettings:
        return "No settings available."
    else:
        output = "Current User Settings:\n"
        for key, value in dctSettings.items():
            key = key.capitalize()
            output += f"{key}: {value}\n"
        return output

print("--- 1. Testing view_settings (Initial State) ---")
print(view_settings(test_settings))

print("\n--- 2. Testing add_setting ---")
# Success Case:
print(add_setting(test_settings, ("volume", "high"))) 
# Fail Case:
print(add_setting(test_settings, ("theme", "dark")))

print("\n--- 3. Testing update_setting ---")
# Success Case:
print(update_setting(test_settings, ("theme", "dark")))
# Fail Case:
print(update_setting(test_settings, ("brightness", "100")))

print("\n--- 4. Testing delete_setting ---")
# Success Case:
print(delete_setting(test_settings, "notifications"))
# Fail Case:
print(delete_setting(test_settings, "wifi"))

print("\n--- 5. Testing view_settings (Final State) ---")
print(view_settings(test_settings))
