# Ensure day3.txt ends with 2 empty lines!
print('Part1')
import re
this_line_idx_vals = []
prev_line = ''
this_line = ''
next_line = ''
total = 0
lineno = 1

part_numbers = []
with open('day3.txt') as f:
    for line in f:
        prev_line = this_line
        this_line = next_line
        next_line = line
        matches = list(re.finditer(r'(\d+)', this_line))
        this_line_idx_vals = [(match.start(0)-1, match.end(0), int(match.group(0))) for match in matches]
        print('##################################')
        print(f'prevli={lineno-1}: {prev_line}', end='')
        print(f'lineno={lineno}: {this_line}', end='')
        print(f'nextli={lineno+1}: {next_line}', end='')

        
        for begin, end, val in this_line_idx_vals:
            print(f'begin={begin} end={end} val={val}')
            found = False
            
            if begin >= 0 and re.search(r'[^0-9.]', str(this_line[begin])) is not None:
                print('matched begin')
                total += val
                part_numbers.append( { "pn":val , "valid": True } )
                continue
            if this_line[end] != '\n' and re.search(r'[^0-9.]', str(this_line[end])) is not None:
                print('matched end')
                total += val
                print(val)
                part_numbers.append( { "pn":val , "valid": True } )
                continue
            if re.search(r'[^0-9.]', prev_line[begin:end+1]) is not None:
                print('matched prev_line')
                total += val
                print(val)
                part_numbers.append( { "pn":val , "valid": True } )
                continue
            if re.search(r'[^0-9.]', next_line[begin:end+1]) is not None:
                print('matched next_line')
                total += val
                print(val)
                part_numbers.append( { "pn":val , "valid": True } )
                continue
            
            part_numbers.append( { "pn":val , "valid": False } )
            
        lineno += 1
print(f'total={total}')

for pn in part_numbers:
    print(pn)