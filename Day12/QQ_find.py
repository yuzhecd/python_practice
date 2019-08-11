import re

def main():
    username = input('Please input your name: ')
    qq = input('Please input your QQ: ')
    # use match to re
    user_right = re.match(r'^[0-9a-zA-Z_]{6,20}$', username)
    if not user_right:
        print('Please input right username')
    qq_right = re.match(r'^[1-9]\d{4,11}$', qq)
    if not qq_right:
        print('Pleaset input right QQ')
    if user_right and qq_right:
        print('You input right information')

if __name__ == '__main__':
    main()
