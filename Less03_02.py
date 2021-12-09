def person_date(name, lastname, birth, city, email, phone):
    return print(f'Name:{name} Lastname: {lastname} Year of birth: {birth} City: {city} Email: {email} Phone: {phone}')


person_date(
    name=input("Name:"),
    lastname=input("Lastname:"),
    birth=input("Year of birth:"),
    city=input("City:"),
    email=input("Email:"),
    phone=input("Phone:"))
