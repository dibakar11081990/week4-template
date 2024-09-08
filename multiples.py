"""
    Multiples of 3 or 5

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
The sum of these multiples is 23.

Find and print the sum of all the multiples of 3 or 5 below 1000.
"""

def mutiple_3_5(start, end):

    sum_of_mutiples = 0

    for i in range(start, end):
        if i%3 == 0 or i%5 == 0:
            sum_of_mutiples += i 
    
    print(sum_of_mutiples)


if __name__ == "__main__":
    mutiple_3_5(1, 1000)

