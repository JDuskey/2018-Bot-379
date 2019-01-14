import magicbot
import wpilib
from wpilib.drive import DifferentialDrive
from robotpy_ext.control.button_debouncer import ButtonDebouncer

class MyRobot(magicbot.MagicRobot):

	def createObjects(self):

                self.leftStick = wpilib.Joystick(2)
                self.elevatorStick = wpilib.Joystick(1)
                self.rightStick = wpilib.Joystick(0)
                self.elevatorMotorOne = wpilib.Victor(2)
                self.elevatorMotorTwo = wpilib.Victor(3)
                self.left = wpilib.Victor(0)
                self.right = wpilib.Victor(1)
                self.myRobot = DifferentialDrive(self.left, self.right)
                self.elevator = wpilib.SpeedControllerGroup(self.elevatorMotorOne, self.elevatorMotorTwo)
                self.elevatorPot = wpilib.AnalogPotentiometer(0)

                self.gearshift = wpilib.DoubleSolenoid(0,0,1)
                self.trigger = ButtonDebouncer(self.rightStick,1,period=.5)
                self.gearshift.set(1)

	def teleopInit(self):
                pass

	def teleopPeriodic(self):
		self.myRobot.tankDrive(self.leftStick.getY(), self.rightStick.getY())
        if(self.trigger.get()):
        	if(self.gearshift.get() == 1):
            	self.gearshift.set(2)
            elif(self.gearshift.get() == 2):
                self.gearshift.set(1)
		self.elevator.set(self.elevatorStick.getY())
                 
if __name__ == '__main__':
	wpilib.run(MyRobot)
