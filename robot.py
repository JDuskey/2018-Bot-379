import magicbot
import wpilib
from wpilib.drive import DifferentialDrive

class MyRobot(magicbot.MagicRobot):

	def createObjects(self):
                self.left = wpilib.Victor(0)
                self.right = wpilib.Victor(1)
                self.leftStick = wpilib.Joystick(2)
                self.rightStick = wpilib.Joystick(0)
                self.myRobot = DifferentialDrive(self.left, self.right)

	def teleopInit(self):
                pass

	def teleopPeriodic(self):
                 self.myRobot.arcadeDrive(self.rightStick.getY(), -self.rightStick.getThrottle() * .4)
                 
                 
if __name__ == '__main__':
	wpilib.run(MyRobot)
