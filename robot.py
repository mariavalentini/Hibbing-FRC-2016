#!/usr/bin/env python3

import wpilib

class MyRobot(wpilib.SampleRobot):

    def robotInit(self):
        '''Robot initialization function'''

        # object that handles basic drive operations
        self.driveRight = wpilib.Victor(0)
        self.driveLeft = wpilib.Victor(1)
        self.myRobot = wpilib.RobotDrive(self.driveRight, self.driveLeft)
        self.myRobot.setExpiration(0.1)

        self.launcherTop = wpilib.Spark(2)
        self.launcherBottom = wpilib.Spark(3)
        self.ballIntake = wpilib.Victor(4)
        self.winch1 = wpilib.Victor(5)
        self.winch2 = wpilib.Victor(6)
        
        self.armIn = wpilib.Solenoid(0)
        self.armOut = wpilib.Solenoid(1)
        self.liftUp = wpilib.Solenoid(2)
        self.liftDown = wpilib.Solenoid(3)

        # joysticks 1 & 2 on the driver station
        self.stick = wpilib.Joystick(0)

    def autonomous(self):
        '''Autonomous initialization function'''
        self.myRobot.setSafetyEnabled(False)
        self.myRobot.tankDrive(0.75,0.75)
        wpilib.Timer.delay(5)
        self.myRobot.tankDrive(0,0)
        
    def operatorControl(self):
        '''Runs the motors with tank steering'''

        self.myRobot.setSafetyEnabled(True)

        while self.isOperatorControl() and self.isEnabled():
            self.myRobot.tankDrive(-self.stick.getRawAxis(1),-self.stick.getRawAxis(3))

            if self.stick.getRawButton(6):
                self.launcherTop.set(-0.95)
                self.launcherBottom.set(0.95)
            elif self.stick.getRawButton(3):
                self.launcherTop.set(0.95)
                self.launcherBottom.set(-0.95)
            else:
                self.launcherTop.set(0)
                self.launcherBottom.set(0)

            if self.stick.getRawButton(5):
                self.ballIntake.set(1)
            elif self.stick.getRawButton(4):
                self.ballIntake.set(-1)
            else:
                self.ballIntake.set(0)
            
            if self.stick.getRawButton(1):
                self.armIn.set(True)
                self.armOut.set(False)
            else:
                self.armIn.set(False)
                self.armOut.set(True)
                
            if self.stick.getRawButton(2):
                self.liftUp.set(True)
                self.liftDown.set(False)
            else:
                self.liftUp.set(False)
                self.liftDown.set(True)
                
            wpilib.Timer.delay(0.005) # wait for a motor update time

if __name__ == '__main__':
    wpilib.run(MyRobot)
