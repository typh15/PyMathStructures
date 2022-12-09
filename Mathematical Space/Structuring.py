from types import FunctionType


def sp(n):
    for i in range(n):
        print('\n')


def groupprog(i, j, k, ):
    sp(16)
    print('i:   ', i.lst)
    print('j:   ', j.lst)
    print('k:   ', k.lst)
    print('i*(j*k) product in progress')
    x = i * (j * k)
    sp(1)
    print('i*(j*k):   ', x.lst)
    sp(2)
    print('i:   ', i.lst)
    print('j:   ', j.lst)
    print('k:   ', k.lst)
    print('(i*j)*k product in progress')
    z = (i * j) * k
    sp(1)
    print('(i*)j*k:   ', z.lst)
    sp(6)
    print('i:   ', i.lst)
    print('j:   ', j.lst)
    print('k:   ', k.lst)
    print('~(i*(j*k)) product in progress')
    y = ~(i * (j * k))
    sp(1)
    print('~(i*(j*k)):   ', y.lst)
    sp(3)
    if x != z:
        print('NOT ASSOCIATIVE \n' * 10)
    if x == z:
        print('IS ASSOCIATIVE \n' * 3)


class Cat:

    class Partition:

        def __init__(self, numlist):
            if type(numlist) == int:
                self.lst = [numlist]
            if type(numlist) == list:
                self.lst = sorted(numlist, reverse=True)
            self.size = len(self.lst)
            self.start = lambda n: self.lst[: n]
            self.end = lambda n: self.lst[self.size-n: self.size]

        def reduce(self):
            out = []
            for i in self.lst:
                if i != 0:
                    out.append(i)
            self.lst = out

        def trans(self):
            out = []
            listn1 = self.lst.copy()
            for i in range(max(self.lst)):
                currat = 0
                listn = listn1
                for j in range(len(listn)):
                    if listn[j] > 0:
                        currat += 1
                    listn[j] = listn[j] - 1
                out.append(currat)

            outed = Cat.Partition(out)
            outed.reduce()
            return outed

        def __matmul__(self, other):
            out = []
            if self.size <= other.size:
                for i in sorted([*set(self.lst)], reverse=True):
                    prt = [i]
                    multiple = min(self.lst.count(i), other.lst.count(i))
                    if multiple > 0:
                        out = out + (prt*multiple)
            if self.size > other.size:
                for i in sorted([*set(other.lst)], reverse=True):
                    prt = [i]
                    multiple = min(self.lst.count(i), other.lst.count(i))
                    if multiple > 0:
                        out = out + (prt*multiple)
            outed = Cat.Partition(out)
            outed.reduce()
            return outed

        def __add__(self, other):
            out = []
            l = max(self.size, other.size)

            for i in range(l):
                term = 0
                if i > self.size - 1:
                    term += other.lst[i]
                    out.append(term)
                    continue
                if i > other.size - 1:
                    term += self.lst[i]
                    out.append(term)
                    continue
                if i <= min(self.size, other.size)-1:
                    term += self.lst[i]+other.lst[i]
                    out.append(term)
                    continue
            outed = Cat.Partition(out)
            outed.reduce()
            return outed

        def __sub__(self, other):
            out1 = []
            l = max(self.size, other.size)
            for i in range(l):
                term = 0
                if i > self.size - 1:
                    term += -other.lst[i]
                    out1.append(term)
                    continue
                if i > other.size - 1:
                    term += self.lst[i]
                    out1.append(term)
                    continue
                if i <= min(self.size, other.size)-1:
                    term += self.lst[i]-other.lst[i]
                    out1.append(term)
                    continue
            out = [max(0,x) for x in out1]
            outed = Cat.Partition(out)
            outed.reduce()
            return outed

        def __mul__(self, other):
            if type(other) == int:
                out = [other*n for n in self.lst]
                outed = Cat.Partition(out)
                outed.reduce()
                return outed
            if type(other) == Cat.Partition:
                out = self.lst + other.lst
                outed = Cat.Partition(out)
                outed.reduce()
                return outed

        def __truediv__(self, other):
            out = []
            for i in sorted([*set(self.lst)], reverse=True):
                prt = [i]
                multiple = max(0, self.lst.count(i) - other.lst.count(i))
                if multiple > 0:
                    out = out + (prt * multiple)
            outed = Cat.Partition(out)
            outed.reduce()
            return outed

        def __eq__(self, other):
            self.reduce()
            other.reduce()
            if self.lst == other.lst:
                return True
            else:
                return False

        def __le__(self, other):
            self.reduce()
            other.reduce()
            if self.size > other.size:
                return False
            valid = True
            for i in sorted([*set(self.lst)], reverse=True):
                if self.lst.count(i) <= other.lst.count(i):
                    valid = valid and True
                else:
                    valid = False
            return valid

        def __ge__(self, other):
            self.reduce()
            other.reduce()
            if other <= self:
                return True
            else:
                return False

        def __lt__(self, other):
            self.reduce()
            other.reduce()
            diff = other - self
            diff.reduce()
            if diff.size == other.size:
                return True
            else:
                return False

        def __gt__(self, other):
            self.reduce()
            other.reduce()
            if other < self:
                return True
            else:
                return False

        def __copy__(self):
            out = self.lst.copy()
            outed = Cat.Partition(out)
            outed.reduce()
            return outed

        def superprod(self, n):
            tot = self.__copy__()
            for j in range(n):
                if j % 2 == 1:
                    tot = tot @ self
                if j % 2 == 0:
                    tot = tot + self
            return tot

    class Group:

        def __init__(self, elements, operations):
            self.els = elements
            self.op = operations
            l = list(elements)
            ordered = []



        class Permutation:

            def __init__(self, mapping, home, domain):
                self.domain = sorted(domain)
                self.space = home
                self.lst = tuple([mapping(i) for i in self.domain])
                self.trans = lambda n: self.lst[n-min(domain)]
                self.lst2 = tuple(self.trans(i) for i in self.domain)
                if self.lst != self.lst2:
                    sp(3)
                    print('As function - f(0):   ', self.trans(0))
                    print('As list - f(0):   ', self.lst[0])
                    print('As list2 - f(0):   ', self.lst2[0])
                    print('ENCODING ERROR:  ', self.lst,' not equal to ',self.lst2)

            def rem(self):
                self.trans = lambda n: self.lst[n-min(self.domain)]

            def __hash__(self):
                return hash(self.lst)

            def __eq__(self, other):
                return self.lst == other.lst

            def __mul__(self, other):
                self.rem()
                other.rem()
                if self == self.space.I:
                    return other
                if other == self.space.I:
                    return self
                if self.domain == other.domain:
                    self.rem()
                    other.rem()
                    prod = Cat.Group.Permutation(lambda x: self.trans(other.trans(x)),
                                                 self.space, self.domain)
                    return prod
                if self.domain != other.domain:
                    return None

            def __invert__(self):
                self.rem()
                return Cat.Group.Permutation(lambda x: self.lst.index(x),
                                             self.space, self.domain)

            def __pow__(self, power, modulo=None):
                self.rem()
                if type(power) != int:
                    power.rem()
                    conj1 = (~power)*self
                    conj2 = conj1*power
                    return conj2


        class PermGrp:

            def __init__(self, maps, baseset):
                self.maps = maps
                self.generated = False
                self.abelean = False
                self.domain = baseset
                self.I = Cat.Group.Permutation(lambda n: n, self, self.domain)
                self.els = {self.I}
                self.op = lambda a,b: self.I
                if isinstance(maps[0], FunctionType):
                    self.els = self.els.union(set([Cat.Group.Permutation(f, self, self.domain)
                                                   for f in maps]))
                if type(maps[0]) == list or type(maps[0]) == tuple:
                    if len(maps[0]) < len(self.domain):
                        print('ill defined group: Returned Trivial Group')
                    else:
                        for m in maps:
                            f = lambda n: m[n-min(self.domain)]
                            newel = Cat.Group.Permutation(f, self, self.domain)
                            self.els.update({newel})
                            del f
                    for p in self.els:
                        p.rem()
                self.elslst = {tuple([f.trans(x) for x in self.domain]) for
                               f in self.els}
                self.ord = len(self.els)
                self.di = {str(e.lst):e for e in self.els}
                self.__updatetracker = set([])

            def group(self):
                return Cat.Group(self.els, self.op)


            def partialgen(self):
                self.ord = len(self.els)
                for p in self.els:
                    p.rem()
                temp1 = self.els.copy()
                temp2 = self.els.copy()
                self.abelean = True
                for i in temp1:
                    if self.generated:
                        break
                    for j in temp1:
                        if (i,j) in self.__updatetracker:
                            temp2.discard(j)
                    for j in temp2:
                        if self.generated:
                            break
                        if (i,j) not in self.__updatetracker:
                            self.__updatetracker.add((i,j))
                            self.__updatetracker.add((j,i))
                            a = i*j
                            b = j*i
                            c = ~a
                            d = ~b
                            self.abelean = self.abelean and (a == b)
                            self.els.add(a)
                            self.els.add(b)
                            self.els.add(c)
                            self.els.add(d)
                self.generated = (len(self.els) == self.ord)
                print('Is Group Generated?    ', self.generated)
                print('Current Size:    ', self.ord)
                sp(1)
                self.elslst = {tuple([f.trans(x) for x in self.domain])
                               for f in self.els}
                self.ord = len(self.els)
                self.di = {str(e.lst):e for e in self.els}

            def generate(self):
                while not self.generated:
                    for p in self.els:
                        p.rem()
                    self.partialgen()
                self.op = lambda a,b: a*b
                self.elslst = {tuple([f.trans(x) for x in self.domain])
                               for f in self.els}

            def __eq__(self, other):
                tots = set([])
                toto = set([])
                for t in self.els:
                    t.rem()
                    tots.add(tuple(t.trans(o) for o in self.domain))
                for s in other.els:
                    s.rem()
                    toto.add(tuple(s.trans(o) for o in other.domain))
                if set(tuple(tots)) == set(tuple(toto)):
                    return True
                else:
                    return False

            def conj(self,perm):
                if self.domain == perm.domain:
                    newmaps = []
                    for g in self.els:
                        newmaps.append((g**perm).lst)
                    return Cat.Group.PermGrp(newmaps,self.domain)
                if set(perm.domain).issubset(set(self.domain)):
                    diff = [n + len(perm.domain) for n in
                            range(len(self.domain)-len(perm.domain))]
                    newpermlist = list(perm.lst)+diff
                    IsoGroup = Cat.Group.PermGrp([newpermlist],self.domain)
                    IsoGroup.generate()
                    newperm = IsoGroup.di[str(tuple(newpermlist))]
                    newmaps = []
                    for g in self.els:
                        newmaps.append((g**newperm).lst)
                    out = Cat.Group.PermGrp(newmaps,self.domain)
                    out.generate()
                    return out

            def __add__(self, other):
                newsize = len(self.domain) + len(other.domain)
                newdom = N(newsize)
                diff1 = [n + len(self.domain) for n in range(len(other.domain))]
                g1permlst = [list(permlis.lst) + diff1 for permlis in self.els]
                print(g1permlst)
                diff2 = N(len(self.domain))
                g2permlst1 = [[n + len(self.domain) for
                               n in list(permlis.lst)] for permlis in other.els]
                g2permlst2 = [diff2 + list(permlis) for permlis in g2permlst1]
                print(g2permlst2)
                out = Cat.Group.PermGrp(g1permlst + g2permlst2, newdom)
                out.generate()

                return out










def N(n):
    return [m for m in range(n)]


def symmgen(n):
    base = N(n)
    out = []
    for k in range(n-1):
        j = k+1
        outerm = base.copy()
        outerm[j] = j-1
        outerm[j-1] = j
        out.append(outerm)
    return out


def cycgen(n):
    base = N(n)
    for j in range(n-1):
        k = j+1
        base[k] = k-1
    base[0] = n-1
    return base



def sn(n):
    return Cat.Group.PermGrp(symmgen(n), N(n))


def cn(n):
    print('Generator:  ',cycgen(n))
    return Cat.Group.PermGrp([cycgen(n)], N(n))


X = sn(3)
Y = sn(2)
X.generate()
Y.generate()
print(X == X)
print('Is S5 Abelian?  ', X.abelean)
print('Is G Abelian?  ',  Y.abelean)
sp(8)
Z = X+Y
Z.generate()
g = X.di['(0, 2, 1)']
h = X.di['(1, 2, 0)']
print('g*h : ',X.op(g,h).lst)
print('g*h : ',(g*h).lst)
print(X.di.keys())
print('X =   ', X.elslst)
print('Size   ',len(X.els))
print('Y =   ', Y.elslst)
print('Size   ',len(Y.els))
print('Z =   ', Z.elslst)
print('Size   ',len(Z.els))
print('Is Conjugate Same?   ',X == Z)
X = X.group()
print(X.op(g,h).lst)

f = lambda n: n*n





