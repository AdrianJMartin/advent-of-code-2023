data = open(0).read().split('\n')

def expand( seq : [[int]] ):
    at_zero = 0

    while not at_zero :
        row = seq[-1]
        next_row = []

        for i in range( len( row ) -1 ):
            next_row.append( row[i+1] - row[i] )

        seq.append(next_row)

        at_zero = all( [ t == 0 for t in next_row ] )

    return seq

running_total = 0

for d in data:
    a = [ int(n) for n in d.split() ]
    a = list(reversed(a))
    a = [a]
    a = expand(a) 

    n = sum( [ n[-1] for n in a])

    print(a)
    print(n)

    print("-" * 50 )

    running_total += n

print( running_total )





