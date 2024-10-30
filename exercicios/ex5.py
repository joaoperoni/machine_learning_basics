
def datetime_test():
    import datetime

    print(dir(datetime))
    print(datetime.date.today())
    print(datetime.datetime.now())
    data=datetime.datetime(2020,7,10,7,30,0)
    print(data)
    print(f"Ano: {data.year}, Mes: {data.month}. Dia:{data.day}, Hora:{data.hour}, Minute: {data.minute}, Segundo: {data.second}")


def random_time():
    import random
    import time as tm

    print(random.random())
    print(random.randint(1,10))
    print(random.randrange(0,10,3))

    x=['K',10,'32j']
    print(random.choice(x))

    print(tm.time())
    
    tm.sleep(2)
    print(tm.time())

def exercicio():
    import arquivo as ar

    print(ar.ler_float("Insira o numero "))
    print(ar.ler_string("Insira uma palavra "))


if __name__=="__main__":

    #datetime_test()
    #random_time()
    exercicio()