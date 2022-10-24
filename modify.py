from os import remove, rename

# Modification in Basic Salary
from valid import dateval


# Modification of existing records in Employee File except Employee Number and Employee Name


def modif1():
    fin = open('EMPLOYEE_FILE.TXT', 'r')
    fout = open('TEMPORARY.TXT', 'w')
    # Input Employee's Designation
    desig = input('Designation to change Basic Salary? ')
    # Input amount by which Basic Salary has to be increased
    inc = int(input('Amount by which Basic Salary to be increased? '))
    found = 0
    for data in fin:
        data = data.strip()
        arr = data.split(',')
        if arr[5] == desig.upper():
            found = 1
            arr[6] = str(int(arr[6]) + inc)
        print('Are you sure you want to change:\n\tY/y for Yes or N/n for No')
        ch = input('Enter your Choice [Y/y or N/n] ')
        if ch == 'Y' or ch == 'y':
            print('BASIC SALARY UPDATED SUCCESSFULLY!\n')
        else:
            print('BASIC SALARY NOT UPDATED!\n')
        rec = (',').join(arr)
        fout.write(rec + '\n')
    if found == 0:
        print('\nERROR: DESIGNATION NOT FOUND!\n')
    fin.close()
    fout.close()
    remove('EMPLOYEE_FILE.TXT')
    rename('TEMPORARY.TXT', 'EMPLOYEE_FILE.TXT')


# Modification in Designation
def modif2():
    fin = open('EMPLOYEE_FILE.TXT', 'r')
    fout = open('TEMPORARY.TXT', 'w')
    # Input Employee Number
    no = input('Employee Number to change Designation? ')
    found = 0
    for data in fin:
        data = data.strip()
        arr = data.split(',')
        if int(arr[0]) == no:
            found = 1
            print('Name :', arr[1])
            print('Designation:', arr[5], '\t\t', 'Basic Salary :', arr[6])
            newdes = input('New Designation? ')
            newbs = input('New Basic Salary? ')
            if not newdes.isalnum() or newdes.isdigit():
                print('Please enter proper Designation')
                newdes = input('New Designation? ')
            elif newdes.isalpha():
                print('Please enter proper Designation')
                newdes = input('New Designation? ')
            else:
                break
            print('Are you sure you want to change:\n\tY/y for Yes or N/n for No')
            ch = input('Enter your Choice [Y/y or N/n]? ')
            if ch == 'Y' or ch == 'y':
                arr[5] = newdes.upper()
                arr[6] = newbs
                print('DESIGNATION UPDATED SUCCESSFULLY!\n')
            else:
                print('DESIGNATION NOT UPDATED!\n')
        rec = (',').join(arr)
        fout.write(rec + '\n')
    if found == 0:
        print('\nERROR: EMPLOYEE NUMBER NOT FOUND!\n')
    fin.close()
    fout.close()
    remove('EMPLOYEE_FILE.TXT')
    rename('TEMPORARY.TXT', 'EMPLOYEE_FILE.TXT')


# Modification in Gender
def modif3():
    fin = open('EMPLOYEE_FILE.TXT', 'r')
    fout = open('TEMPORARY.TXT', 'w')
    found = 0
    # Input Employee Number
    no = input('Employee Number to change Gender? ')
    found = 0
    for data in fin:
        data = data.strip()
        arr = data.split(',')
        if int(arr[0]) == no:
            found = 1
            print('Name :', arr[1])
            print('Gender:', arr[2])
            gender = input('Gender [F/M]? ')
            while True:
                if not gender.isalpha():
                    print('Please enter Gender as either F- Female or M- Male')
                    gender = input('Gender [F/M]? ')
                elif gender.isalpha() and len(gender) != 1:
                    print('Please enter Gender as either F- Female or M- Male')
                    gender = input('Gender [F/M]? ')
                elif gender.upper() != 'F' and gender.upper() != 'M':
                    print('Please enter Gender as either F- Female or M- Male')
                    gender = input('Gender [F/M]? ')
                else:
                    print('Are you sure you want to change?\n\tY/y for Yes or N/n for No')
                    ch = input('Enter your Choice [Y/y or N/n]? ')
                    if ch == 'Y' or ch == 'y':
                        arr[2] = gender
                        print('GENDER UPDATED!\n')
                    else:
                        print('GENDER NOT UPDATED!\n')
                        break
        rec = (',').join(arr)
        fout.write(rec + '\n')
    if found == 0:
        print('\nERROR: EMPLOYEE NUMBER NOT FOUND!\n')
    fin.close()
    fout.close()
    remove('EMPLOYEE_FILE.TXT')
    rename('TEMPORARY.TXT', 'EMPLOYEE_FILE.TXT')


# Modification in Date of Birth
def modif4():
    fin = open('EMPLOYEE_FILE.TXT', 'r')
    fout = open('TEMPORARY.TXT', 'w')
    # Input Employee Number
    no = input('Employee Number to change Date of Birth? ')
    found = 0
    for data in fin:
        data = data.strip()
        arr = data.split(',')
        if int(arr[0]) == no:
            found = 1
            print('Name :', arr[1])
            print('Date of Birth:', arr[3])
            print('Enter a Correct Data of Birth')
            newdob = dateval()
            while len(newdob) != 10:
                print(newdob)
                print('Please enter Correct Date of Birth')
                newdob = dateval()
            print('Are you sure you want to change?\n\tY/y for Yes or N/n for No')
            ch = input('Enter your Choice [Y/y or N/n]? ')
            if ch == 'Y' or ch == 'y':
                arr[4] = newdob
                print('DATE OF BIRTH UPDATED SUCCESSFULLY!\n')
            else:
                print('DATE OF BIRTH NOT UPDATED!\n')
        rec = (',').join(arr)
        fout.write(rec + '\n')
    if found == 0:
        print('\nERROR: EMPLOYEE NUMBER NOT FOUND!\n')
    fin.close()
    fout.close()
    remove('EMPLOYEE_FILE.TXT')
    rename('TEMPORARY.TXT', 'EMPLOYEE_FILE.TXT')


# Modification in Date of Joining
def modif5():
    fin = open('EMPLOYEE_FILE.TXT', 'r')
    fout = open('TEMPORARY.TXT', 'w')
    # Input Employee Number
    no = int(input('Employee Number to change Date of Joining? '))
    found = 0
    for data in fin:
        data = data.strip()
        arr = data.split(',')
        if int(arr[0]) == no:
            found = 1
            print('Name:', arr[1])
            print('Date of Joining:', arr[4])
            print('Enter a Correct Data of Joining')
            newdoj = dateval()
            while len(newdoj) != 10:
                print(newdoj)
                print('Please enter Correct Data of Joining')
                newdoj = dateval()
            print('Are you sure you want to change?\n\tY/y for Yes or N/n for No')
            ch = input('Enter your Choice [Y/y or N/n]? ')
            if ch == 'Y' or ch == 'y':
                arr[5] = newdoj
                print('DATE OF JOINING UPDATED SUCCESSFULLY!\n')
            else:
                print('DATE OF JOINING NOT UPDATED!\n')
        rec = (',').join(arr)
        fout.write(rec + '\n')
    if found == 0:
        print('\nERROR: EMPLOYEE NUMBER NOT FOUND!\n')
    fin.close()
    fout.close()
    remove('EMPLOYEE_FILE.TXT')
    rename('TEMPORARY.TXT', 'EMPLOYEE_FILE.TXT')


# Modification in Phone Number
def modif6():
    fin = open('EMPLOYEE_FILE.TXT', 'r')
    fout = open('TEMPORARY.TXT', 'w')
    # Input Employee Number
    no = int(input('Employee Number to change Phone Number? '))
    # Input New Phone Number
    newpn = input('New Phone Number? ')
    found = 0
    for data in fin:
        data = data.strip()
        arr = data.split(',')
        if int(arr[0]) == no:
            found = 1
            print('Name :', arr[1])
            print('Phone Number:', arr[7])
            print('Are you sure you want to change?\n\tY/y for Yes or N/n for No')
            ch = input('Enter your Choice [Y/y or N/n]? ')
            if ch == 'Y' or ch == 'y':
                arr[7] = newpn
                print('Phone Number updated!\n')
            else:
                print('Phone Number not updated!\n')
        rec = (',').join(arr)
        fout.write(rec + '\n')
    if found == 0:
        print('\nERROR: EMPLOYEE NUMBER NOT FOUND!\n')
    fin.close()
    fout.close()
    remove('EMPLOYEE_FILE.TXT')
    rename('TEMPORARY.TXT', 'EMPLOYEE_FILE.TXT')


# Modification in Mobile Number
def modif7():
    fin = open('EMPLOYEE_FILE.TXT')
    fout = open('TEMPORARY.TXT', 'w')
    # Input Employee Number
    no = int(input('Employee Number to change Mobile Number? '))
    # Input New Mobile Number
    newmob = input('New Mobile Number? ')
    found = 0
    for data in fin:
        data = data.strip()
        arr = data.split(',')
        if int(arr[0]) == no:
            found = 1
            print('Name :', arr[1])
            print('Mobile Number:', arr[8])
            print('Are you sure you want to change?\n\tY/y for Yes or N/n for No')
            ch = input('Enter your Choice [Y/y or N/n]? ')
            if ch == 'Y' or ch == 'y':
                arr[8] = newmob
                print('MOBILE NUMBER UPDATED SUCCESSFULLY!\n')
            else:
                print('MOBILE NUMBER NOT UPDATED!\n')
        rec = (',').join(arr)
        fout.write(rec + '\n')
    if found == 0:
        print('\nERROR: EMPLOYEE NUMBER NOT FOUND!\n')
    fin.close()
    fout.close()
    remove('EMPLOYEE_FILE.TXT')
    rename('TEMPORARY.TXT', 'EMPLOYEE_FILE.TXT')


# Modification in Address
def modif8():
    fin = open('EMPLOYEE_FILE.TXT')
    fout = open('TEMPORARY.TXT', 'w')
    # Input Employee Number
    no = int(input('Enter the Number for changing the Address- '))
    # Input New Address
    newadd = input('New address? ')
    found = 0
    for data in fin:
        data = data.strip()
        arr = data.split(',')
        if int(arr[0]) == no:
            found = 1
            print('Name :', arr[1])
            print('Address :', arr[9])
        print('Are you sure you want to change?\n\tY/y for Yes or N/n for No')
        ch = input('Enter your Choice [Y/y or N/n]? ')
        if ch == 'Y' or ch == 'y':
            arr[9] = newadd.upper()
            print('ADDRESS UPDATED SUCCESSFULLY!\n')
        else:
            print('ADDRESS NOT UPDATED!\n')
        rec = (',').join(arr)
        fout.write(rec + '\n')
    if found == 0:
        print('\nERROR: EMPLOYEE NUMBER NOT FOUND!\n')
    fin.close()
    fout.close()
    remove('EMPLOYEE_FILE.TXT')
    rename('TEMPORARY.TXT', 'EMPLOYEE_FILE.TXT')

# Input Number of days worked and other deductions of each Employee in Monthly Pay File
def mpayfile():
    arr = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
    m, y = 0, 1
    maxdays_work = 0
    while True:
        if m not in [1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12] and y < 2015:
            # Input Month
            m = int(input('Month? '))
            # Input Year
            y = int(input('Year? '))
        else:
            break
    if m in [1, 3, 5, 7, 8, 9, 10, 12]:
        maxdays_work = 27
    elif m in [4, 6, 9, 11]:
        maxdays_work = 26
    elif m == 2:
        if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
            maxdays_work = 25
        else:
            maxdays_work = 24
    file_name = 'Monthly_pay' + '_' + arr[m - 1] + '_' + str(y) + '.txt'
    fout = open(file_name, 'a')
    # Input Emplyee Number
    no = input('Employee Number? ')
    fin = open('EMPLOYEE_FILE.TXT', 'r')
    for line in fin:
        line = line.strip()
        arr = line.split(',')
        if arr[0] == str(no):
            print('Employee Name  :', arr[1])
            act_basic = int(arr[6])
            print('Basic  :', act_basic)
            # Validation for Number of working days
            # Calculation of Basic Salary
            leaves = int(input('Number of leaves taken in the month? '))
            if leaves >= 0 and leaves <= maxdays_work:
                days = maxdays_work - leaves
                mon_sal = (act_basic // maxdays_work) * days
            else:
                while leaves >= 0 and leaves <= maxdays_work:
                    print('Please enter valid Number of leaves')
                    leaves = int(input('Number of leaves taken in the month? '))
                    days = maxdays_work - leaves
            if days >= 0 and leaves <= days:
                mon_sal = (act_basic // maxdays_work) * days
                da = round(0.55 * mon_sal)
                hra = round(0.35 * mon_sal)
                conv = round(0.15 * mon_sal)
                gross = round(mon_sal + da + hra + conv)
                itax = round(0.05 * mon_sal)
                loan = round(0.1 * mon_sal)
                ded = round(itax + loan)
                net = round(gross - ded)
                print('\nBasic\tDA\tHRA\tConveyance\tGross\tItax\tLoan\tDeductions\tNet')
                print('-' * 90)
                print(str(mon_sal) + '\t' + str(da) + '\t' + str(hra) + '\t' + str(conv) + '\t\t' + str(
                    gross) + '\t' + str(itax) + '\t' + str(loan) + '\t' + str(ded) + '\t\t' + str(net),
                      '\n\nAdded in Monthly Pay File!\n')
                data = str(no) + ',' + arr[1].upper() + ',' + arr[5].upper() + ',' + str(days) + ',' + str(
                    mon_sal) + ',' + str(da) + ',' + str(hra) + ',' + str(conv) + ',' + str(gross) + ',' + str(
                    itax) + ',' + str(loan) + ',' + str(net) + '\n'
                fout.write(data)
    fout.close()


# Delete Employee records
def delete():
    fin = open('EMPLOYEE_FILE.TXT', 'r')
    fout = open('TEMPORARY.TXT', 'a')
    # Input Employee Number
    no = int(input('Employee Number to delete? '))
    # Input Employee Name
    na = input('Employee Name to delete? ')
    found = 0
    for data in fin:
        arr = data.split(',')
        if int(arr[0]) == no and arr[1] == na.upper():
            print('Name:', arr[1], '\t\t\t\t', 'Employee Number:', arr[0])
            print('Designation:', arr[5], '\t\t\t', 'Basic Salary :', arr[6])
            print('Date of Birth:', arr[3], '\t\t\t\t', 'Date of Joining:', arr[4])
            print('Are you sure you want to delete?\n\tY/y for Yes or N/n for No')
            ch = input('Enter your Choice [Y/y or N/n]? ')
            if ch == 'Y' or ch == 'y':
                print('RECORD SUCCESSFULLY DELETED!\n')
            else:
                print('RECORD NOT DELETED!\n')
        else:
            fout.write(data)
    fout.close()
    fin.close()
    if found == 0:
        print('\nERROR: RECORD NOT FOUND!\n')
    remove('EMPLOYEE_FILE.TXT')
    rename('TEMPORARY.TXT', 'EMPLOYEE_FILE.TXT')
