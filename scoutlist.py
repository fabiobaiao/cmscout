import sys

file = open(sys.argv[1], 'rb')

file.read(6)

name = file.read(101).decode('latin-1')

manName = file.read(252).decode('latin-1')

file.read(8)

count = int.from_bytes(file.read(4), byteorder='little')

for j in range(count):
    firstNameId = int.from_bytes(file.read(4), byteorder='little')
    secondNameId = int.from_bytes(file.read(4), byteorder='little')
    commonNameId = int.from_bytes(file.read(4), byteorder='little')
    id = int.from_bytes(file.read(4), byteorder='little')

    day = int.from_bytes(file.read(2), byteorder='little')
    year = int.from_bytes(file.read(2), byteorder='little')
    leapyear = int.from_bytes(file.read(4), byteorder='little')

    dateOfBirth = {'Day': day, 'Year': year, 'LeapYear': leapyear}

    file.read(20)
    file.read(1)

    print(firstNameId)
    print(secondNameId)
    print(commonNameId)
    print(id)
    print(dateOfBirth)
    print()
