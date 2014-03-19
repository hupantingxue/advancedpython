#!/usr/bin/python2.6
#--*-- utf-8 --*--

'''
    list generator sample
    Author: hupantingxue
    Email:  hupantingxue@126.com
'''

def main():
    '''
        Result as below:
        cl1 <generator object <genexpr> at 0x7f25ec533410>
        [1, 9, 25, 49, 81, 121, 169, 225, 289, 361, 441, 529, 625, 729, 841]
        cl2 <generator object <genexpr> at 0x7f25ec533460>
        [1, 9, 25, 49, 81, 121, 169, 225, 289, 361, 441, 529, 625, 729, 841, 1, 9, 25, 49, 81, 121, 169, 225, 289, 361]
    '''
    cl1 = (x*x for x in range(30)[1:31:2] if 1 == x % 2)
    # Result is 
    ll = []
    print 'cl1', cl1
    for x in cl1:
        ll.append(x)
    print ll
    cl2 = (x*x for x in range(30)[1:21:2] if 1 == x % 2)
    print 'cl2', cl2
    # Result is 
    for x in cl2:
        ll.append(x)
    print ll

if '__main__' == __name__:
    main()
