def swap_func(cond, a, b):
    """Swap Function Call is defined to swap the function without additional variables used.
    Arguments are (Condition, data 1,data 2)"""
    # Specify the dataType as a Integer for Arguments 1
    a, b = int(a), int(b)
    # If Condition arguments is 0(Zero) it will run as a module,
    # If Condition arguments is 1 it will get the data from the function call and execute it
    if cond == 0:
        # Get the Input from the user
        a = int(input("Key in value for a:  "))
        b = int(input("Key in value for b:  "))
    # Print the values before Swapping
    print("Before   :   a = %d and b = %d" % (a, b))
    # Message append to return for the function call
    Msg = "Before   : a ={0} , b ={1}".format(a, b)
    # Swap the two values
    a, b = b, a
    # Print the Values after the Swap
    Msg1 = "After   : a ={0} , b ={1}".format(a, b)
    # Append the Swap before and after used to return the string during the function call
    Msg2 = Msg + '\n' + Msg1
    # Print the values after Swapping
    print("After    :   a = %d and b = %d" % (a, b))
    # Return to the functional call
    return Msg2


def lookup_func(cond, requestedFruit, requestedQty):
    """Lookup Function call is used to calculate the Total cost based on the Selection of Fruit and Number of Qty
    Arguments are Condition ,RequestedFruit and RequestedQuantity"""
    # Dictionary is used to fix the Fruit name and Cost for per fruiy
    table = dict({'apple': 1.30, 'orange': 1.00, 'pear': 0.80, 'grape': 2.20, 'kiwi': 1.70})
    # Condition is used to differentiate the Function call or standalone test parameters
    # if the condition value is 0(zero). It will run as a standalone script(used for unit test)
    if cond == 0:
        # Ask the user to input the fruit name
        requestedFruit = input('Please enter the Fruit from this list [Apple,Orange,Pear,Grape,Kiwi] :  ')
        # Ask the user to input the number of Quantity
        requestedQty = input('Please enter the required quantity :  ')
        # if the user input the  didnt input the fruit name or quantity .
        # Following below if case will check and return the value to user
    if (len(requestedFruit) > 0 and requestedFruit.isspace() == False and len(
            requestedQty) > 0 and requestedQty.isspace() == False):
        # Convert the Requested Quantity string to an integer value
        requestedQty = int(requestedQty)
    else:
        # User didn't input the fruit name or Quantity .Script will print as a "Invalid Input" to the terminal Screen
        print('Invalid Input')
        # When during the function call . Else case is executed it will return to the functional call as #0(Zero)
        return 0
    # Convert the requested fruit into the lower case format
    price = table.get(requestedFruit.lower())
    # Check the Fruit name is available in the dictionary or not
    if price is None:
        # if the Fruit name not found in the dictionary it will print as "Fruit not Found"
        print('Fruit is not found.')
        # When during the function call . It will return as #0(Zero)
        return 0
    else:
        # If the Fruit is found in the dictionary it will calculate the
        # total price based on the Requested Fruit and Requested Quantity
        total = round(requestedQty * price, 2)
        # Print the Total Price as well as Requested fruit and Quantity onto the Terminal
        print('Fruit    : {0}\nQuantity    : {1}\n'
              'Total Price  : {2}'.format(requestedFruit, requestedQty, total))
        # Return the total cost to the Functional Call Script
        return "{0:.2f}".format(total)


if __name__ == '__main__':
    """It will run the script when the execution happens. It used to do for Unit testing"""
    # Call the Swap Function and send the Arguments as a dummy values except the Condition is #0(Zero)
    swap_func(0, 2, 3)
    # Call the lookup Function and send the Arguments as a dummy values except the Condition is #0(Zero)
    lookup_func(0, 'Apple', '5')
