import logging

class Logger:
    def __init__(self, name='Timbo', level=logging.INFO,
            filename=None, stream=None,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'):
        self.logger = logging.getLogger(name)
        self.level = level
        self.logger.setLevel(level)

        self.format = format

        if format is "level":
            self.format = '%(levelname)s: %(message)s'

        self.delimiter = "=" * 10
        self.titleFormat = self.delimiter + " %(message)s " + self.delimiter

        if not filename:
            self.handler = self.StreamHandler(stream)
        else:
            self.handler = self.FileHandler(filename)

    def FileHandler(self, filename, format=None
            #, mode, delay):
            ):
        if not format:
            format = self.format

        self.handler = logging.FileHandler(filename)
        self.handler.setLevel(self.level)
        formatter = logging.Formatter(format)
        self.handler.setFormatter(formatter)
        self.logger.addHandler(self.handler)

        return self.handler


    def StreamHandler(self, stream=None, format=None):
        if not format:
            format = self.format

        self.handler = logging.StreamHandler(stream)
        self.handler.setLevel(self.level)
        formatter = logging.Formatter(format)
        self.handler.setFormatter(formatter)
        self.logger.addHandler(self.handler)

        return self.handler

    def info(self, message):
        self.logger.info(message)
    def warn(self, message):
        self.logger.warn(message)
    def error(self, message):
        self.logger.error(message)
    def debug(self, message):
        self.logger.debug(message)
    def fatal(self, message):
        self.logger.fatal(message)
    def critical(self, message):
        self.logger.critical(message)

    def infoTitle(self, message, breakLine=True):

        if breakLine:
            formatStr = "\n" + self.titleFormat + "\n"
        else:
            formatStr = self.titleFormat
        
        self.handler.setFormatter(logging.Formatter(formatStr))
        self.logger.info(message)
        self.handler.setFormatter(logging.Formatter(self.format))
