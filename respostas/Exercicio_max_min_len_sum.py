y = [i for i in range(-27, 70, 5)]

def meu_min(x):
    curr_min = 1000000
    for i in x:
        if i < curr_min:
            curr_min = i
            
    return curr_min

def meu_max(x):
    curr_max = -1000000
    for i in x:
        if i > curr_max:
            curr_max = i
    
    return curr_max

def meu_len(x):
    counter = 0
    for i in x:
        counter += 1
    return counter

def meu_sum(x):
    acumulador = 0
    for i in x:
        acumulador += i
    return acumulador

print(min(y), meu_min(y))
print(max(y), meu_max(y))
print(len(y), meu_len(y))
print(sum(y), meu_sum(y))