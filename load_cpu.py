import os,sys
from multiprocessing import cpu_count

load1, load5, load15 = os.getloadavg()
nproc = cpu_count()


print("Numero de CPUs: ", nproc)
print("Load 1: %.2f\nLoad 5: %.2f\nLoad 15: %.2f\n" % (load1,load5,load15));

if load5 >= 5:
    print("Load em estado de atencao: %.1f", load5)
    sys.exit(1)
#elif load15 >=5:
#    print("teste")
else:
    print("Load OK: %.1f" % (load5))
    sys.exit(0)
