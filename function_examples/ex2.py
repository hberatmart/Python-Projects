def sav_user(**user):
    print(user)
    return user

print(type(sav_user(id=1, name="Berat", age=23)))