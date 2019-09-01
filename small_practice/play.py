import sys;
sys.path.append('E:/CSC/CSC learning/CSC1002/')
from myMatrix import myMatrix;

m = myMatrix([[1,2,3],[4,5,6],[7,8,9]])
n = myMatrix([[1,2,4],[3,4,5],[5,6,7]])

m.setValue(1,1,-3)
n.setValue(2,1,4)
m.scale(2)
m.plusMat(n)

m.print()