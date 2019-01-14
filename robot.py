import magicbot
import wpilib
from wpilib.drive import DifferentialDrive

class MyRobot(magicbot.MagicRobot):

	def createObjects(self):
                
                self.leftStick = wpilib.Joystick(2)
                self.rightStick = wpilib.Joystick(0)
                self.elevatorMotorOne = wpilib.Victor(2)
                self.elevatorMotorTwo = wpilib.Victor(3)
                self.left = wpilib.Victor(0)
                self.right = wpilib.Victor(1)
                self.myRobot = DifferentialDrive(self.left, self.right)
                self.elevator = wpilib.SpeedControllerGroup(self.elevatorMotorOne, self.elevatorMotorTwo)
                self.shift = wpilib.DoubleSolenoid(0,0,1)
                self.elevatorPot = wpilib.AnalogPotentiometer(0)
                
                
	def teleopInit(self):
                pass

	def teleopPeriodic(self):
                 self.myRobot.tankDrive(-self.leftStick.getY(), -self.rightStick.getY())
                 
                 
if __name__ == '__main__':
	wpilib.run(MyRobot)
