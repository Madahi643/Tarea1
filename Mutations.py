def mutate_string(string, position, character):Modificacion
    z=list(string)Modificaciones2,
    z[position]=character Modificaciones 3, Pruebas
    a=''.join(z)
    
    return a

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)