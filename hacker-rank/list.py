if __name__ == '__main__':
    N = int(input())
    
    arr = []
    i = 0
    while i < N:
        i += 1
        ins = input().split()
        if ins[0] == 'print':
            print(arr)
        else:
            getattr(arr, ins[0])(*[int(i) for i in ins[1:]])
