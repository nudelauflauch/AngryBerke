import time

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