class myMatrix:
    def __init__(self,L):
        self.L = L
        self.m = len(L)
        self.n = len(L[0])

    def getValue(self,i,j):
        return self.L[i][j]
    
    def setValue(self,i,j,v):
        self.L[i][j] = v

    def plusMat(self, M):
        for i in range(self.m):
            for j in range(self.n):
                self.L[i][j] += M.getValue(i,j)

    def scale(self,s):
        for i in range(self.m):
            for j in range(self.n):
                self.L[i][j] *= s

    def print(self):
        for i in range(self.m):
            s = ''
            for j in range(self.n):
                s += str(self.L[i][j])+" "
            print(s)