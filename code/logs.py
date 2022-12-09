
import logging


extraData = {
        'user': 'joem@example.com'
}


def basic_logging():
    # use basicConfig to configure logging
    logging.basicConfig(level=logging.DEBUG, 
                        filename='output.log', 
                        filemode='w')
    
    # trying each of the log levels
    logging.debug('this is a debug message')
    logging.info('this is an info message')
    logging.warning('this is a warning message')
    logging.error('this is an error message')
    logging.critical('this is a critical message')

    # output formatted string to log file
    logging.info("Here's a {} variable and an int:".format("string", 10))


def custom_logging():
    # use basicConfig to configure logging
    fmtstr = "User:%(user)s %(asctime)s: %(levelname)s: %(funcName)s Line:%(lineno)d %(message)s"
    datestr = "%m/%d/%Y %I:%M:%S %p"
    logging.basicConfig(level=logging.DEBUG, 
                        filename='output.log', 
                        filemode='w',
                        format=fmtstr,
                        datefmt=datestr
    )


    logging.info("This is an info-level log message", extra=extraData)
    logging.warning("This is an warning-level log message", extra=extraData)



def anotherFunc():
    logging.debug("this is a debug-level log message")


def main():
    # basic_loggin()
    custom_logging()


if __name__ == "__main__":
    main()
