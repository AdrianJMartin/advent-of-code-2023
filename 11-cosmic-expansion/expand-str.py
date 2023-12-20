import itertools
#    |     |

s = "#.#...#"
e = ""

for c in s:
    if c == ".":
        e += "e"
    else:
        e += c


print(s)
print(e)

t = "#..#......#"

galaxies = [ i for i,c in enumerate(s) if c == "#" ]

print(galaxies)

galactic_pairs = list(itertools.combinations(galaxies,2))
print(galactic_pairs)


exp_factor = 1000000

for gp in galactic_pairs:
    print(gp)
    print(s[gp[0]+1:gp[1]+1])
    print(e[gp[0]+1:gp[1]+1])

    steps = 0
    for c in e[gp[0]+1:gp[1]+1]:
        if c == "e":
            steps += exp_factor
        elif c == ".":
            steps += 1 
        elif c == "#":
            steps += 1
    print(steps)
    print("-"*10)






