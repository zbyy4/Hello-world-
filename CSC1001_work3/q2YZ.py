class termDifferentiate:
    def __init__(self,term):    #term is str type, find variable name

        self.term = term
        self.flag = False
        self.coefficient = None #no coefficient
        self.exponent = None   #exponent is 1
        self.sign = None

        for element in self.term:
            if element.isalpha():
                self.variable = element
                self.flag = True

#include variable    
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
        # print(self.coefficient)
        # print(self.exponent)

    def outputExponent(self):
        if self.coefficient != None:
            if self.exponent != None:
                self.coefficient = str(eval(self.coefficient)*eval(self.exponent))#int??????????????
                self.exponent = str(eval(self.exponent)-1)     #warning: special case, exponent is 1
            else:
                self.exponent = '0'
        else:
            if self.exponent != None:
                self.coefficient = self.exponent
                self.exponent = str(eval(self.exponent)-1)       #warning: special case, exponent is 1
            else:
                self.coefficient = '1'
                self.exponent = '0'

    def output(self):      
        if not self.flag:   #just constant term, exponent is 0
            return ''
        elif self.exponent == '0':          
            return self.sign+self.coefficient
        elif self.exponent == '1':
            return self.sign+self.coefficient+'*x'
        else:
            return self.sign+self.coefficient+'*x^'+self.exponent


def reshape(function):
    # if function[0] != '+' and function[0] != '-':
    #     function = '+'+function
    function = function.replace('-','+-')
    polynomial = function.split('+')
    if polynomial[0] == '':
        polynomial = polynomial[1:]
    newPolynomial = []
    # print(polynomial)
    for term in polynomial:
        handle = termDifferentiate(term)
        handle.containVariable()
        handle.outputExponent()
        newPolynomial.append(handle.output())
    # newPolynomial[0] = newPolynomial[0][1:]
    # print(newPolynomial)
    output = ''.join(newPolynomial)
    if len(output) != 0:
        if output[0] == '+':
            return output[1:]
        else:
            return output
    else:
        return '0'

function = input('Please input a polynomial > ')
print(reshape(function))