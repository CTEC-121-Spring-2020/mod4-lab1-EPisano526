"""
CTEC 121
Esther Pisano
<assignment/lab name>
<assignment/lab description
"""

""" IPO template
Input(s): list/description
Process: description of what function does
Output: return value and description
"""




from graphics import *
def main():
    '''
    win = GraphWin("Title", 600, 300)
    p = Point(100, 200)
    x = p.getX()
    y = p.getY()
    print("x and y:", x, y)
    input()

    win = GraphWin("Bill's Window", 600, 600)
    p1 = Point(50, 50)
    p2 = Point(100, 100)
    r1 = Rectangle(p1, p2)
    r1.draw(win)
    r2 = Rectangle(Point(200, 200), Point(250, 250))
    r2.draw(win)

    input()
    '''
    # convert.py
    # IPO or program description
    # create a window object
    win = GraphWin("Celsius Converter", 400, 300)
    # create text objects
    celsiusTempString = "Celsius Temperature:   "
    fahrenheitTempString = "Fahrenheit Temperature:"
    # create Text boxes
    Text(Point(150, 50), celsiusTempString).draw(win)
    Text(Point(150, 250), fahrenheitTempString).draw(win)
    # create center box
    Rectangle(Point(125, 100), Point(275, 200)).draw(win)
    # create button text
    buttonText = Text(Point(200, 150), "Convert It")
    buttonText.draw(win)
    # create input and output fields
    inputCelsiusField = Entry(Point(300, 50), 5)
    inputCelsiusField.setText("0.0")
    inputCelsiusField.draw(win)
    outputFahrenheitField = Text(Point(300, 250), "")
    outputFahrenheitField.draw(win)
    win.getMouse()
    celsiusTemperature = float(inputCelsiusField.getText())
    fahrenheit = 9.0/5.0 * celsiusTemperature + 32
    # display results
    outputFahrenheitField.setText(round(fahrenheit, 2))
    # update button text
    buttonText.setText("Quit")
    # wait for final click to end
    win.getMouse()


main()
