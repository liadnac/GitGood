def greet(name):
    print(f"hi {name} :)")


def fun(hour):
    is_awake = True
    if hour >= 19 or hour <= 6:
        is_awake = False
    return is_awake
