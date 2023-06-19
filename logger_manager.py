import time
<<<<<<< Updated upstream

class Logger:
    def __init__(self) -> None:
        self.start_time = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
        self.log_file = open("log/" + self.start_time + ".log", "w")
        self.print_consol = True
        self.is_logging = True

        self.log("Starting", "Hello from Logmanager")

    @staticmethod
    def _get_time():
        return time.strftime('%H:%M:%S', time.localtime())
    
    @staticmethod
    def _gen_log(log_type, log):
        log_str = ""
        for lol in log:
            log_str += str(lol) + " "
        return f"[{Logger._get_time()}] [{log_type}] {log_str} \n"

    def log(self, log_type:any, *log):
        if not self.is_logging:
            return

        output = Logger._gen_log(log_type, log)

        if self.print_consol:
            print(output.replace("\n", ""))

        self.log_file.write(output)

    def stop_logging(self):
        self.log("Stopping", "Stopping logger, closing file stream")
        self.log_file.close()

if __name__ == "__main__":
    logger = Logger()
    logger.log("Starting", "du huan", logger)
    logger.stop_logging()
=======
import os

def _get_time():
    return time.strftime('%H:%M:%S', time.localtime())

def _gen_log(log_type, log):
    log_str = ""
    for lol in log:
        log_str += str(lol) + " "
    return f"[{_get_time()}] [{log_type}] {log_str} \n"

def log(log_type:any, *log):
    if not Logger().logger.is_logging:
        return

    output = _gen_log(log_type, log)

    if Logger().logger.print_consol:
        print(output.replace("\n", ""))

    Logger().logger.log_file.write(output)

def stop_logging():
    log("Stopping", "Stopping logger, closing file stream")
    Logger().logger.log_file.close()
    Logger().logger.is_logging = False

def log_print(*args):
    message = " ".join(str(arg) for arg in args)
    log("Print", message)


class Logger:
    logger = None

    def __init__(self) -> None:
        if Logger.logger == None:
            self.start_time = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())

            if not os.path.exists("log"):
                os.mkdir("log")

            self.log_file = open("log/" + self.start_time + ".log", "w")
            self.print_consol = True
            self.is_logging = True

            Logger.logger = self
            log("Starting", "Hello from Logmanager")
            log("Starting", "Creating file:", self.log_file.name.replace("log/", ""))
        else:
            self = Logger.logger

if __name__ == "__main__":
    logger = Logger()
    logger2 = Logger()
    print("stop2")
>>>>>>> Stashed changes
