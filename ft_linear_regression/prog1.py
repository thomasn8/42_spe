import os

def getThetaValues(theta0, theta1):
	if os.path.exists("thetas.txt"):
		with open("thetas.txt", "r") as file:
			lines = file.readlines()
		if len(lines) >= 2:
			theta0_line = lines[0].split()
			theta1_line = lines[1].split()
			if len(theta0_line) >= 2 and theta0_line[0] == "theta0" and \
				len(theta1_line) >= 2 and theta1_line[0] == "theta1":
				theta0 = float(theta0_line[1])
				theta1 = float(theta1_line[1])
				return theta0, theta1
		print("Warning: thetas.txt is corrupted")
	else:	
		print("Warning: thetas.txt not found")
	print("You should consider train the model using prog2.py")
	return theta0, theta1


def estimatePrice(theta0, theta1, mileage, decimal=2):
	prediction = round(theta1*mileage + theta0)
	return round(prediction, decimal)


def main():
	theta0 = 0.
	theta1 = 0.
	theta0, theta1 = getThetaValues(theta0, theta1)
	mileage = input("Enter the mileage of the car: ")
	if not mileage.isnumeric():
		print("Error: enter a numeric value.")
	else:
		prediction = estimatePrice(theta0, theta1, float(mileage))
		print('Estimated price:', prediction)
	

if __name__ == "__main__":
	main()
