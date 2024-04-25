import threading

def precess(input_file):
    with open(input_file, 'r') as f:
        data = f.read()
    return data

def ch(inputdata):
    chr = ''.join(c for c in inputdata if c.isalpha())
    with open('out.txt', 'w') as f:
        f.write(chr)

def nu(inputdata):
    num = ''.join(c for c in inputdata if c.isdigit())
    with open('out1.txt', 'w') as f:
        f.write(num)

def se(inputdata):
    sep = ''.join(c for c in inputdata if not c.isalnum() and not c.isspace())
    with open('out2.txt', 'w') as f:
        f.write(sep)

input_file = 'input.txt'
inputdata = precess(input_file)

t1 = threading.Thread(target=ch, args=(inputdata,))
t2 = threading.Thread(target=nu, args=(inputdata,))
t3 = threading.Thread(target=se, args=(inputdata,))

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()
