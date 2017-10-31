def swapRows(A,row1,row2):
	A[row1],A[row2]=A[row2],A[row1]
	return A



def Row_Transformations(A,x,row1,row2):
	for i in range(len(A)):
		if i==row2:
			for j in range(len(A[row2])):
				A[row2][j]=A[row2][j]+A[row1][j]*x
	return A



def MatrixRank(A):
	rank=len(A[0])
	lastcolumn=rank-1
	row=0
	while row<len(A):
		c=0
	\
		if row>=rank:
			break
		if A[row][row]!=0:
			for column in range(len(A)):
				if column!=row:
					columnzero=A[column][row]/A[row][row]
					A=Row_Transformations(A,-1*columnzero,row,column)
					
		else :
			for j in range (row+1,len(A)):
				if A[j][row]!=0:
					A=swapRows(A,j,row)
					c=1
					row=row-1
					break ;
			if c==0:
				for i in range (len(A)):
					A[i][row]=A[i][lastcolumn]
					
				lastcolumn=lastcolumn-1	
				rank=rank-1
				row=row-1
		
		row=row+1
	return rank
f=[[2,1,5,0],[7,3,5,2]]
g=MatrixRank(f)
print (g)




















