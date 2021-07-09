    def percentage(self):
        try:
            self.current_expression = str(eval(f"{self.current_expression}/100"))
            self.update_label()
        except Exception:
            pass

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
            output = t[len(t.rstrip('().0123456789')):]
            operator = ["/", "*", "-", "+"]
            try:
                if t[-1].isdigit() or t[-1] == ")" or t[-1] in operator:
                    self.total_expression = self.total_expression.rstrip('().0123456789')
                    self.current_expression = output

            except IndexError:
                pass
            self.update_total_label()
            self.update_label()
    
    def square(self):
        try:
            self.current_expression = str(eval(f"{self.current_expression}**2"))
            self.update_label()
        except Exception:
            pass

    def sqrt(self):
        try:
            self.current_expression = str(eval(f"{self.current_expression}**0.5"))
            self.update_label() 
        except Exception:
            pass

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
