from pathlib import Path

FILE_NAME = 'number.txt'
FILE_PATH = Path().cwd() / FILE_NAME

def main():
    if not FILE_PATH.exists():
        FILE_PATH.touch()

    with FILE_PATH.open(mode='r') as file:
        number = int(file.read() or 0)

    with FILE_PATH.open(mode='w') as file:
        number += 1
        file.write(str(number))

    print(number)


if __name__ == '__main__':
    main()
