class termDifferentiate:
    def __init__(self,term):    #term is str type, to find variable name

        self.term = term
        self.flag = False
        self.coefficient = None #what if no coefficient
        self.exponent = None   #what if exponent is 1
        self.sign = None

        #locate variable
        for element in self.term:   
            if element.isalpha():
                self.variable = element
                self.flag = True

#include variable?  
    def containVariable(self):
        if self.term[0] == '-':
            self.sign = '-'
        else:
            self.sign = '+'        
        if '*' in self.term:
            if self.sign == '-':
                self.coefficient = self.term[1:self.term.find('*')]
            else:
                self.coefficient = self.term[:self.term.find('*')]
        if '^' in self.term:
            self.exponent = self.term[self.term.find('^')+1:]

    def outputComponent(self):
        if self.exponent != None and self.exponent == '0':
            self.coefficient = '0'
        elif self.coefficient != None:
            if self.exponent != None:
                self.coefficient = str(eval(self.coefficient)*eval(self.exponent))
                #to treat special case, exponent is 1
                self.exponent = str(eval(self.exponent)-1) 
            else:
                self.exponent = '0'
        else:
            if self.exponent != None:
                self.coefficient = self.exponent
                #warning: special case, exponent is 1
                self.exponent = str(eval(self.exponent)-1)       
            else:
                self.coefficient = '1'
                self.exponent = '0'

    def output(self): 
        #just constant term, exponent is 0     
        if not self.flag:   
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
    function = function.replace('-','+-')
    polynomial = function.split('+')
    if polynomial[0] == '':
        polynomial = polynomial[1:]
    #generate a list to split the function term by term
    newPolynomial = []
    #call class
    for term in polynomial:
        handle = termDifferentiate(term)
        handle.containVariable()
        handle.outputComponent()
        newPolynomial.append(handle.output())
    output = ''.join(newPolynomial)
    #reshape the output and delete uneccessary things
    if len(output) != 0:
        if output[0] == '+':
            return output[1:]
        else:
            return output
    else:
        return '0'

function = input('Please input a polynomial > ')
print(reshape(function))