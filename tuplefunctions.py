import os
os.system('cls')  # clear screen on windows
os.system('clear')  # clear screen on linux / os x

'''
value swap
==========
There are times we experience the need of swapping values and we 
normally use this line:

temp = a
a = b
b = temp

In Python, we can just do this...

(a, b) = (b, a)
The left side is a tuple of variables; the right side is a tuple of 
values. Each value is assigned to its respective variable. All the 
expressions on the right side are evaluated before any of the assignments. 
This feature makes tuple assignment quite versatile. But take note 
that the  count of variables to the left should also have the same 
count of variables to the right.
'''
print 'VALUE SWAP====> (a, b) = (b, a)\n'
a = 7
b = 17
print 'a:', a, '\n'
print 'b:', b, '\n'
print '\nAfter Swap...\n\n'
(a, b) = (b, a)
print 'a:', a, '\n'
print 'b:', b, '\n'

raw_input ("\n\nPress Enter to continue...")
os.system('cls')  # clear screen on windows
os.system('clear')  # clear screen on linux / os x
'''
enumerate()
iterate through the tuple returning 2-tuples of ( index, item ). 
This function enumerates all the items in a sequence: it provides 
a number and each element of the original sequence in a 2-tuple.
'''
print 'Enumerate====> iterate through the tuple returning 2-tuples of ( index, item ).\n'
print 'num = (1, 5, 7, 3, 8)\nfor index, item in enumerate(num):'
print '   print(str(index)+" = "+str(item))\n\nthis will return:'
num = (1, 5, 7, 3, 8)
for index, item in enumerate(num):
    print(str(index)+" = "+str(item))
#result is...
#0 = 1
#1 = 5
#2 = 7
#3 = 3
#4 = 8

raw_input ("\n\nPress Enter to continue...")
os.system('cls')  # clear screen on windows
os.system('clear')  # clear screen on linux / os x
'''
sorted()
iterate through the tuple in sorted order.  Note: the returned collection is a sorted list, not a tuple. 
'''
print 'num = (1, 5, 7, 3, 8)'
print 'print sorted(num) will return:\n'
num = (1, 5, 7, 3, 8)
print sorted(num)
#result: [1,3,5,7,8]

raw_input ("\n\nPress Enter to continue...")
os.system('cls')  # clear screen on windows
os.system('clear')  # clear screen on linux / os x
'''
reversed()

'''
print 'iterate through the tuple in reverse order. '
print 'Note that the return value from reversed() is a generic <reversed object>'
print 'and must be fed into the tuple() or list() constructor to create one of those objects. '
print 'num = (9, 1, 8, 2, 7, 3)\n'
print 'print tuple(reversed(num)) will return:\n'
num = (9, 1, 8, 2, 7, 3)
print tuple(reversed(num))
#result: (3, 7, 2, 8, 1, 9)


raw_input ("\n\nPress Enter to exit...")
os.system('cls')  # clear screen on windows
os.system('clear')  # clear screen on linux / os x
