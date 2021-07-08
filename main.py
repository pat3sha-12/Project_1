import tkinter as tk

LARGE_FONT_STYLE = ("Arial", 40, "bold")
SMALL_FONT_STYLE = ("Arial", 16)
DIGITS_FONT_STYLE = ("Arial", 24, "bold")
DEFAULT_FONT_STYLE = ("Arial", 20)
FONT_STYLE = ("Arial", 16)

OFF_WHITE = "#F8FAFF"
WHITE = "#FFFFFF"
LIGHT_BLUE = "#CCEDFF"
LIGHT_GRAY = "#F5F5F5"
LABEL_COLOR = "#25265E"

class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("320x492")
        self.window.resizable(0,0)
        self.window.title("Calculator")

        self.total_expression = " "
        self.current_expression = " "
        self.display_frame = self.create_display_frame()

        self.total_label, self.label = self.create_display_labels()

        self.digits = {
            7: (1,1), 8: (1,2), 9: (1,3),
            4: (2,1), 5: (2,2), 6: (2,3),
            1: (3,1), 2: (3,2), 3: (3,3),
            0: (4,2), '.':(4,1)
        }
        self.operations = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"}
        self.buttons_frame = self.create_buttons_frame()

        self.buttons_frame.rowconfigure(0, weight = 1)

        for x in range(1,5):
            self.buttons_frame.rowconfigure(x, weight = 1)
            self.buttons_frame.columnconfigure(x, weight = 1)
        
        # Buttons for operations
        operators = self.operations.keys()
        operator =list(operators)

        symbols = self.operations.values()
        symbol = list(symbols)

        self.button_divide = tk.Button(self.buttons_frame, text=symbol[0], bg=OFF_WHITE, fg=LABEL_COLOR, font= DEFAULT_FONT_STYLE, borderwidth = 0, command=lambda x=operator[0]: self.append_operator(x), name="/")
        self.button_divide.grid(row =1, column = 4, sticky=tk.NSEW)

        self.button_multiply = tk.Button(self.buttons_frame, text=symbol[1], bg=OFF_WHITE, fg=LABEL_COLOR, font= DEFAULT_FONT_STYLE, borderwidth = 0, command=lambda x=operator[1]: self.append_operator(x), name="*")
        self.button_multiply.grid(row =2, column = 4, sticky=tk.NSEW)

        self.button_subtract = tk.Button(self.buttons_frame, text=symbol[2], bg=OFF_WHITE, fg=LABEL_COLOR, font= DEFAULT_FONT_STYLE, borderwidth = 0, command=lambda x=operator[2]: self.append_operator(x), name="-")
        self.button_subtract.grid(row =3, column = 4, sticky=tk.NSEW)

        self.button_add = tk.Button(self.buttons_frame, text=symbol[3], bg=OFF_WHITE, fg=LABEL_COLOR, font= DEFAULT_FONT_STYLE, borderwidth = 0, command=lambda x=operator[3]: self.append_operator(x), name="+")
        self.button_add.grid(row =4, column = 4, sticky=tk.NSEW)

        # Buttons for digits
        digits = self.digits.keys()
        digit = list(digits)

        self.button_7 = tk.Button(self.buttons_frame, text=str(7), bg = WHITE, fg=LABEL_COLOR, font=DIGITS_FONT_STYLE, borderwidth = 0, command=lambda x=digit[0]: self.add_to_expression(x), name="7")
        self.button_7.grid(row=1, column=1, sticky=tk.NSEW)

        self.button_8 = tk.Button(self.buttons_frame, text=str(8), bg = WHITE, fg=LABEL_COLOR, font=DIGITS_FONT_STYLE, borderwidth = 0, command=lambda x=digit[1]: self.add_to_expression(x), name="8")
        self.button_8.grid(row=1, column=2, sticky=tk.NSEW)

        self.button_9 = tk.Button(self.buttons_frame, text=str(9), bg = WHITE, fg=LABEL_COLOR, font=DIGITS_FONT_STYLE, borderwidth = 0, command=lambda x=digit[2]: self.add_to_expression(x), name="9")
        self.button_9.grid(row=1, column=3, sticky=tk.NSEW)

        self.button_4 = tk.Button(self.buttons_frame, text=str(4), bg = WHITE, fg=LABEL_COLOR, font=DIGITS_FONT_STYLE, borderwidth = 0, command=lambda x=digit[3]: self.add_to_expression(x), name="4")
        self.button_4.grid(row=2, column=1, sticky=tk.NSEW)

        self.button_5 = tk.Button(self.buttons_frame, text=str(5), bg = WHITE, fg=LABEL_COLOR, font=DIGITS_FONT_STYLE, borderwidth = 0, command=lambda x=digit[4]: self.add_to_expression(x), name="5")
        self.button_5.grid(row=2, column=2, sticky=tk.NSEW)

        self.button_6 = tk.Button(self.buttons_frame, text=str(6), bg = WHITE, fg=LABEL_COLOR, font=DIGITS_FONT_STYLE, borderwidth = 0, command=lambda x=digit[5]: self.add_to_expression(x), name="6")
        self.button_6.grid(row=2, column=3, sticky=tk.NSEW)

        self.button_1 = tk.Button(self.buttons_frame, text=str(1), bg = WHITE, fg=LABEL_COLOR, font=DIGITS_FONT_STYLE, borderwidth = 0, command=lambda x=digit[6]: self.add_to_expression(x), name="1")
        self.button_1.grid(row=3, column=1, sticky=tk.NSEW)

        self.button_2 = tk.Button(self.buttons_frame, text=str(2), bg = WHITE, fg=LABEL_COLOR, font=DIGITS_FONT_STYLE, borderwidth = 0, command=lambda x=digit[7]: self.add_to_expression(x), name="2")
        self.button_2.grid(row=3, column=2, sticky=tk.NSEW)

        self.button_3 = tk.Button(self.buttons_frame, text=str(3), bg = WHITE, fg=LABEL_COLOR, font=DIGITS_FONT_STYLE, borderwidth = 0, command=lambda x=digit[8]: self.add_to_expression(x), name="3")
        self.button_3.grid(row=3, column=3, sticky=tk.NSEW)

        self.button_0 = tk.Button(self.buttons_frame, text=str(0), bg = WHITE, fg=LABEL_COLOR, font=DIGITS_FONT_STYLE, borderwidth = 0, command=lambda x=digit[9]: self.add_to_expression(x), name="0")
        self.button_0.grid(row=4, column=2, sticky=tk.NSEW)

        self.button_dp = tk.Button(self.buttons_frame, text=str('.'), bg = WHITE, fg=LABEL_COLOR, font=DIGITS_FONT_STYLE, borderwidth = 0, command=lambda x=digit[10]: self.add_to_expression(x), name="decimal")
        self.button_dp.grid(row=4, column=1, sticky=tk.NSEW)

        # Button for Clear
        self.button_Clear = tk.Button(self.buttons_frame, text="C", bg=OFF_WHITE, fg=LABEL_COLOR, font= DEFAULT_FONT_STYLE, borderwidth = 0, command = self.clear, name="clear")
        self.button_Clear.grid(row =0, column = 1, sticky=tk.NSEW)

        # Button for backspace
        self.button_backspace = tk.Button(self.buttons_frame, text="\u232b", bg=OFF_WHITE, fg=LABEL_COLOR, font= FONT_STYLE, borderwidth = 0, command = self.backspace, name="backspace")
        self.button_backspace.grid(row =0, column = 4, sticky=tk.NSEW)

        # Button for square
        self.button_square = tk.Button(self.buttons_frame, text="x\u00b2", bg=OFF_WHITE, fg=LABEL_COLOR, font= DEFAULT_FONT_STYLE, borderwidth = 0, command = self.square, name="square")
        self.button_square.grid(row =0, column = 2, sticky=tk.NSEW)

        # Button for squareroot
        self.button_sqrt = tk.Button(self.buttons_frame, text="\u221ax", bg=OFF_WHITE, fg=LABEL_COLOR, font= DEFAULT_FONT_STYLE, borderwidth = 0, command = self.sqrt, name="sqrt")
        self.button_sqrt.grid(row =0, column = 3, sticky=tk.NSEW)

        # Button for equals
        self.button_equals = tk.Button(self.buttons_frame, text="=", bg=LIGHT_BLUE, fg=LABEL_COLOR, font= DEFAULT_FONT_STYLE, borderwidth = 0, command = self.evaluate, name="equals")
        self.button_equals.grid(row =4, column = 3, columnspan =1, sticky=tk.NSEW)


        self.bind_keys()
    
    def bind_keys(self):
        self.window.bind("<Return>", lambda event: self.evaluate())
        for key in self.digits:
            self.window.bind(str(key), lambda event, digit = key: self.add_to_expression(digit))
        
        for key in self.operations:
            self.window.bind(key, lambda event, operator=key: self.append_operator(operator))

    def create_display_labels(self):
        total_label = tk.Label(self.display_frame, text=self.total_expression, anchor=tk.E, bg=LIGHT_GRAY, fg=LABEL_COLOR, padx=24,font = SMALL_FONT_STYLE)
        total_label.pack(expand=True, fill='both')

        label = tk.Label(self.display_frame, text=self.current_expression, anchor=tk.E, bg=LIGHT_GRAY, fg=LABEL_COLOR, padx=24,font = LARGE_FONT_STYLE)
        label.pack(expand=True, fill='both')


        return total_label,label

    def create_display_frame(self):
        frame = tk.Frame(self.window, height = 221,bg = LIGHT_GRAY)
        frame.pack(expand=True, fill="both")
        return frame

    def create_buttons_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill="both")
        return frame

    def clear(self):
        self.current_expression = ""
        self.total_expression = ""
        self.update_label()
        self.update_total_label()

    def backspace(self):

        if len(self.total_expression) == 0 and len(self.current_expression) > 0:
            self.total_expression == ""
            self.current_expression = ""
            self.update_total_label()

        else:
            self.current_expression = self.current_expression[:-1]
            self.update_label()
            
        if self.current_expression == "" and len(self.total_expression) > 1:
            self.total_expression = self.total_expression[:-1]
            t = self.total_expression
            Final = t[len(t.rstrip('.0123456789')):]
            try:
                if t[-1].isdigit():
                    self.total_expression = self.total_expression.rstrip('.0123456789')
                    self.current_expression = Final
            except IndexError:
                pass
            self.update_total_label()
            self.update_label()
    
    def square(self):
        self.current_expression = str(eval(f"{self.current_expression}**2"))
        self.update_label()

    def sqrt(self):
        self.current_expression = str(eval(f"{self.current_expression}**0.5"))
        self.update_label()

    def evaluate(self):
        self.total_expression += self.current_expression
        self.update_total_label()
        try:
            self.current_expression = str(eval(self.total_expression))
            expression = self.current_expression
            self.current_expression = expression.rstrip('0').rstrip('.') if '.' in expression else expression

            self.total_expression = ""
        except Exception:
            self.current_expression = "Math Error"   

            self.total_expression = ""
        finally:
            self.update_label()
    
    def add_to_expression(self, value):
        self.current_expression += str(value)
        self.update_label()
    
    def append_operator(self, operator):
        self.current_expression += operator
        self.total_expression += self.current_expression
        self.current_expression = " "
        self.update_total_label()
        self.update_label()
    
    def update_total_label(self):
        expression = self.total_expression
        for operator, symbol in self.operations.items():
            expression = expression.replace(operator, f' {symbol} ')
        self.total_label.config(text=expression)
        
    def update_label(self):
        self.label.config(text=self.current_expression[: 11])
        


    def run(self):
        self.window.mainloop()

if __name__ == '__main__':
    Calculator().run()

    

    