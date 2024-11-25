import time

def greet(name, cb):
    print(f'Hello, {name}!')
    # time.sleep(3)
    cb(name)

def say_bye(name):
    print('Bye!!')

def shout():
    for i in range(5):
        print('GOODBYE!!!!!!!')

# Main
greet('Steve', say_bye)
greet('Mary', shout)

print('Continuing main ...')
# More statements
