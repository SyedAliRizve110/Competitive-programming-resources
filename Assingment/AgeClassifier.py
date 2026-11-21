def age_classifier(age):
    if age < 13:
        print('Child')
    elif age>=13 and age<=19:
        print('Teenage')
    elif age>=20 and age<=59:
        print('Adult')
    else: print('Senior')

age = 45
age_classifier(age)