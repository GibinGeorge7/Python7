
"""Program to
1.convert temperature in celcius to fahrenhet
2.print out on screen
3.write output to file temperature1.txt"""

temperatures = [10, -20, -289, 100]
def c_to_f(c):
    if c < -273.15:
        return "That temperature doesn't make sense!"
    else:
        f = c* 9/5 + 32
        return f
for t in temperatures:
    var1=str((c_to_f(t)))
    print (var1)
    with open("temperature.txt","a+") as myfile:
        myfile.write(var1)
        myfile.write("\n")
