from subprocess import PIPE, Popen
p1 = Popen(["./ps_recursivo.sh"], stdin=PIPE, stdout=PIPE, bufsize=1)
while True:
    print('true')
