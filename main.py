def read_file(filename):
    with open(filename, 'r') as file:
        return set(file.readlines())

def write_file(filename, lines):
    with open(filename, 'w') as file:
        file.writelines(lines)

def main(file1, file2):

    # Зчитуємо вміст обох файлів
    lines1 = read_file(file1)
    lines2 = read_file(file2)

    # Знаходимо рядки, які містяться в обох файлах
    same_lines = lines1.intersection(lines2)
    # Знаходимо рядки, які містяться лише в одному з двох файлів
    diff_lines = lines1.symmetric_difference(lines2)

    # Записуємо результати у відповідні файли
    write_file("same.txt", same_lines)
    write_file("diff.txt", diff_lines)

if __name__ == "__main__":
    main('file1.txt', 'file2.txt')