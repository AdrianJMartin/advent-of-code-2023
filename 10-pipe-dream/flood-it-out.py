from PIL import Image
from PIL.ImageDraw import ImageDraw,floodfill
import random


# these are only the pipe we are interested in
# none of the junk

tests = []
tests.append( 
"""F-------7
|F-----7|
||.....||
||.....||
|L-7.F-J|
|..|.|..|
L--J.L--J"""
)
tests.append( """.F----7F7F7F7F-7....
.|F--7||||||||FJ....
.||.FJ||||||||L7....
FJL7L7LJLJ||LJ.L-7..
L--J.L7...LJF7F-7L7.
....F-J..F7FJ|L7L7L7
....L7.F7||L7|.L7L7|
.....|FJLJ|FJ|F7|.LJ
....FJL-7.||.||||...
....L---J.LJ.LJLJ..."""
)

with open("big-path.txt") as f:
    tests.append( f.read())

dot_color = ( 255,255,255 )
background_color = (20,100,20)
pipe_color = ( 255,0,0)
flood_color = (100,100,255)

def add_tup ( t1 ,t2 ):
    return ( t1[0] + t2[0] , t1[1] + t2[1])

def make_field( t):

    t = t.splitlines()
    r = []
    for y,line in enumerate( t):
        r.append( f".{line}.")

    n =  "." * len(r[0])

    r = [n,*r,n]
    return r


for t in tests:
    field = make_field(t) 

    width = len( field[0] )
    height = len( field )

    width *= 12
    height *= 12

    image_size = ( width,height )

    field_img = Image.new( mode="RGB", size=image_size , color= background_color)
    drawing = ImageDraw( field_img , "RGB")

    for y, line in enumerate(field):
        for x, c in enumerate(line):

            offset = ( x * 12 , y * 12 )


            if c == "|":
                tl = add_tup( offset , ( 4 ,  0 ))
                br = add_tup( offset , ( 7 , 11 ))
                drawing.rectangle( [tl,br],fill=pipe_color)

            elif c == "-":
                tl = add_tup( offset , (  0 , 4 ))
                br = add_tup( offset , ( 11 , 7 ))
                drawing.rectangle( [tl,br],fill=pipe_color)

            elif c == "F":
                tl = add_tup( offset , (  4 , 4 ))
                br = add_tup( offset , ( 11 , 7 ))
                drawing.rectangle( [tl,br],fill=pipe_color)
                tl = add_tup( offset , ( 4 , 8 ))
                br = add_tup( offset , ( 7 , 11 ))
                drawing.rectangle( [tl,br],fill=pipe_color)

            elif c == "7":
                tl = add_tup( offset , (  0 , 4 ))
                br = add_tup( offset , (  7 , 7 ))
                drawing.rectangle( [tl,br],fill=pipe_color)
                tl = add_tup( offset , ( 4 , 8 ))
                br = add_tup( offset , ( 7 , 11 ))
                drawing.rectangle( [tl,br],fill=pipe_color)

            elif c == "J":
                tl = add_tup( offset , (  4 , 0 ))
                br = add_tup( offset , (  7 , 3 ))
                drawing.rectangle( [tl,br],fill=pipe_color)
                tl = add_tup( offset , ( 0 , 4 ))
                br = add_tup( offset , ( 7 , 7 ))
                drawing.rectangle( [tl,br],fill=pipe_color)

            elif c == "L":
                tl = add_tup( offset , (  4 , 0 ))
                br = add_tup( offset , (  7 , 3 ))
                drawing.rectangle( [tl,br],fill=pipe_color)
                tl = add_tup( offset , (  4 , 4 ))
                br = add_tup( offset , ( 11 , 7 ))
                drawing.rectangle( [tl,br],fill=pipe_color)

            tl = add_tup( offset , (5,5))
            br = add_tup( offset , (6,6) )
            drawing.ellipse( [tl,br] , fill=dot_color )

    field_img.save( f"output-{tests.index(t)}-b.png")
    floodfill(field_img,xy=(1,1),value=flood_color, thresh=20)
    field_img.save( f"output-{tests.index(t)}.png")

    inside = 0

    for y, line in enumerate(field):
        for x, c in enumerate(line):
            offset = ( x * 12 , y * 12 )
            tl = add_tup( offset , (4,4))
            v = field_img.getpixel( tl )
            if v == background_color:
                inside += 1
    
    print( f"test {tests.index(t)} {inside}")
            






