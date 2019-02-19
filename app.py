import os
from fill_input import fill

def read():
    if os.path.exists('ARAB.IN'):
        with open('ARAB.IN', 'r') as f:
            for line in f:
                if line.isnumeric and int(line) >= 0 and int(line) <= 4000:
                    write_converted(convert(line))
                else:
                    print('Error: wrong input')
                    break
    else:
        print('\nFile not found!')

def convert(ro):
    ro = int(ro)
    result = ""
    
    if ro >= 1000:
        for i in range(ro // 1000):
            result += 'm '
            ro -= 1000

    if ro >= 900:
        result += 'c m '
        ro -= 900
    #   500   -   899    |   d - dccc
    elif ro >= 500:
        result += 'd '
        ro -= 500
        for i in range(ro // 100):
            result += 'c '
            ro -= 100
    #   400    -   499    |   cd
    elif ro >= 400:
        result += 'c d '
        ro -= 400
    #   100    -    399    |    c   -   ccc
    elif ro >= 100:
        for i in range(ro // 100):
            result += 'c '
            ro -= 100
    
    if ro >= 90:
        result += 'x c '
        ro -= 90
    #   50   -   89    |   l - lxxx
    elif ro >= 50:
        result += 'l '
        ro -= 50
        for i in range(ro // 10):
            result += 'x '
            ro -= 10
    #   40    -   49    |   xl
    elif ro >= 40:
        result += 'x l '
        ro -= 40
    #   10    -    39    |    x   -   xxx
    elif ro >= 10:
        for i in range(ro // 10):
            result += 'x '
            ro -= 10
    
    if ro == 9:
        result += 'i x '
        ro -= 9
    #   50   -   89    |   l - lxxx
    elif ro >= 5:
        result += 'v '
        ro -= 5
        for i in range(ro // 1):
            result += 'i '
            ro -= 1
    #   40    -   49    |   xl
    elif ro == 4:
        result += 'i v '
        ro -= 4
    #   10    -    39    |    x   -   xxx
    elif ro >= 1:
        for i in range(ro // 1):
            result += 'i '
            ro -= 1

    return result.upper()

def write_converted(ar):
    if os.path.exists('ROMAI.OUT'):
        with open('ROMAI.OUT', 'a') as f:
            f.write(ar + '\n')
    else:
        print('\nFile not found!')

read()
#fill()