# Automatic generation of Employee code
def empcode():
    code = 1000
    fin = open('EMPLOYEE_FILE.TXT', 'r')
    fin.seek(0)
    first_char = fin.read(1)
    if not first_char:
        code = 1000
    else:
        for line in fin:
            line = line.strip()
            rec = line.split(',')
            code = int(rec[0])
    return (code)