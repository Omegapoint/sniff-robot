from gpiozero import CamJamKitRobot
from gpiozero import LineSensor as _LineSensor


class LineSensor:
    __queue_len = 2
    __sample_rate = 400
    __tolerance = 0.5

    def __init__(self, input_pin):
        self.__line_sensor = _LineSensor(
            input_pin,
            queue_len=self.__queue_len,
            sample_rate=self.__sample_rate
        )

    def is_over_line(self):
        return self.__line_sensor.value < self.__tolerance


class Sniff:
    __left_line_sensor_input_pin = 17
    __right_line_sensor_input_pin = 18
    __speed = 0.3

    def __init__(self):
        self.__robot = CamJamKitRobot()
        self.left_line_sensor = LineSensor(self.__left_line_sensor_input_pin)
        self.right_line_sensor = LineSensor(self.__right_line_sensor_input_pin)

    def forward(self):
        self.__robot.forward(self.__speed)

    def turn_left(self):
        self.__robot.left_motor.forward(0)
        self.__robot.right_motor.forward(self.__speed)

    def turn_right(self):
        self.__robot.right_motor.forward(0)
        self.__robot.left_motor.forward(self.__speed)

    def stop(self):
        self.__robot.stop()


def main():
    robot = Sniff()

    try:
        while True:
            line_on_left = robot.left_line_sensor.is_over_line()
            line_on_right = robot.right_line_sensor.is_over_line()

            # Add logic here to make the robot follow the white line

    except KeyboardInterrupt:
        robot.stop()


if __name__ == "__main__":
    main()
