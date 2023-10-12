def find_word_in_file(file_name, word_to_find):
    line_numbers = []

    try:
        with open(file_name, 'r') as file:
            for line_number, line in enumerate(file, 1):
                if word_to_find in line:
                    line_numbers.append(line_number)

        if line_numbers:
            print(f'Word "{word_to_find}" found in the following lines: {line_numbers}')
        else:
            print(f'Word "{word_to_find}" not found in the file.')

    except FileNotFoundError:
        print(f'File "{file_name}" not found.')
    except Exception as e:
        print(f'An error occurred: {str(e)}')

file_name = "samplefile.txt"
word_to_find = "python"
find_word_in_file(file_name, word_to_find)
