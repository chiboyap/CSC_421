# FUNCTION FOR VALIDATION OF DATA

# Validation for inputted date
def dateval():
    # Input Day
    d = int(input('Day? '))
    # Input Month
    m = int(input('Month? '))
    # Input Year
    y = int(input('Year? '))
    maxd = 0
    if m in [1, 3, 5, 7, 8, 9, 10, 12]:
        maxd = 31
    elif m in [4, 6, 9, 11]:
        maxd = 30
    elif m == 2:
        if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
            maxd = 29
        else:
            maxd = 28
    if maxd == 0:
        print('Please input valid Month')
    elif d < 1 or d > maxd:
        print('Please input valid Day')
    elif y < 1950 and y > 2001:
        print('Please input valid Year between 1950 and 2001')
    else:
        if len(str(m)) == 1:
            m = '0' + str(m)
        if len(str(d)) == 1:
            d = '0' + str(d)
        return (str(d) + '-' + str(m) + '-' + str(y))


# Validation for Phone Number
def phonevalidate(n):
    fin = open('EMPLOYEE_FILE.TXT', 'r')
    fin.seek(0)
    found = 0
    for line in fin:
        line = line.strip()
        rec = line.split(',')
        ph = rec[7]
        if ph == n:
            found = 1
            print('Same Phone Number found in records')
            break
    if len(fin.read()) == 0:
        found = 0
    return (found)
