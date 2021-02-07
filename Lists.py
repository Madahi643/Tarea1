
if __name__ == '__main__':
    N = int(input())
    c=[]
    for i in range(N):
        m=input().split()
        for i in range(1, len(m)):
         m[i]= int(m[i])
         
        if m[0]=="pop":
            c.pop()
        elif m[0]=="append":
            c.append(m[1])    
        elif m[0]=="remove":
            c.remove(m[1])
        elif m[0]=="insert":
            c.insert(m[1],m[2])
        elif m[0]=="sort":
            c.sort()
        elif m[0]=="reverse":
            c.reverse()
        elif m[0]=="print":
            print(c)   
             