from turtle import Turtle
import time


def main():
    startTime = time.time()
    t = Turtle()
    t.color("red")
    p = Turtle()
    p.color("blue")
    tLength = 30
    pLength = 30
    for i in range(1, 101):
        toPrint = ""
        advanceTriangle(t, tLength)
        tcheck = checkPosition(t)
        advancePentagon(p, pLength)
        pcheck = checkPosition(p)
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
    if int(position[0]) == 0 and int(position[1]) == 0:
        return "Fizz" if t.color()[0] == "red" else "Buzz"

def advanceTriangle(t, length=100):
    t.forward(length)
    t.left(120)

def advancePentagon(p, length=100):
    p.forward(length)
    p.left(72)

if __name__ == "__main__":
    main()
