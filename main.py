
def task(array):
    if isinstance(array, str):
        if array.isnumeric():
            return array.find('0')
        else:
            print(f'{array} не является числом')
    elif isinstance(array, int):
        num = str(array)
        return num.find('0')
    return None


def main():
    print(task("111111111110000000000000000"))


if __name__ == '__main__':
    main()