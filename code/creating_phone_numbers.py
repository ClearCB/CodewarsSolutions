def create_phone_number(n):
    prefix = ""
    first_three= ""
    rest = ""
    for i in n[0:3]:
        prefix += str(i)
    for j in n[3:6]:
        first_three += str(j)
    for k in n[6:]:
        rest += str(k)
    telephone_number = f"({prefix}) {first_three}-{rest}"
    return telephone_number

create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])