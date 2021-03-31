# Your code goes here:
def render_person(name, date_born, eye_color, age, gender):
    param = name + " is a "+ str(age)+ " years old "+ gender + " born in "+ date_born + " with "+eye_color+" eyes"
    return param


# Do not edit below this line
print(render_person('Bob', '05/22/1983', 'green', 23, 'male'))