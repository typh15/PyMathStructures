import os
import csv

import gc
from operator import itemgetter, attrgetter


class DataSet:
    def __init__(self, name, variablelist):
        self.dic = {variablelist[i]: [] for i in range(len(variablelist))}
        self.ds = open(name+'_ds.txt', 'w')
        self.ds.write(str(variablelist))
        self.ds.close()
        self.rows = 0
        self.name = name
        self.vars = variablelist


    def update(self):
        ds = open(self.name+'_ds.txt', 'w')
        ds.write(str(self.dic))
        self.ds.close()


    def append(self, row):
        length = 1
        newrows = []
        if type(row) != dict:
            newrows = varlist(self.vars, row)
        if type(row) == dict:
            newrows = row
        print('newrows:     ', newrows)
        for i in newrows:
            print('i:   ', i)
            print('newrows[i]:   ', newrows[i])
            if type(newrows[i]) == list:
                length = len(i)
                self.dic[i].extend(newrows[i])
            if not type(newrows[i]) == list:
                self.dic[i].append(newrows[i])
            print('self.dic[i]:     ', self.dic[i])
        self.rows += length

    def delete(self):
        self.ds.close()
        if os.path.exists(self.name+'_ds.txt'):
            os.remove(self.name+'_ds.txt')
        else:
            print("ERROR: File Not Found")
        del self


def varlist(variables, data):
    if len(variables) > len(data):
        print('Error: Too Few Data Points')
        return None
    if len(variables) < len(data):
        print('Error: Too Many Data Points')
        return None
    return {variables[i]: data[i] for i in range(len(variables))}


def imprt(directory):
    for filename in os.scandir(directory):
        if filename.is_file():
            file = filename.path.replace(directory + "\\", "")
            datsetname = file.replace('_ds.txt', '')
            print(' \n \n \n DATA FILE NAME:' + file + ' \n \n', )
            if datsetname == file:
                continue
            if datsetname in locals() or datsetname in globals():
                print('Data Set "' + eval(datsetname).name + '" already exists')
                continue
            if datsetname != file:
                f = open(file, "r")
                strdict = f.read()
               # strdict0 = strdict.replace('], ', ']@&@').replace('{', '').replace('}', '')
               # strdict1 = strdict0.split('@&@')
                strdict1 = strdict.replace('{', '').replace('}', '').split('], ')
                varis = []
                data = []
                for n0 in strdict1:
                    n = n0.split(': ')
                    if len(n) == 2:
                        dictkey = n[0].replace("'", "").replace('"', '')
                        dictitem = n[1].replace('[', '').replace(']', '')
                        dictitemlst = dictitem.replace("'", "").replace('"', '').replace(', ', ',').split(',')
                        varis.append(dictkey)
                        data.append(dictitemlst)

                print('name:  ' + datsetname.replace(" ", ""), '\n  vars:  ', varis, '\n    data:  ', data)
                global gdsname, gvaris, gdata
                gdsname = datsetname
                gvaris = varis
                gdata = data
                inststatement = datsetname + ' = DataSet(gdsname.replace(" ", ""), gvaris)'
                appstatement = datsetname + '.append(gdata)'
                updstatement = datsetname + '.update()'
                exec(inststatement, globals())
                exec(appstatement, globals())
                exec(updstatement, globals())
                del gdsname, gvaris, gdata



with open('username.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0
    transposedata = []
    data = []
    for row in csv_reader:
        if line_count == 0:
            varbls = row
            line_count += 1
        else:
            if len(row) != 0:
                transposedata.append(row)
                line_count += 1
    for i in range(len(varbls)):
        col = []
        for j in range(line_count-1):
            col.append(transposedata[j][i])
        data.append(col)
    print(f'Processed {line_count} lines.')
print('Variables:    ', varbls, '\n  TransData:  ', transposedata, '\n    Data:     ', data)


path = r"C:\Users\typh1\Desktop\Projects\Database Construction"


imprt(path)

rocket
rocket.partialgen()






