if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    l=max(arr)
    c=arr.count(l)
    for i in range(c):
          arr.remove(l)  
    print(max(arr) )  