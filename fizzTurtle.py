from turtle import Turtle
import time


def main():
    startTime = time.time()

    #Initializing triangle turtle
    t = Turtle()
    t.color("red")
    tLength = 30

    #Initializing pentagon turtle
    p = Turtle()
    p.color("blue")
    pLength = 30

    for i in range(1, 101):
        toPrint = ""
        #Every iteration, move the triangle, check it's position
        advanceTriangle(t, tLength)
        tcheck = checkPosition(t)

        #Every iteration, move the pentagon, check it's position
        advancePentagon(p, pLength)
        pcheck = checkPosition(p)

        # If the shape is back to the origin
            # Increase the distance traveled
            # (Not important, it just adds to the visual)
        if tcheck:
            toPrint += tcheck
            tLength += 5

        if pcheck:
            toPrint += pcheck 
            pLength += 5
        print(i) if not toPrint else print(toPrint)


    print(f"--- {time.time() - startTime :.2f} ---")


def checkPosition(t):
    position = t.pos()
    #Checking if the turtle is at the origin
    if int(position[0]) == 0 and int(position[1]) == 0:
        #Checking for the color, and returning the appropriate string
        return "Fizz" if t.color()[0] == "red" else "Buzz"

def advanceTriangle(t, length=100):
    t.forward(length)
    t.left(120)

def advancePentagon(p, length=100):
    p.forward(length)
    p.left(72)


if __name__ == "__main__":
    main()
