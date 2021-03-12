# ############## Creator: Fareeda Ragab
# Calculator and Timer
# Using Tkinter, math and time module


from tkinter import *
import math
from time import strftime

expression = ""
# Window
window = Tk()
window.geometry("280x294")
window.title("Calculator")


# For the display of the expression
def display(input_exp):
    global expression
    expression += str(input_exp)
    equation.set(expression)


# Main Code
def equal_press():
    global expression
    expression_after_mod = expression
    try:
        if "sin(" in expression_after_mod:
            sine = "math.sin((math.pi/180)*"
            expression_after_mod = expression_after_mod.replace("sin(", sine)
        if "cos(" in expression_after_mod:
            cosine = "math.cos((math.pi/180)*"
            expression_after_mod = expression_after_mod.replace("cos(", cosine)
        if "tan(" in expression_after_mod:
            tan = "math.tan((math.pi/180)*"
            expression_after_mod = expression_after_mod.replace("tan(", tan)
        if "e^(" in expression_after_mod:
            ex = "math.exp("
            expression_after_mod = expression_after_mod.replace("e^(", ex)
        if "!(" in expression_after_mod:
            factorial = "math.factorial("
            expression_after_mod = expression_after_mod.replace(
                "!(", factorial)
        if "In(" in expression_after_mod:
            In = "math.log("
            expression_after_mod = expression_after_mod.replace("In(", In)
        if "log10(" in expression_after_mod:
            log10 = "math.log10("
            expression_after_mod = expression_after_mod.replace(
                "log10(", log10)
        if "^2" in expression_after_mod:
            expression_after_mod = expression_after_mod.replace("^2", "**2")
        if "10^" in expression_after_mod:
            expression_after_mod = expression_after_mod.replace("10^", "10**")
        if "^" in expression_after_mod:
            expression_after_mod = expression_after_mod.replace("^", "**")
        if "√(" in expression_after_mod:
            sqrt = "math.sqrt("
            expression_after_mod = expression_after_mod.replace("√(", sqrt)
        if "log(" in expression_after_mod:
            log = "math.log("
            expression_after_mod = expression_after_mod.replace("log(", log)
        result = str(f"{eval(expression_after_mod):.6f}")
    except ZeroDivisionError:
        result = "Division By Zero Not Allowed!"
    except Exception:
        result = "Math Error!"
    equation.set(result)


def clear_all():
    global expression
    expression = ""
    equation.set(expression)


def delete_char():
    global expression
    expression = expression[:-1]
    equation.set(expression)


# Buttons
zero_but = Button(window,
                  text="0",
                  width=6,
                  bg="Chocolate",
                  font=('arial', 10, 'bold'),
                  fg="white",
                  command=lambda: display("0")).place(x=70, y=235)

one_but = Button(window,
                 text="1",
                 width=6,
                 bg="Chocolate",
                 font=('arial', 10, 'bold'),
                 fg="white",
                 command=lambda: display("1")).place(x=0, y=210)

four_but = Button(window,
                  text="4",
                  width=6,
                  bg="Chocolate",
                  font=('arial', 10, 'bold'),
                  fg="white",
                  command=lambda: display("4")).place(x=0, y=185)

seven_but = Button(window,
                   text="7",
                   width=6,
                   bg="Chocolate",
                   font=('arial', 10, 'bold'),
                   fg="white",
                   command=lambda: display("7")).place(x=0, y=160)

dot_but = Button(window,
                 text=".",
                 width=6,
                 bg="LightSkyBlue",
                 font=('arial', 10, 'bold'),
                 fg="white",
                 command=lambda: display(".")).place(x=0, y=235)

two_but = Button(window,
                 text="2",
                 width=6,
                 bg="Chocolate",
                 font=('arial', 10, 'bold'),
                 fg="white",
                 command=lambda: display("2")).place(x=70, y=210)

five_but = Button(window,
                  text="5",
                  width=6,
                  bg="Chocolate",
                  font=('arial', 10, 'bold'),
                  fg="white",
                  command=lambda: display("5")).place(x=70, y=185)

eight_but = Button(window,
                   text="8",
                   width=6,
                   bg="Chocolate",
                   font=('arial', 10, 'bold'),
                   fg="white",
                   command=lambda: display("8")).place(x=70, y=160)

equal_but = Button(window,
                   text="=",
                   width=6,
                   bg="LightSkyBlue",
                   font=('arial', 10, 'bold'),
                   fg="white",
                   command=equal_press).place(x=140, y=235)

three_but = Button(window,
                   text="3",
                   width=6,
                   bg="Chocolate",
                   font=('arial', 10, 'bold'),
                   fg="white",
                   command=lambda: display("3")).place(x=140, y=210)

six_but = Button(window,
                 text="6",
                 width=6,
                 bg="Chocolate",
                 font=('arial', 10, 'bold'),
                 fg="white",
                 command=lambda: display("6")).place(x=140, y=185)

nine_but = Button(window,
                  text="9",
                  width=6,
                  bg="Chocolate",
                  font=('arial', 10, 'bold'),
                  fg="white",
                  command=lambda: display("9")).place(x=140, y=160)

plus_but = Button(window,
                  text="+",
                  width=6,
                  bg="LightSkyBlue",
                  font=('arial', 10, 'bold'),
                  fg="white",
                  command=lambda: display("+")).place(x=210, y=235)

minus_but = Button(window,
                   text="-",
                   width=6,
                   bg="LightSkyBlue",
                   font=('arial', 10, 'bold'),
                   fg="white",
                   command=lambda: display("-")).place(x=210, y=210)

multiple_but = Button(window,
                      text="*",
                      width=6,
                      bg="LightSkyBlue",
                      font=('arial', 10, 'bold'),
                      fg="white",
                      command=lambda: display("*")).place(x=210, y=185)

divide_but = Button(window,
                    text="/",
                    width=6,
                    bg="LightSkyBlue",
                    font=('arial', 10, 'bold'),
                    fg="white",
                    command=lambda: display("/")).place(x=210, y=160)

rightBrackt_but = Button(window,
                         text="(",
                         width=6,
                         bg="LightSkyBlue",
                         font=('arial', 10, 'bold'),
                         fg="white",
                         command=lambda: display("(")).place(x=0, y=135)

leftBracket_but = Button(window,
                         text=")",
                         width=6,
                         bg="LightSkyBlue",
                         font=('arial', 10, 'bold'),
                         fg="white",
                         command=lambda: display(")")).place(x=70, y=135)

module_but = Button(window,
                    text="%",
                    width=6,
                    bg="LightSkyBlue",
                    font=('arial', 10, 'bold'),
                    fg="white",
                    command=lambda: display("%")).place(x=140, y=135)

comma_but = Button(window,
                   text=",",
                   width=6,
                   bg="LightSkyBlue",
                   font=('arial', 10, 'bold'),
                   fg="white",
                   command=lambda: display(",")).place(x=210, y=135)

pi_but = Button(window,
                text="π",
                width=6,
                bg="LightSkyBlue",
                font=('arial', 10, 'bold'),
                fg="white",
                command=lambda: display("π")).place(x=210, y=110)

squareRoot_but = Button(window,
                        text="√",
                        width=6,
                        bg="LightSkyBlue",
                        font=('arial', 10, 'bold'),
                        fg="white",
                        command=lambda: display("√(")).place(x=140, y=110)

factorial_but = Button(window,
                       text="X!",
                       width=6,
                       bg="LightSkyBlue",
                       font=('arial', 10, 'bold'),
                       fg="white",
                       command=lambda: display("!(")).place(x=70, y=110)

power_but = Button(window,
                   text="X^Y",
                   width=6,
                   bg="LightSkyBlue",
                   font=('arial', 10, 'bold'),
                   fg="white",
                   command=lambda: display("^")).place(x=0, y=110)

power2_but = Button(window,
                    text="X^2",
                    width=6,
                    bg="LightSkyBlue",
                    font=('arial', 10, 'bold'),
                    fg="white",
                    command=lambda: display("^2")).place(x=0, y=85)

power10_but = Button(window,
                     text="10^X",
                     width=6,
                     bg="LightSkyBlue",
                     font=('arial', 10, 'bold'),
                     fg="white",
                     command=lambda: display("10^")).place(x=70, y=85)

delete_but = Button(window,
                    text="DE",
                    width=6,
                    bg="Chocolate",
                    font=('arial', 10, 'bold'),
                    fg="white",
                    command=delete_char).place(x=140, y=85)

clear_but = Button(window,
                   text="CLS",
                   width=6,
                   bg="Chocolate",
                   font=('arial', 10, 'bold'),
                   fg="white",
                   command=clear_all).place(x=210, y=85)

cos_but = Button(window,
                 text="Cos",
                 width=6,
                 bg="LightSkyBlue",
                 font=('arial', 10, 'bold'),
                 fg="white",
                 command=lambda: display("cos(")).place(x=0, y=60)

sin_but = Button(window,
                 text="sin",
                 width=6,
                 bg="LightSkyBlue",
                 font=('arial', 10, 'bold'),
                 fg="white",
                 command=lambda: display("sin(")).place(x=70, y=60)

tan_but = Button(window,
                 text="tan",
                 width=6,
                 bg="LightSkyBlue",
                 font=('arial', 10, 'bold'),
                 fg="white",
                 command=lambda: display("tan(")).place(x=140, y=60)

oneOverX_but = Button(window,
                      text="1/X",
                      width=6,
                      bg="LightSkyBlue",
                      font=('arial', 10, 'bold'),
                      fg="white",
                      command=lambda: display("1/(")).place(x=210, y=60)

in_but = Button(window,
                text="In",
                width=6,
                bg="LightSkyBlue",
                font=('arial', 10, 'bold'),
                fg="white",
                command=lambda: display("In(")).place(x=0, y=35)

log_but = Button(window,
                 text="log(x,b",
                 width=6,
                 bg="LightSkyBlue",
                 font=('arial', 10, 'bold'),
                 fg="white",
                 command=lambda: display("log(")).place(x=70, y=35)

logBase10_but = Button(window,
                       text="log10",
                       width=6,
                       bg="LightSkyBlue",
                       font=('arial', 10, 'bold'),
                       fg="white",
                       command=lambda: display("log10(")).place(x=140, y=35)

inverseLog_but = Button(window,
                        text="e^X",
                        width=6,
                        bg="LightSkyBlue",
                        font=('arial', 10, 'bold'),
                        fg="white",
                        command=lambda: display("e^(")).place(x=210, y=35)

# Entry For The Display
equation = StringVar()
expression_field = Entry(window, textvariable=equation)
expression_field.grid(row=0, column=0, ipadx=66, ipady=8)


# The Clock
# Place - Grid - Pack For places ---Use Just One -- Not allowed More Than One for the same Widget
def time():
    time_now = strftime("%H:%M:%S %p")
    time_label.config(text=time_now)
    time_label.after(1000, time)


time_label = Label(window, font=("arial", 15), bg="white")
time_label.place(x=50, y=262, height=30, width=200)
time()

var = StringVar()
clock = Label(window, textvariable=var, font=("arial", 12))
var.set(" Time")
clock.place(x=0, y=270)

window.mainloop()
# The End :)
