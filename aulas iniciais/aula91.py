def generator(n=0, maximum=10):
    while True:
        yield n

        if n >= maximum:
            return

        n += 1


#    yield 1
#    #yeld pausa e return finaliza
#    print('Continuando')
#    yield 2
#    print('mais um')
#    yield 3
#    print('Vou terminar')
#    return 'Acabou'
gen = generator(n=1, maximum=1000)
for n in gen:
    print(n)
