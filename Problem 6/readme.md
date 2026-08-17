# Problem 1.6

The following equation estimates the average calories burned for a person when exercising, which is based on a [scientific journal article](https://www.tandfonline.com/doi/abs/10.1080/02640410470001730089)

$$ Calories = \frac{(Age * 0.2757 + Weight*0.03295+ HeartRate * 1.0781 - 75.4991)* Time}{8.368}$$

Write a program using inputs age (years), weight (pounds), heart rate (beats per minute), and time (minutes), respectively. Output the average calories burned for a person. 

Output each floating-point value with two digits after the decimal point, which can be achieved as follows:

`print(f'Calories: {calories:.2f} calories')`

Ex: If the input is:

    49
    155
    148
    60

then the output is:

    Calories: 736.21 calories
