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

        self.setTitle()

        if not self.logger.hasHandlers():
            if not filename:
                self.handler = self.StreamHandler(stream)
            else:
                self.handler = self.FileHandler(filename)
        else:
            self.handler = self.logger.handlers[0]

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

    def setTitle(self, delimiter=None, title=" %(message)s "):
        if (delimiter is None):
            delimiter = "="

        self.line = delimiter * 10
        self.titleFormat = self.line + title + self.line

    def infoEndTitle(self, message=None, breakLine=True, delimiter=None):
        if (delimiter is None):
            delimiter='-'

        self.infoTitle(message=message, breakLine=breakLine, delimiter=delimiter)

    def infoTitle(self, message=None, breakLine=True, delimiter=None):
        if (delimiter is None):
            delimiter='='

        if (message is None):
            self.setTitle(delimiter=delimiter, title=" %(name)s ")

        if breakLine:
            formatStr = "\n" + self.titleFormat + "\n"
        else:
            formatStr = self.titleFormat

        self.handler.setFormatter(logging.Formatter(formatStr))
        self.info(message)

        # Reset configs
        self.handler.setFormatter(logging.Formatter(self.format))
        #self.setTitle()
