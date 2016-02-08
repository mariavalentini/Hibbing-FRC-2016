#!/usr/bin/env python3

import wpilib

class MyRobot(wpilib.SampleRobot):
    
    def robotInit(self):
        '''Robot initialization function'''
        
        # object that handles basic drive operations
        self.myRobot = wpilib.RobotDrive(0, 1)
        self.myRobot.setExpiration(0.1)
        
        # joysticks 1 & 2 on the driver station
        self.leftStick = wpilib.Joystick(0)
        self.rightStick = wpilib.Joystick(1)
        
    def operatorControl(self):
        '''Runs the motors with tank steering'''
        
        self.myRobot.setSafetyEnabled(True)
        
        while self.isOperatorControl() and self.isEnabled():
            self.myRobot.arcadeDrive(self.leftStick)
            wpilib.Timer.delay(0.005) # wait for a motor update time
            
if __name__ == '__main__':
    wpilib.run(MyRobot)
