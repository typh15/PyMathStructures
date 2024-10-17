
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

