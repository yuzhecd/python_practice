import json

def main():
    mydict = {
        'name':'James',
        'age': 38,
        'qq': 8458403,
        'friends': ['Tom', 'Jack']
    }

    try:
        with open('data.json', 'w') as f:
            json.dump(mydict, f)
    except IOError as e:
        print(e)
    print('Done')

if __name__ == '__main__':
    main()
