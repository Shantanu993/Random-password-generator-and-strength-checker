import subprocess
from subprocess import PIPE, Popen

subprocess.call(["gcc", "randompass.c"]);
subprocess.call("./a.exe");
c_out = str(subprocess.check_output("./a.exe"));
c_out = c_out[2:-1]
print()



""" A password is said to be strong if it satisfies the following criteria: 

It contains at least one lowercase English character.
It contains at least one uppercase English character.
It contains at least one special character. The special characters are: !@#$%^&*()-+
Its length is at least 8.
It contains at least one digit. """

# Python3 program to check if a given
# password is strong or not.
def printStrongNess(input_string):
	
	n = len(input_string)

	# Checking lower alphabet in string
	hasLower = False
	hasUpper = False
	hasDigit = False
	specialChar = False
	normalChars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 "
	
	for i in range(n):
		if input_string[i].islower():
			hasLower = True
		if input_string[i].isupper():
			hasUpper = True
		if input_string[i].isdigit():
			hasDigit = True
		if input_string[i] not in normalChars:
			specialChar = True

	# Strength of password
	print("Strength of password:-", end = "")
	if (hasLower and hasUpper and
		hasDigit and specialChar and n >= 8):
		print("Strong")
		
	elif ((hasLower or hasUpper) and
		specialChar and n >= 6):
		print("Moderate")
	else:
		print("Weak")

# Driver code
if __name__=="__main__":
	
	input_string = c_out
	
	printStrongNess(input_string)


