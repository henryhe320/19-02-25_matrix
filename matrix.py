def draw_lines( matrix, screen, color ):
    counter = 0
    while counter+2 <= len(matrix):
        draw_line(matrix[counter][0], matrix[counter][1], matrix[counter+1][0], matrix[counter+1][1],screen,color)
        counter += 2
    return screen
        

def add_edge( matrix, x0, y0, z0, x1, y1, z1 ):
    add_point(matrix,x0,y0,z0)
    add_point(matrix,x1,y1,z1)

def add_point( matrix, x, y, z=0 ):
    matrix.append([x,y,z,1])
    return matrix




def draw_line( x0, y0, x1, y1, screen, color ):

    #swap points if going right -> left
    if x0 > x1:
        xt = x0
        yt = y0
        x0 = x1
        y0 = y1
        x1 = xt
        y1 = yt

    x = x0
    y = y0
    A = 2 * (y1 - y0)
    B = -2 * (x1 - x0)

    #octants 1 and 8
    if ( abs(x1-x0) >= abs(y1 - y0) ):

        #octant 1
        if A > 0:            
            d = A + B/2

            while x < x1:
                plot(screen, color, x, y)
                if d > 0:
                    y+= 1
                    d+= B
                x+= 1
                d+= A
            #end octant 1 while
            plot(screen, color, x1, y1)
        #end octant 1

        #octant 8
        else:
            d = A - B/2

            while x < x1:
                plot(screen, color, x, y)
                if d < 0:
                    y-= 1
                    d-= B
                x+= 1
                d+= A
            #end octant 8 while
            plot(screen, color, x1, y1)
        #end octant 8
    #end octants 1 and 8

    #octants 2 and 7
    else:
        #octant 2
        if A > 0:
            d = A/2 + B

            while y < y1:
                plot(screen, color, x, y)
                if d < 0:
                    x+= 1
                    d+= A
                y+= 1
                d+= B
            #end octant 2 while
            plot(screen, color, x1, y1)
        #end octant 2

        #octant 7
        else:
            d = A/2 - B;

            while y > y1:
                plot(screen, color, x, y)
                if d > 0:
                    x+= 1
                    d+= A
                y-= 1
                d-= B
            #end octant 7 while
            plot(screen, color, x1, y1)
        #end octant 7
    #end octants 2 and 7
#end draw_line

#print the matrix such that it looks like
#the template in the top comment
def print_matrix( matrix ):
    final = ''
    rowstrs = []
    for i in range(4):
        rowstr = '['
        for col in matrix:
            if len(str(col[i])) == 1:
                rowstr += f'    {col[i]}'
            elif len(str(col[i])) == 2:
                rowstr += f'   {col[i]}'
            elif len(str(col[i])) == 3:
                rowstr += f'  {col[i]}'
            elif len(str(col[i])) == 4:
                rowstr += f' {col[i]}'
        rowstr += ']\n'
        rowstrs.append(rowstr)
    for rs in rowstrs:
        final += rs
    print(final)

#turn the paramter matrix into an identity matrix
#you may assume matrix is square
def ident( matrix ):
    dim = len(matrix)
    return [[1 if row == col else 0 for col in range(dim)] for row in range(dim)]
    

#multiply m1 by m2, modifying m2 to be the product
#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    if len(m1) != len(m2[0]):
        print("can't multiply these two :(")
        return
    return [[dotprohelper(m1[i][row],[m2[col]
              for i in range(len(m2[0]))])
              for col in range(len(m2))]
              for row in range(len(m1[0]))]
              
def dotprohelper(l1,l2): # does the multiplying and adding of the rows and columns
    if len(l1) != len(l2):
        print("can't multiply these two >:(")
        return
    finsum = 0
    for i in range(len(l1)):
        finsum += l1[i] * l2[i]
    return finsum

def new_matrix(rows = 4, cols = 50):
    m = []
    for c in range( cols ):
        # print('hello')
        def zig(col):
            a = 0
            if col % 2 == 0:
                a = 250
            else: a = 240
            return a
        add_edge(m,c*10,zig(c),0,(c+1)*10,zig(c+1),0)
    # print(m)
    return m
    
#constants
XRES = 500
YRES = 500
MAX_COLOR = 255
RED = 0
GREEN = 1
BLUE = 2

DEFAULT_COLOR = [0, 0, 0]

def new_screen( width = XRES, height = YRES ):
    screen = []
    for y in range( height ):
        row = []
        screen.append( row )
        for x in range( width ):
            screen[y].append( DEFAULT_COLOR[:] )
    return screen

def plot( screen, color, x, y ):
    newy = YRES - 1 - y
    if ( x >= 0 and x < XRES and newy >= 0 and newy < YRES ):
        screen[newy][x] = color[:]

