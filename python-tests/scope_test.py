#!/usr/bin/python

def test_fun(t):
    t += 100  # This is local


def f(x, y):
    z = 1
    print('You called f(x,y) with the value x = ' + str(x) + ' and y = ' + str(y))
    print('x * y = ' + str(x*y))
    y = y + 1
    print('You called f(x,y) with the value x = ' + str(x) + ' and y = ' + str(y))
    print('x * y = ' + str(x*y))

    print(z) # can reach because variable z is defined in the function
    print('dentro: ' + str(a))

    # Se si scommenta si arrabbia
    # a = a + 1
    print('dentro: ' + str(a))


a = 3
f(3, a)
print(a)  # can reach because variable z is defined in the function

t = 3
print('t: ' + str(t))
test_fun(t)
print('t: ' + str(t))
