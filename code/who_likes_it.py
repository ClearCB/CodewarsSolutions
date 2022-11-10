def likes(names):
    if len(names) < 1:
        return "no one likes this"
    if len(names) == 1:
        first_name = names[0]
        return f"{first_name} likes this"
    if len(names) == 2:
        first_name = names[0]
        second_name = names[1]
        return f"{first_name} and {second_name} like this"
    if len(names) == 3:
        first_name = names[0]
        second_name = names[1]
        third_name = names[2]
        return f"{first_name}, {second_name} and {third_name} like this"
    if len(names) >= 4:
        first_name = names[0]
        second_name = names[1]
        third_name = names[2]
        number = len(names) - 2
        return f"{first_name}, {second_name} and {number} others like this"