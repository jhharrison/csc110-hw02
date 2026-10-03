# Task 1.1:
#  Complete the function "read_two_ints" below:
def read_two_ints():
    """Read two numbers from the user and return them as integers."""
    x_str = input("give me x: ")
    x = int(x_str)
    
    y_str = input("give me y: ")
    y = int(y_str)
    
    return x, y

# Task 2.1:
#  Complete the function "compute_multadd" below:
def compute_multadd(a, b):
    """Calculate and print the multipliation and addition results, then return their quotient."""
    mult_result = a * b
    print("mult result:", mult_result)
    
    add_result = a + b
    print("add result:", add_result)
    
    return mult_result / add_result
    
    
    
# Task 3.1:
#  Complete the function "print_fancy" below:
def print_fancy(a, b, ab_multadd):
    """Print the input numbers and multadd result in a formatted display."""
    print("****************")
    print("RESULTS:")
    print("first number:", a)
    print("second number:", b)
    print("multadd result:", ab_multadd)
    print("================")

def main ():
    """Run the program by reading inputs, computer th result, and printing it."""
    # Task 1.2:
    #  Add one line below to call read_two_ints (note that it returns two values)
    #  the call should provide no arguments
    #  store the returned values into two variables: x and y
    
    x, y = read_two_ints()


    # Task 2.2:
    #  Add one line below to call multadd (note that it returns one value)
    #  the call should provide the arguments x, and y you obtained above;
    #  store the returned value in a variable called xy_multadd

    xy_multadd = compute_multadd(x, y)
    

    # Task 3.2:
    #  Complete The line below to call print_fancy
    #  the call should provide the arguments x, y, and xy_multadd you obtained above;

    print_fancy(x, y, xy_multadd)

    # Do not modify this final print statement
    print("The End")

# Do not modify these two lines
if __name__ == "__main__":
    main()
