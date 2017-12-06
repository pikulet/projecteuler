##Problem 4
##A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
##Find the largest palindrome made from the product of two 3-digit numbers.

def largest_palindrome():
    greatest = 0
    for i in range(999,100,-1):
        if i%10 == 0: continue
        for j in range(999,100,-1):
            if j%10 == 0: continue
            product = i*j
            if is_palindrome(product):
                greatest = max(greatest, product)
    return greatest

def is_palindrome(n):
    n = str(n)
    mid = len(n)//2
    if len(n)%2 == 0:
        return compare(n[:mid],n[mid:])
    else:
        return compare(n[:mid],n[mid+1:])

def compare(a,b):
    return a == b[::-1]
