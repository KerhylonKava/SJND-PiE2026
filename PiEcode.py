KOALA_DRIVE = "6_12014819996989542905" # Device ID
KOALA_HAMMERHEAD = "6_14079944033812652925"
LINE_FOLLOWER = "line_follower"
LIMIT_SWITCH = "limit_switch"
speed = 0.1
degrees_translate = 0.1
motor_speed = 0.7

def autonomous():
    print("Autonomous mode has started!")
    # Left motor rotates in the opposite direction
    Robot.set_value(KOALA_DRIVE, "invert_b", True)
    Robot.run(autonomous_red)

def autonomous_main():
    pass

def teleop_setup():
    print("Teleop mode has started!")
    # Left motor rotates in the opposite direction
    Robot.set_value(KOALA_DRIVE, "invert_b", True)

def teleop():
    driving_mode = 1
    Robot.set_value(KOALA_DRIVE, "invert_a", True)
    print("Teleop mode has started!")

    if driving_mode == 0:
        # Driving straight
        Robot.set_value(KOALA_DRIVE, "velocity_b", 0.7)
        Robot.set_value(KOALA_DRIVE, "velocity_a", -0.7)
        print("drive mode 0")
    elif driving_mode == 1:
        print("drive mode is 1")
        # Tank Drive
        while True:
            
            while Gamepad.get_value("dpad_up"):
                Robot.set_value(KOALA_DRIVE, "velocity_b", motor_speed)
                Robot.set_value(KOALA_DRIVE, "velocity_a", motor_speed)
                #print("up arrow") these crash dawn
                
            while Gamepad.get_value("dpad_down"):
                Robot.set_value(KOALA_DRIVE, "velocity_b", -motor_speed)
                Robot.set_value(KOALA_DRIVE, "velocity_a", -motor_speed)
                #print("down arrow") these crash dawn
            while Gamepad.get_value("dpad_right"):
                Robot.set_value(KOALA_DRIVE, "velocity_b", motor_speed)
                Robot.set_value(KOALA_DRIVE, "velocity_a", -motor_speed)
                #print("right arrow") these crash dawn
            while Gamepad.get_value("dpad_left"):
                Robot.set_value(KOALA_DRIVE, "velocity_b", -motor_speed)
                Robot.set_value(KOALA_DRIVE, "velocity_a", motor_speed)
                #print("left arrow") these crash dawn
            
            while Gamepad.get_value("button_y"):
                Robot.set_value(KOALA_HAMMERHEAD, "velocity_b", -0.1)
            while Gamepad.get_value("button_a"):
                Robot.set_value(KOALA_HAMMERHEAD, "velocity_b", 0.1)
        
            Robot.set_value(KOALA_DRIVE, "velocity_b", 0) # left motor
            Robot.set_value(KOALA_DRIVE, "velocity_a", 0) # right motor
            Robot.set_value(KOALA_HAMMERHEAD, "velocity_b", 0) # Hammerhead Gear
    elif driving_mode == 2:
        # Tank Drive
        left_motor_speed = 0
        right_motor_speed = 0
        if Keyboard.get_value("w"):
            pass
        elif Keyboard.get_value("s"):
            pass
        if Gamepad.get_value("dpad_up"):
            right_motor_speed = 1
            left_motor_speed = 1
        elif Keyboard.get_value("down_arrow"):
            right_motor_speed = -1
            left_motor_speed = -1
        elif Keyboard.get_value("right_arrow"):
            right_motor_speed = -1
            left_motor_speed = 1
        elif Keyboard.get_value("left_arrow"):
            right_motor_speed = 1
            left_motor_speed = -1
    
        Robot.set_value(KOALA_DRIVE, "velocity_b", left_motor_speed)
        Robot.set_value(KOALA_DRIVE, "velocity_a", -right_motor_speed)
    elif driving_mode == 3:
        # Arcade Drive
        forward_speed = 0
        turning_speed = 0
        if Keyboard.get_value("w"):
            forward_speed = 1
        elif Keyboard.get_value("s"):
            forward_speed = -1
        if Keyboard.get_value("d"):
            turning_speed = 1
        elif Keyboard.get_value("a"):
            turning_speed = -1
        Robot.set_value(KOALA_DRIVE, "velocity_b", max(min((forward_speed + turning_speed), 1.0), -1.0))
        Robot.set_value(KOALA_DRIVE, "velocity_a", max(min(forward_speed - turning_speed, 1.0), -1.0))

def autonomous_red():
    forward(1,5) # 1 ft 5 in
    turn_right(45)
    forward(1,4) # 1 ft 4 in
    turn_right(45)
    forward(2,6) # 2 ft 6 in
    turn_right(45)
    forward(10,0)
    
def autonomous_yellow():
    forward(2,6)
    turn_right(45)
    forward(2,0)
    turn_right(45)
    forward(3,2) # 3 ft 2 in
    turn_left(45)
    forward(1,4) # 1 ft 4 in

def forward(feet, inches):
#def forward(distance):
    print("Forward")
    Robot.set_value(KOALA_DRIVE, "velocity_b", motor_speed)
    Robot.set_value(KOALA_DRIVE, "velocity_a", motor_speed)
    #Robot.sleep(distance*speed)
    Robot.sleep((feet+inches*12)*speed/motor_speed)

def turn_right(degrees):
    print("right")
    Robot.set_value(KOALA_DRIVE, "velocity_b", 1.0)
    Robot.set_value(KOALA_DRIVE, "velocity_a", 1.0)
    Robot.sleep(degrees*degrees_translate/motor_speed)

def turn_left(degrees):
    print("right")
    Robot.set_value(KOALA_DRIVE, "velocity_b", 1.0)
    Robot.set_value(KOALA_DRIVE, "velocity_a", 1.0)
    Robot.sleep(degrees*degrees_translate/motor_speed)
    