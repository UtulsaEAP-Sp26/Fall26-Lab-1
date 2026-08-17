'''
In this assignment you will read input from the command line and print output to the console.


Name:
Lab Time:
'''
def io_func():
    '''
    This function will read a number from the command line and print out the number doubled.
    '''
    print('Enter x: ')
    x = int(input())

    print(x) # Student mistakenly is echoing the input to output to match example
    print('x doubled is:', (2 * x))

if __name__ == '__main__':
    io()