import re

def main():
    sentence = 'Fuck you'
    purified = re.sub('fuck','*', sentence, flags=re.IGNORECASE)
    print(purified)

if __name__ == '__main__':
    main()
