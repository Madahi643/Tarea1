def count_substring(string, sub_string):
    a=0
    b=-1
    while b<len(string):
     c=string.find(sub_string,b+1)
     if c==-1:
        break
     a=a+1
     b=c
    return a

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
