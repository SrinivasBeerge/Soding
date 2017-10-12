
import sys
def sum_of_even_fibonacci(limit):
    if limit < 2:
        return 0
    elif limit < 8:
        return 2
    else:
        sum = 10l
        curr = 8l
        prev = 5l
        while(True):
            next = prev + curr
            if next > limit:
                return sum
            else:
                prev = curr
                curr = next
                if next % 2 == 0:
                    sum = sum + next

if __name__ == '__main__':
    #print sum_of_even_fibonacci(int(sys.argv[1]))
    print sum_of_even_fibonacci(4000000)
