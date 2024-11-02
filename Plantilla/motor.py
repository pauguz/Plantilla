from matematiqueria import RestDupla

def recta(dup1, dup2):
    k=RestDupla(dup1, dup2)
    return k[1]*k[2]==0

def diagonal(dup1, dup2):
    k=RestDupla(dup1, dup2)
    return abs(k[1]/k[2])==1





