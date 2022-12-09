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

        class Gels:

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
                    prod = Cat.Group.Gels(lambda x: self.trans(other.trans(x)), self.space, self.domain)
                    return prod
                if self.domain != other.domain:
                    return None

            def __invert__(self):
                self.rem()
                print(self.lst)
                return Cat.Group.Gels(lambda x: self.lst.index(x+min(self.domain)), self.space, self.domain)



        class FinGrp:

            def __init__(self, maps, baseset):
                self.maps = maps
                self.filled = False
                self.domain = baseset
                self.I = Cat.Group.Gels(lambda n: n, self, self.domain)
                self.els = {self.I}

                if isinstance(maps[0], FunctionType):
                    self.els = self.els.union(set([Cat.Group.Gels(f, self, self.domain) for f in maps]))
                if type(maps[0]) == list:
                    if len(maps[0]) < len(self.domain):
                        print('ill defined group: Returned Trivial Group')
                    else:
                        for m in maps:
                            f = lambda n: m[n-min(self.domain)]
                            newel = Cat.Group.Gels(f, self, self.domain)
                            self.els.update({newel})
                            del f
                    for p in self.els:
                        p.rem()
                self.elslst = {tuple([f.trans(x) for x in self.domain]) for f in self.els}
                self.ord = len(self.els)
                self.di = {str(e.lst):e for e in self.els}



            def update(self):
                for p in self.els:
                    p.rem()
                oldord = self.ord
                temp = self.els.copy()
                if not self.filled:
                    for i in self.els:
                        for j in self.els:
                            for k in self.els:
                                x = i*(j*k)
                                y = ~(i*(j*k))
                                if x not in self.els:
                                    temp.add(x)
                                if y not in self.els:
                                    temp.add(y)
                self.els.update(temp)
                self.filled = (oldord == self.ord)
                self.elslst = {tuple([f.trans(x) for x in self.domain]) for f in self.els}
                self.ord = len(self.els)
                self.di = {str(e.lst):e for e in self.els}


            def totalupdate(self):
                while not self.filled:
                    for p in self.els:
                        p.rem()
                    self.update()

            def __eq__(self, other):
                tots = set([])
                toto = set([])
                print(len(self.els))

                for t in self.els:
                    t.rem()
                    print('X does:   ', tuple(t.trans(o) for o in self.domain))
                    tots.add(tuple(t.trans(o) for o in self.domain))
                for s in other.els:
                    s.rem()
                    print('Y does:   ',tuple(s.trans(o) for o in other.domain))
                    toto.add(tuple(s.trans(o) for o in other.domain))
                print('Domain = ', self.domain)
                print('X = ', tots)
                print('Y = ', toto)
                if set(tuple(tots)) == set(tuple(toto)):
                    return True
                else:
                    return False

            def __add__(self, other):
                for p in self.els:
                    p.rem()
                for k in other.els:
                    k.rem()
                basesize = len(self.domain)
                otherproj = Cat.Group.FinGrp([[m+basesize for m in thismap] for thismap in other.maps],[m+basesize for m in other.domain])
                outmaps = []
                for i in self.maps:
                    for j in other.maps:
                        outmaps.append(i+j)
                outdom = N(basesize+len(other.domain))
                return Cat.Group.FinGrp(outmaps,outdom)


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


print(symmgen(4))


def cycgen(n):
    base = N(n)
    for j in range(n-1):
        k = j+1
        base[k] = k-1
    base[0] = n-1
    return base


print(cycgen(4))


def sn(n):
    return Cat.Group.FinGrp(symmgen(n),symmgen(n)[0])


def cn(n):
    return Cat.Group.FinGrp([cycgen(n)],symmgen(n)[0])


X = cn(4)+cn(2)
Y = Cat.Group.FinGrp([[1,2,0]],[0,1,2])
X.totalupdate()
Y.totalupdate()
print(X.elslst)




