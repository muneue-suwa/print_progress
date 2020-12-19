class PrintProgress:
    def __init__(self, progress_message, entire_num=0):
        self.PROGRESS_MESSAGE = progress_message
        self.entire_num = entire_num

    def print_start(self):
        print(f"{self.PROGRESS_MESSAGE}: ...", end="")

    def print_progress(self, current_num):
        progress_message = f"\r{self.PROGRESS_MESSAGE}: {current_num:2d}"
        if self.entire_num > 0:
            progress_message += f"/{self.entire_num}"
        print(progress_message, end=" ")

    def print_completed(self):
        print("Completed")


if __name__ == "__main__":
    from time import sleep
    pp1 = PrintProgress("Test1: with entire_num", 10)
    pp1.print_start()
    for i in range(10):
        pp1.print_progress(i + 1)
        sleep(1)
    pp1.print_completed()

    pp2 = PrintProgress("Test2: without entire_num")
    pp2.print_start()
    for i in range(10):
        pp2.print_progress(i + 1)
        sleep(1)
    pp2.print_completed()

    pp3 = PrintProgress("Test3: add entire_num in the middle")
    pp3.print_start()
    pp3.entire_num = 11
    for i in range(10):
        pp3.print_progress(i + 1)
        sleep(1)
    pp3.print_completed()
