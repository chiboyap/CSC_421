
# Searching in Employee File using following fields: Employee Number and Employee Name

# Searching using Employee Number
def search1():
    fout = open('EMPLOYEE_FILE.TXT', 'r')
    no = int(input('Employee Number? '))
    found = 0
    for line in fout:
        line = line.strip()
        arr = line.split(',')
        if arr[0] == str(no):
            found = 1
            print(75 * '-')
            print('Employee Number :', arr[0], '\t\t\t\tEmployee Name :', arr[1])
            print('Gender :', arr[2], '\t\t\t\t\tDesignation :', arr[5])
            print('Date of Birth :', arr[3], '\t\t\tDate of Joining :', arr[4])
            print('Basic Salary : $' + str(arr[6]))
            print('Phone Number :', arr[7], '\t\t\tMobile Number :', arr[8])
            print('Address :', arr[9])
            print(75 * '-')
    if found:
        print('\nEMPLOYEE SUCCESSFULLY DISPLAYED!\n')
    else:
        print('\nEMPLOYEE RECORD NOT FOUND!\n')
    fout.close()


# Searching using Employee Name
def search2():
    fout = open('EMPLOYEE_FILE.TXT', 'r')
    na = input('Employee Name? ')
    found = 0
    for line in fout:
        line = line.strip()
        arr = line.split(',')
        if arr[1] == na.upper():
            found = 1
            print(75 * '-')
            print('Employee Number :', arr[0], '\t\t\t\tEmployee Name :', arr[1])
            print('Gender :', arr[2], '\t\t\t\t\tDesignation :', arr[5])
            print('Date of Birth :', arr[3], '\t\t\tDate of Joining :', arr[4])
            print('Basic Salary : $' + str(arr[6]))
            print('Phone Number :', arr[7], '\t\t\tMobile Number :', arr[8])
            print('Address :', arr[9])
            print(75 * '-')
    if found:
        print('\nEMPLOYEE SUCCESSFULLY DISPLAYED!\n')
    else:
        print('\nEMPLOYEE RECORD NOT FOUND!\n')
    fout.close()