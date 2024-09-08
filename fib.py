"""
Open fib.py and write a python program that prints the n'th fibonacci number.

The fibonacci series is 0, 1, 1, 2, 3, 5, 8, 13, ...

The 1st fibonacci number is 0.

The 6th fibonacci number is 5.

The code to input n is already written, you do not need to modify it.

When you run the python file, you will have to enter a number (the value of n) for the program to continue executing
"""

def fibonacci_series(n):
    
    if n <=1:
        return n
    else:
        return fibonacci_series(n-1) + fibonacci_series(n-2)
    

if __name__ == "__main__":
    n = int(input("Enter the nth fibonacci series you are looking for: "))
    print(fibonacci_series(n))