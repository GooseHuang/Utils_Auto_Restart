import logging

LOGGING_FILE = os.path.join(FILE_PATH,'GucciWebScrapping.log')

logging.basicConfig(filename=LOGGING_FILE, filemode='w', format='%(message)s')  # Without Name
logger = logging.getLogger('Maverick')
logger.setLevel(logging.INFO)

# Log to console
console_handler = logging.StreamHandler()
formatter = logging.Formatter('%(message)s')
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)
import time



class InfoHub:
    def __init__(self):
        pass
INFO_HUB = InfoHub()


def demo_run():
    # Do something
    print('Run once.')
    INFO_HUB.N +=1
    time.sleep(1)
    return



def looper(target_list):

    INFO_HUB.N = -1 #-1

    res_list = []
    while INFO_HUB.N < (len(target_list)-1):
        try:

            # Automation Start Here

            # Run some code
            demo_run()
            

            # Automation End Here

            res_list.append(df)
        except Exception as e:
            driver.quit()
            logger.error("\n" + "#"*40 + " Error: looper " + "#" * 40, exc_info=True)
            logger.error("#" * 100 + '\n')

    df = pd.concat(res_list)
    return df


def main():

    # Fake code for demo
    target_list = ['example1', 'example2', 'example3']

    N = 0 #-1

    # Auto restart if error
    df = looper(smc_list, N)

