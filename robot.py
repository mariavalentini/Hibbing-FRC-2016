#!/usr/bin/env python3

import wpilib

class MyRobot(wpilib.SampleRobot):

    def robotInit(self):
        '''Robot initialization function'''

        # object that handles basic drive operations
        self.myRobot = wpilib.RobotDrive(wpilib.Victor(0), wpilib.Victor(1))
        self.myRobot.setExpiration(0.1)

        self.launcherTop = wpilib.Spark(0)
        self.launcherBottom = wpilib.Spark(1)
        self.ballIntake = wpilib.Victor(2)
        self.winch1 = wpilib.Victor(3)
        self.winch2 = wpilib.Victor(4)

        # joysticks 1 & 2 on the driver station
        self.stick = wpilib.Joystick(0)

    def operatorControl(self):
        '''Runs the motors with tank steering'''

        self.myRobot.setSafetyEnabled(True)

        while self.isOperatorControl() and self.isEnabled():
            self.myRobot.arcadeDrive(self.stick)

            if self.stick.getRawButton(1):
                self.launcherTop.set(1)
                self.launcherBottom.set(-1)
            else:
                self.launcherTop.set(0)
                self.launcherBottom.set(0)

            if self.stick.getRawButton(8):
                self.ballIntake.set(1)
            else:
                self.ballIntake.set(0)

            wpilib.Timer.delay(0.005) # wait for a motor update time

if __name__ == '__main__':
    wpilib.run(MyRobot)
