def fibonnaci():
    x, y = 0, 1
    while 1:
        yield x
        x, y = x, x + y

def main():
    r = fibonnaci()
    for i in range (10):
        print r.next()

if __name__ == '__main__':
    main()
