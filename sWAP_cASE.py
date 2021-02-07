def swap_case(s):
    s=list(s)
    for i in range(len(s)):
      if(str.islower(s[i])):
        s[i]=str.upper(s[i])
      else:
        s[i]=str.lower(s[i])
    s="".join(s)
    return s



if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)