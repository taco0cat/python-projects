full_dot = '●'
empty_dot = '○'

def create_character(cname, strength, intelligence, charisma):
    # Validating cname
    if not isinstance(cname, str):
        return "The character name should be a string"
    if len(cname) > 10:
        return "The character name is too long"
    if ' ' in cname:
        return "The character name should not contain spaces"

    # Validating stats
        # any() : any one should be true
        # all() : all should be true
    stats = [strength, intelligence, charisma]
    if not all(isinstance(stat, int) for stat in stats):
        return "All stats should be integers"
    if any(stat < 1 for stat in stats):
        return "All stats should be no less than 1"
    if any(stat > 4 for stat in stats):
        return "All stats should be no more than 4"
    if (strength + intelligence + charisma) != 7:
        return "The character should start with 7 points"

    str_dots = (full_dot * strength) + (empty_dot * (10 - strength))
    int_dots = (full_dot * intelligence) + (empty_dot * (10 - intelligence))
    cha_dots = (full_dot * charisma) + (empty_dot * (10 - charisma))

    final_string = f"{cname}\nSTR {str_dots}\nINT {int_dots}\nCHA {cha_dots}"

    return final_string

rpg = create_character("ren", 4, 2, 1)
print(rpg)


# OUTPUT
    # ren
    # STR ●●●●○○○○○○
    # INT ●●○○○○○○○○
    # CHA ●○○○○○○○○○