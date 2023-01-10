def read_file():
    with open('test.txt', 'r', encoding='utf-8') as f:
        print(f.read())

def rewrite():
    with open('test.txt', 'w', encoding='utf-8') as f:
        a = input('Введите новые данные в файл: ')
        f.write(a)
        f.write('\n\n')
        f.write(a)
        f.write('\n')
        f.write(a)

rewrite()
read_file()