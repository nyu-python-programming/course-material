x = 10

def nonsense1():
    return 10


def nonsense2():
    response = input("What's your age?")
    if response.isnumeric():
        response = int(response)
        response = response * 7
        return response
    else:
        return False

