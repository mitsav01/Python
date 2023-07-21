'''You are painting a wall. 
The instructions on the paint can says that 1 can of paint can cover 5 square meters of wall.
 Given a random height and width of wall, calculate how many cans of paint you'll need to buy.
 '''

height=float(input("Enter height(in m): "))
width=float(input("Enter width(in m):"))


def canc(height,width):
    area=height*width
    number_of_can= area/5
    return print(f"For given height= {height} m and width= {width} m \nTotal area= {area} m \nnumber of can needed= {number_of_can}")

canc(height,width)


