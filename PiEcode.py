# Substitute device IDs when using real robot
KOALA_DRIVE = "6_12014819996989542905"
LINE_FOLLOWER = "line_follower"
LIMIT_SWITCH = "limit_switch"
speed = 1
degrees_translate = 0.1

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

    if driving_mode == 0:
        # Driving straight
        Robot.set_value(KOALA_DRIVE, "velocity_b", 0.7)
        Robot.set_value(KOALA_DRIVE, "velocity_a", -0.7)
        print("drive mode 0")
    elif driving_mode == 1:
        print("drive mode is 1")
        # Tank Drive
        while True:
            left_motor_speed = -0.7
            right_motor_speed = -0.7
            
            while Gamepad.get_value("dpad_up"):
                Robot.set_value(KOALA_DRIVE, "velocity_b", left_motor_speed)
                Robot.set_value(KOALA_DRIVE, "velocity_a", right_motor_speed)
                #print("up arrow") these crash dawn
                
            while Gamepad.get_value("dpad_down"):
                Robot.set_value(KOALA_DRIVE, "velocity_b", -left_motor_speed)
                Robot.set_value(KOALA_DRIVE, "velocity_a", -right_motor_speed)
                #print("down arrow") these crash dawn
            while Gamepad.get_value("dpad_right"):
                Robot.set_value(KOALA_DRIVE, "velocity_b", left_motor_speed)
                Robot.set_value(KOALA_DRIVE, "velocity_a", -right_motor_speed)
                #print("right arrow") these crash dawn
            while Gamepad.get_value("dpad_left"):
                Robot.set_value(KOALA_DRIVE, "velocity_b", -left_motor_speed)
                Robot.set_value(KOALA_DRIVE, "velocity_a", right_motor_speed)
                #print("left arrow") these crash dawn
        
            Robot.set_value(KOALA_DRIVE, "velocity_b", 0)
            Robot.set_value(KOALA_DRIVE, "velocity_a", 0)
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
    forward(10)
    turn_right(45)

    
def forward(distance):
    print("Forward")
    Robot.set_value(KOALA_DRIVE, "velocity_b", -1.0)
    Robot.set_value(KOALA_DRIVE, "velocity_a", -1.0)
    Robot.sleep(distance*speed)

def turn_right(degrees):
    print("right")
    Robot.set_value(KOALA_DRIVE, "velocity_b", 1.0)
    Robot.set_value(KOALA_DRIVE, "velocity_a", 1.0)
    Robot.sleep(degrees*degrees_translate)

def turn_left(degrees):
    print("right")
    Robot.set_value(KOALA_DRIVE, "velocity_b", 1.0)
    Robot.set_value(KOALA_DRIVE, "velocity_a", 1.0)
    Robot.sleep(degrees*degrees_translate)
    