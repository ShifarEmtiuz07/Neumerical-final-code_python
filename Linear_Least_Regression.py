import numpy as np


def estimate_coef(X, Y):
	N = np.size(X)
	sumx = sumy = sumx2 = sumxy = 0
	for i in range(N):
		sumx += X[i]
		sumy += Y[i]
		sumx2 += X[i]**2
		sumxy += X[i]*Y[i]
	meanx = sumx / N
	meany = sumy / N

	a1 = (N*sumxy - sumx*sumy) / (N*sumx2 - sumx**2)
	a0 = meany - a1 * meanx

	return (a1,a0)

	


	
	



def main():
	
	X = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
	Y = np.array([1, 3, 2, 5, 7, 8, 8, 9, 10, 12])

	b = estimate_coef(X,Y)
	print("Estimated coefficients:\nb_0 = {:.4f} \
		\nb_1 = {:.4f}".format(b[0], b[1]))

	# plotting regression line
	#plot_regression_line(x, y, b)
if __name__ == "__main__":
	main()



