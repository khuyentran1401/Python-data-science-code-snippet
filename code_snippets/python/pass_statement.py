def say_hello():
    pass 

def ask_to_sign_in():
    pass 

def main(is_user: bool):
    if is_user:
        say_hello()
    else:
        ask_to_sign_in()

if __name__ == '__main__':
    main(is_user=True)