import csv

# Решение уравнений методом Гаусса

INPUT_FILENAME = 'source_matrix.csv'
OUTPUT_FILENAME = 'output.csv'
matrix = []


def read_input_data(filename):
    """Reading source matrix file and saving in the list"""
    with open(filename) as File:
        reader = csv.reader(File, delimiter=',')
        for row in reader:
            matrix.append(row)
            print(row)


def write_output_data(filename, _matrix):
    with open(filename, mode="w", encoding='utf-8') as FILE:
        file_writer = csv.writer(FILE, delimiter=",", lineterminator="\r")
        for row in _matrix:
            file_writer.writerow(row)
            print(row)


if __name__ == '__main__':
    read_input_data(INPUT_FILENAME)
    write_output_data(OUTPUT_FILENAME, matrix)
