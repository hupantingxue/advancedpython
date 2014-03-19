#!/usr/bin/python2.6
#--*-- utf-8 --*--

'''
    list comprehension sample
	Author: hupantingxue
	Email:  hupantingxue@126.com
'''

def main():
    cl1 = [x*x for x in range(30)[1:31:2] if 1 == x % 2]
    # Result is 'cl1 [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]'
    print 'cl1 ',cl1
    cl2 = [x*x for x in range(30)[1:21:2] if 1 == x % 2]
	# Result is 'cl2 [1, 9, 25, 49, 81, 121, 169, 225, 289, 361]'
    print 'cl2', cl2

if '__main__' == __name__:
    main()
