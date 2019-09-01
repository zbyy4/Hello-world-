class Term():
    """ Simulate the term in polynomial"""
    def __init__(self, content):
        """set the basic data"""
        self.content = content
        self.coefficient = None
        self.exponent = None
        self.sign = None
        self.flag = False
        for element in self.content:
            if element.isalpha():
                self.variable = element
                self.flag = True

    def set_component(self):
        """ Get the sign, coefficient and exponent of the term."""
        if self.content[0] == '-':
            self.sign = '-'
        else:
            self.sign = '+'
        if '*' in self.content:
            if self.sign == '-':
                self.coefficient = self.content[1:self.content.find('*')]
            else:
                self.coefficient = self.content[:self.content.find('*')]
        if '^' in self.content:
            self.exponent = self.content[self.content.find('^')+1:]
    
    def take_derivative(self):
        """
        If the exponent is not 0 or empty,
        the coefficient will equal to 
        the orginal coefficient times the exponent.
        """
        if self.exponent != None and self.exponent == '0':
            self.coefficient = '0'
        elif self.coefficient != None:
            if self.exponent != None:
                self.coefficient = str(eval(self.coefficient)*eval(self.exponent))
                # Special case: exponent is 1
                self.exponent = str(eval(self.exponent)-1) 
            else:
                self.exponent = '0'
        else:
            if self.exponent != None:
                self.coefficient = self.exponent
                # Special case: exponent is 1
                self.exponent = str(eval(self.exponent)-1)       
            else:
                self.coefficient = '1'
                self.exponent = '0'

    def output_result(self):      
        if not self.flag:  
            # Constant term 
            return ''
        elif self.coefficient == '0':
            return self.sign+'0'
        elif self.exponent == '0':
            return self.sign+self.coefficient
        elif self.exponent == '1':
            return self.sign+self.coefficient+'*x'
        else:
            return self.sign+self.coefficient+'*x^'+self.exponent


def reshape(function):
    """
    This reshape() function first splits the input polynomial into terms,
    then it takes the derivative of every term,
    finally it will combine all the results together.
    """
    function = function.replace('-','+-')
    polynomial = function.split('+')
    if polynomial[0] == '':
        polynomial = polynomial[1:]
    newPolynomial = []
    # Generate a list to split the function term by term,
    for content in polynomial:
        term_in_polynomial = Term(content)    # Then call class Term
        term_in_polynomial.set_component()
        term_in_polynomial.take_derivative()
        newPolynomial.append(term_in_polynomial.output_result())
    output = ''.join(newPolynomial)
    # Reshape the output and delete uneccessary staffs.
    if len(output) != 0:
        if output[0] == '+':
            return output[1:]
        else:
            return output
    else:
        return '0'


function = input('Please input a polynomial > ')
print(reshape(function))