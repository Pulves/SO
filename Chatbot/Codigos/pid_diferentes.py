def PID(arquivo):
    with open(arquivo) as f:
        processos = f.readlines()
    processos = [x.strip(" ") for x in processos]
    processos = [y[:5] for y in processos]
    processos = [z.strip("? ") for z in processos]
    processos.pop(0)
    return processos

def diferentes (pid1,pid2):
    diferente = []
    for n in pid1:
        if n not in pid2:
            diferente.append(n)
    diferente = [x+"\n" for x in diferente]
    return diferente

def arquivo(processos):
    f = open("pid_diferentes.txt", "wt")
    for n in processos:
        f.write(n)

maquina_linux = PID("processos_maquinalinux.txt")
meu_processo = PID("processos_meucenario.txt")
diferente = diferentes(meu_processo, maquina_linux)
arquivo(diferente)


