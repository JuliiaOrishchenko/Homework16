class CustomException(Exception):
    def __init__(self, msg):
        self.msg = msg
        with open("logs.txt", "w", encoding="UTF-8") as file:
            file.write(self.msg)


def func(line):
    if not isinstance(line, str):
        raise CustomException(f"{line} should be string only")


func(-4)
