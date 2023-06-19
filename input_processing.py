# input_processing.py
# Nick Nikolov, ENSF 592 P23
# A terminal-based program for processing computer vision changes detected by a car.
# Detailed specifications are provided via the Assignment 2 git repository.
# You must include the code provided below but you may delete the instructional comments.
# You may add your own additional classes, functions, variables, etc. as long as they do not contradict the requirements (i.e. no global variables, etc.). 
# You may import any modules from the standard Python library.
# Remember to include your name and comments.


# No global variables are permitted

# You do not need to provide additional commenting above this class, just the user-defined functions within the class
class Sensor:
    # Must include a constructor that uses default values
    # You do not need to provide commenting above the constructor
    def __init__(self):
        self.light = "green"
        self.pedestrian = "no"
        self.vehicle = "no"
        self.current_input = 1 #Used to store the current input, used for error checking and status updating

    # update_status is a function that references in the sensor object and
    # updates the light, pedestrian, and vehicle sensors in the Sensor object
    # no return value
    def update_status(self):
        prev_input = self.current_input #Need to store the previous input since vision_change_error_checking will create a new current_input for the status change
        if(vision_change_error_checking(self)): #Only passes if not errors are found in vision change input
            if (prev_input == 1): #if the previous input indicated a light change
                    self.light = self.current_input #Update light sensor to the observed change
            elif (prev_input == 2): #If the previous input indicated a pedestrian change
                    self.pedestrian = self.current_input #Update pedestrian sensor to the observed change
            elif (prev_input == 3): # If the previous input indicated a vehicle change
                    self.vehicle = self.current_input #Update vehicle sensor to the observed change

#print_message is a function that accepts a sensor object as input
#  and will print the current status of all sensors, and whether the vehicle should stop, proceed or proceed with caution
#no return value
def print_message(sensor):

    if (sensor.light == "red" or sensor.pedestrian == "yes" or sensor.vehicle == "yes"): #If red light, or pedestrians, or vehicles are sensed, you must stop
        print("\nSTOP\n")
    elif (sensor.light == "green" and sensor.pedestrian == "no" and sensor.vehicle == "no"): #Only proceed if the light is green, no pedestrians or vehicles are present
        print("\nProceed\n")
    elif (sensor.light == "yellow" and sensor.pedestrian == "no" and sensor.vehicle == "no"):#proceed with caution only if the light is yellow, and there are no vehicle or pedestrians present
        print("\nCaution\n")

#print the current status of all sensors
    print("""Light = {0}, Pedestrian = {1}, Vehicle = {2}.\n""".format(sensor.light, sensor.pedestrian, sensor.vehicle))

#the sensor_error_checking function takes a sensor object as input
#  checks if there is an input error to the vision input (non-integer or integer outside of the range)
# throws a ValueError if a non-integer is input, and returns false
# returns true if there are no input errors
def sensor_error_checking(sensor):
    valid_sensor_inputs = [0,1,2,3] # Used to define the valid sensor inputs

    try: # check if the input is an integer and if it is in the valid_sensor_inputs
        sensor.current_input = int(input("Select 1 for light, 2 for pedestrian, 3 for vehicle, or 0 to end the program: ")) #Int function throws a ValueError if an integer is not input
        if (sensor.current_input not in valid_sensor_inputs): #If input is not between 0 - 3
            raise ValueError #raise valueError
        
        else: return True #Returns true if an input between 0 - 3 was entered
    except ValueError: #If the input is not an integer, exit with false and explain the valid inputs expected
        print("You must select either 1, 2, 3, or 0.\n")
        return False

#the vision_change_error_checking function takes a sensor object as input
# checks if there is an input error to the sensor change, 
# if the sensor change is not valid (red, green, yellow, yes or no), the function explains that an invalid vision change was entered
#returns true if no errors, or false if input error occured
def vision_change_error_checking(sensor):

    valid_vision_inputs = ["red", "green", "yellow", "yes", "no"] # Used to define the valid sensor changes
    sensor.current_input = input("What is the new status of this input?: ") #prompts the user for the sensor change
    if (sensor.current_input in valid_vision_inputs): #Must be a valid sensor input to proceed
        return True
    else: 
        print("Invalid vision change.") #If a astring is input, but not the correct string, a message is displayed 
        return False
  
# Complete the main function below
def main():
    print("\n***ENSF 592 Car Vision Detector Processing Program***\n")
    
    sensor = Sensor() #initialize new sensor object

    while(True): #infinite loop prompting the user for sensor and input changes
        print("What changes are detected in the vision input?")

        if(sensor_error_checking(sensor)): #proceeds only if no sensor error is detected
            if (sensor.current_input == 0): #If user inputs zero, ends the loop immediately
                break

            sensor.update_status() #update the sensors with the latest information
            print_message(sensor) #print the current recommendation along with current satus of each sensor

# No additional code should be included below this
if __name__ == '__main__':
    main()

