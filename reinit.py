import os
from operator import itemgetter, attrgetter


def imprt():
    directory = r"C:\Users\typh1\Desktop\Projects\Database Construction"
    for filename in os.scandir(directory):
        if filename.is_file():
            file = filename.path.replace(directory + "\\", "")
            datsetname = file.replace('_ds.txt', '')
            if datsetname != file:
                f = open(file, "r")
                print(f.read())





rocketstate = ['Height(km)', 'Temp(C)', 'Pressure(atm)']

time1 = [0.25, 38, 1.01]

time2 = [2, 140, 0.92]

time3 = [3.4, 662, 0.73]

t1 = varlist(rocketstate, time1)
t2 = varlist(rocketstate, time2)
t3 = varlist(rocketstate, time3)

rocketed = DataSet('rocketed', rocketstate)
rocketed.append(time1)

rocketed.append(time2)

rocketed.append(time3)

rocketed.partialgen()



