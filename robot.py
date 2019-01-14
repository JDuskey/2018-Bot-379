import magicbot
import wpilib
class MyRobot(magicbot.MagicRobot):

	def createObjects(self):
                
                self.leftStick = wpilib.Joystick(2)
                self.rightStick = wpilib.Joystick(0)
                self.elevatorMotorOne = wpilib.Victor(2)
                self.elevatorMotorTwo = wpilib.Victor(3)


                self.elevator = wpilib.SpeedControllerGroup(self.elevatorMotorOne, self.elevatorMotorTwo)
	
                self.elevatorPot = wpilib.AnalogPotentiometer(0)
	def teleopInit(self):
		pass

	def teleopPeriodic(self):
		pass
if __name__ == '__main__':
	wpilib.run(MyRobot)
