import numpy, random, os

learing_rate = 1
bias = 1
weights = [random.random(), random.random(), random.random()]


def Perceptron(input1, input2, output):
    perceptron_output = input1*weights[0]+input2*weights[1]+bias*weights[2]
    if perceptron_output > 0 : #activation function
      perceptron_output = 1
    else :
      perceptron_output = 0

    error = output - perceptron_output

    weights[0] += error * input1 * learing_rate
    weights[1] += error * input2 * learing_rate
    weights[2] += error * bias * learing_rate

#learning phase - true = 1, false = 0
for i in range(50):
    Perceptron(1, 1, 1)
    Perceptron(1, 0, 1)
    Perceptron(0, 1, 1)
    Perceptron(0, 0, 0)

x = int(input("x = "))
y = int(input("y = "))

perceptron_output = x*weights[0]+y*weights[1]+bias*weights[2]

if perceptron_output > 0 : #activation function
   perceptron_output = 1
else :
   perceptron_output = 0
print(x, "or", y, "is:", perceptron_output)


#currently using heaviside activation function rather than sigmoid since we are looking for a true/false result
