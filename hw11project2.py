# Exercise No.  11.2
# File Name:    hw11project2
# Programmer:   Anna Li
# Date:         June 25th, 2020

# Overall Plan:
# 1. Make graphics shapes for each suit
# 2. Store the shapes in a dictionary with the key being the name of the suit
# 3. Make a Gui that prompts the user to enter the name of the suit
# 4. Make sure there is a confirm and quit button
# 5. Run a loop so that nothing happens unless one of those buttons are pushed
# 6. If quit, quit. If confirm, use an if statement to see if the entry matches a key in the dictionary
# 7. Iterate through the dictionary to the correct suit, iterate through all the shapes and draw everything in the right color
# 8. Display to Window


from graphics import*
from button import*

#I did this at first to play with dimensions and shapes, not used in the program
# but I worked too hard to delete all of this :(
def drawHeart(win, pt, radius):
    circleL = Circle(Point((pt.getX()- .75*radius), pt.getY() ), radius)

    circleL.setFill("red")
    circleL.setOutline("red")
    circleL.draw(win)

    circleR = Circle(Point((pt.getX()+ .75*radius), pt.getY() ), radius)
    circleR.setFill("red")
    circleR.setOutline("red")
    circleR.draw(win)

    bottomY = (pt.getY()-2)
    Point1 = Point((pt.getX()-1.5 *radius), pt.getY()-.65*radius)
    Point2 = Point((pt.getX()+1.5 *radius), pt.getY()-.65*radius)
    Point3 = Point(pt.getX(), (pt.getY()-(2.5*radius)))
    triangle = Polygon(Point1, Point2, Point3)
    Polygon(Point((pt.getX()-1.5 *radius), pt.getY()-.65*radius),
            Point((pt.getX()+1.5 *radius), pt.getY()-.65*radius),
            Point(pt.getX(), (pt.getY()-(2.5*radius))))

    triangle.setFill("red")
    triangle.setOutline("red")
    triangle.draw(win)

def drawDia(win, pt, radius):
    diamond = Polygon(Point(pt.getX(), pt.getY()+radius), Point(pt.getX()-(radius/2), pt.getY()),
                      Point(pt.getX(), pt.getY()-radius), Point(pt.getX()+(radius/2), pt.getY()))
    diamond.setFill("red")
    diamond.setOutline("red")
    diamond.draw(win)

def drawSpade(win, pt, radius):
    circleL = Circle(Point((pt.getX() - .75*radius), pt.getY()), radius)
    circleL.setFill("black")
    circleL.draw(win)

    circleR = Circle(Point((pt.getX() + .75*radius), pt.getY()), radius)
    circleR.setFill("black")
    circleR.draw(win)

    bottomY = (pt.getY() - 2)
    Point1 = Point((pt.getX() - 1.5 * radius), pt.getY()+ .7*radius)
    Point2 = Point((pt.getX() + 1.5 * radius), pt.getY()+ .7*radius)
    Point3 = Point(pt.getX(), (pt.getY() + (2.5 * radius)))
    triangle = Polygon(Point1, Point2, Point3)

    triangle.setFill("black")
    triangle.draw(win)

    niceX = .5*radius
    niceY = 1.5*radius
    stem = Polygon(pt, Point(pt.getX()- .5*radius, pt.getY()-1.5*radius), Point(pt.getX()+ .5*radius, pt.getY()-1.5*radius))
    stem.setFill("black")
    stem.draw(win)

def drawClub(win, pt, radius):
    circleL = Circle(Point((pt.getX() - .75 * radius), pt.getY()), radius*0.9)
    circleL.setFill("black")
    circleL.draw(win)
    circleR = Circle(Point((pt.getX() + .75 * radius), pt.getY()), radius*0.9)
    circleR.setFill("black")
    circleR.draw(win)
    circleT = Circle(Point((pt.getX()), pt.getY()+ 1.1375*radius), radius*0.9)
    circleT.setFill("black")
    circleT.draw(win)

    niceX = .5 * radius
    niceY = 1.5 * radius
    stem = Polygon(pt, Point(pt.getX() -.5 * radius, pt.getY() - 1.5 * radius), Point(pt.getX() + .5 * radius, pt.getY() - 1.5 * radius))
    stem.setFill("black")
    stem.draw(win)


# but then I realized that I had to use a dictionary to store everything so it was kind of redundant....

def main():
    win = GraphWin("Suit Revealer", 500, 500)
    win.setCoords(0, 0, 500, 500)
    win.setBackground('lightblue')

    # Draw the instructions box and entry box
    text = Text(Point(175, 400), "Enter a suit: ")
    text2 = Text(Point(175, 375), " (Diamond, Spade, Club, Heart)")
    suit = Entry(Point(350, 400), 10)
    text.setSize(20)
    text2.setSize(10)
    text.draw(win)
    text2.draw(win)
    suit.draw(win)

    # Make and activate our two buttons
    confirm = Button(win, Point(200, 100), 75, 30, "Confirm")
    confirm.activate()
    quit = Button(win, Point(300, 100), 45, 30, "Quit")
    quit.activate()

    #Used for the dimensions and position of each suit
    pt = Point(250, 250)
    radius = 30

    # lame way of doing it using dictionaries and lists
    # Each shape has a list that contains each shape needed to draw that suit

    #Diamond is just one polygon
    polygon = [Polygon(Point(pt.getX(), pt.getY()+radius), Point(pt.getX()-(radius/2), pt.getY()),
                      Point(pt.getX(), pt.getY()-radius), Point(pt.getX()+(radius/2), pt.getY()))]

    #heart is two circles and a triangle
    heart = [Circle(Point((pt.getX()- .75*radius), pt.getY() ), radius),
             Circle(Point((pt.getX()+ .75*radius), pt.getY() ), radius),
             Polygon(Point((pt.getX() - 1.5 * radius), pt.getY() - .65 * radius),
                     Point((pt.getX() + 1.5 * radius), pt.getY() - .65 * radius),
                     Point(pt.getX(), (pt.getY() - (2.5 * radius))))]

    # club is three circles and a triangle(stem)
    club = [Circle(Point((pt.getX() - .75 * radius), pt.getY()), radius*0.9),
            Circle(Point((pt.getX() + .75 * radius), pt.getY()), radius * 0.9),
            Circle(Point((pt.getX()), pt.getY()+ 1.1375*radius), radius*0.9),
            Polygon(pt, Point(pt.getX() -.5 * radius, pt.getY() - 1.5 * radius), Point(pt.getX() + .5 * radius, pt.getY() - 1.5 * radius))]

    # spade is the heart upsidedown but with a stem ie: 2 circles, 2 triangles
    spade = [Circle(Point((pt.getX() - .75*radius), pt.getY()), radius),
             Circle(Point((pt.getX() + .75*radius), pt.getY()), radius),
             Polygon(Point((pt.getX() - 1.5 * radius), pt.getY()+ .7*radius),
                     Point((pt.getX() + 1.5 * radius), pt.getY()+ .7*radius),
                     Point(pt.getX(), (pt.getY() + (2.5 * radius)))),
             Polygon(pt, Point(pt.getX()- .5*radius, pt.getY()-1.5*radius), Point(pt.getX()+ .5*radius, pt.getY()-1.5*radius))]

    #dictionary stores the name of each suit and also a list that has the shapes (list) and a string for the color of that suit
    suits = {
        "diamond": [polygon, "red"],
        "heart" : [heart, "red"],
        "club" : [club, "black"],
        "spade" : [spade, "black"]
    }
    # Stoers a user's click
    p1 = win.getMouse()
    # while, quit is not clicked
    while not quit.clicked(p1):
        if confirm.clicked(p1): # if confirm is clicked
            entry = (suit.getText()) # get the text from the entry box
            for i in suits: # iterate through the dictionary to check each key
                if entry.lower() == i: # if the textbox entry (all lowercase) is in the dictionary
                    color = suits[i][1] # color is set to the value list indexed at 1, which is color
                    n = suits[i][0] # n is set to the list indexed at 0, which is the list containing all shape objects
                    for m in range(len(n)): # for m in range of the list's length, because each suit has different number of shape objects
                        n[m].setFill(color) # n is iterated through and each object shape is set to the approprate color and drawn
                        n[m].setOutline(color)
                        n[m].draw(win)


            confirm.deactivate() # At the end of the if statement, since confirm was clicked, we deactivate confirm

        else:
            p1 = win.getMouse() # if confirm is not clicked, then we keep getting the user's clicks until we exit the while loop


    win.close() # window is closed only when we exit the while loop ie: when the quit button is pushed.


main()