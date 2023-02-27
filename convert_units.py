import mmap


def convert():
    feet = float(input('Enter feet: '))
    inches = float(input('Enter inches as decimal: '))
    mm = feet * 304.8 + inches * 25.4
    print(f'\n converted dimension = {mm}mm')

convert()