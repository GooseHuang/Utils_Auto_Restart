import logging
import os
FILE_PATH = os.path.dirname(os.path.abspath(__file__))
os.chdir(FILE_PATH)


LOGGING_FILE = os.path.join(FILE_PATH,'Run.log')

logging.basicConfig(filename=LOGGING_FILE, filemode='w', format='%(message)s')  # Without Name
logger = logging.getLogger('Maverick')
logger.setLevel(logging.INFO)

# Log to console
console_handler = logging.StreamHandler()
formatter = logging.Formatter('%(message)s')
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)
import time
import pandas as pd



class InfoHub:
    def __init__(self):
        pass
INFO_HUB = InfoHub()


def demo_run():
    # Do something

    df = pd.DataFrame({'N': INFO_HUB.N }, index=[0])


    print('Run once.')
    INFO_HUB.N += 1
    time.sleep(1)


    return df



def looper(target_list):

    res_list = []
    while INFO_HUB.N < (len(target_list)-1):
        try:

            # Automation Start Here

            # Run some code
            df = demo_run()
            

            # Automation End Here

            res_list.append(df)
        except Exception as e:
            logger.error("\n" + "#"*40 + " Error: looper " + "#" * 40, exc_info=True)
            logger.error("#" * 100 + '\n')

    df = pd.concat(res_list)
    return df


def main():

    # Fake code for demo
    target_list = ['example1', 'example2', 'example3']

    N = 0
    INFO_HUB.N = N

    # Auto restart if error
    df = looper(target_list)

    print(df)




if __name__ == '__main__':
    main()
    print('Done!')