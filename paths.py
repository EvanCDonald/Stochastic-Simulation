import numpy as np  
import pandas as pd
import matplotlib.pyplot as plt

def make_paths(n):
    #make_paths will be called in main.  This function will fill a #dataframe with the values of the brownian motion
	df1=pd.DataFrame(index=range(n), columns=['BM1'])
	df1.loc[0,'BM1']=0
	k=1
	while k<len(df1):
		df1.loc[k,'BM1']=df1.loc[k-1,'BM1']+np.random.normal(0,.1)
		k=k+1
	return(df1)



def main(): 
	
	d=int(input('How many sample paths would you like to see?\n'))
	T=int(input('What is the endpoint of your time interval? Enter a positive integer.\n'))
	
    #Our time increments will be a constant .01, convenient for
    # calculation purposes.  Need to be able to take square 
    # root of increment to get standard deviation for use in 
    # random.normal


    #time interval is [0,T].  There are T*100 increments, and n
    # endpoints
	n=T*100+1
	t=np.linspace(0,T,n)

	i=0
	while i<d:
		G=plt.plot(t, make_paths(n))
		i=i+1
	
	plt.show()

if __name__=='__main__': 
	main()