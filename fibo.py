def fib(n):
    a,b = 0,1
    while a<n :
        print(a, end=' ')
        a,b = b,a+b
    print()
    if __name__ == "__name__":
        import sys
        fib(int(sys.argv[1]))
        