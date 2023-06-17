class CEP_ADT:
    def __init__(s):
        s.d = {}
        s.names = {}
    def print_all(s):
        print("\nFirst dictionary:")
        for k in s.d:
            print(s.d[k])
        print("\nSecond dictionary:")
        for k in s.names:
            print(s.names[k])

    def __repr__(s):
        l = []
        for m in s.d:
            l.append((m,s.d[m]))
        return str(l)
    def insert(s, i, n, c,p=False):
        s.d[i] = (n, c)
        s.names[n] = i
        if p:
            print(f"\nAfter insertion of {[i,n,c]}, the data structures are: ")
            s.print_all()

    def find(s,i,p=False):
        if p:
            print(f"found record {s.d[i]} for id {i}")
        return s.d[i]

    def find_by_name(s,n,p=False):
        if n in s.names:
            i = s.names[n]
            if s.d[i][0] == n:
                if p:
                    print(f"found record {(i,n,s.d[i][1])} for name {n}")
                return (i, n, s.d[i][1])
        return None

    def list_in_range(s, i1, i2,p=False):
        l = []
        for k, v in s.d.items():
            if i1 <= k <= i2:
                l.append((k, v[0], v[1]))
        if p:
            print(f"\nGiven start ID {i1} and end ID {i2}, the records found are:\n")
            for r in l:
                print(r)
        return l

    def list_by_city(s,c,p=False):
        l = []
        for k, v in s.d.items():
            if v[1] == c:
                l.append((k, v[0], v[1]))
        if p:
            print(f"\nFound the following records for city {c}:")
            for r in l:
                print(r)
        return l

    def delete(s,i,p=False):
        if i in s.d:
            n = s.d[i][0]
            del s.d[i]
            del s.names[n]
        if p:
            print(f"\nAfter deletion of record with id {i}, the data structures are:")
            s.print_all()  
