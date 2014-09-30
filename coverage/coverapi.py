from coverage import coverage

def main():
    for ii in xrange(100):
        if 3 == (ii % 7):
            print(ii)

if "__main__" == __name__:
    main()
