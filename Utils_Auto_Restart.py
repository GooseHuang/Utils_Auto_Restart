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



class InfoHub:
    def __init__(self):
        pass
INFO_HUB = InfoHub()



def looper(smc_list):

    INFO_HUB.N = -1 #-1

    res_list = []
    while INFO_HUB.N < (len(smc_list)-1):
        try:

            # Automation Start Here

            driver = init()
            driver.refresh()
            login(driver)
            prepare_page(driver)
            df = batch_search_smc(smc_list, driver, INFO_HUB.N)

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
    smc_list = ['', '', ...]

    N = 0 #-1

    # Auto restart if error
    df = looper(smc_list, N)

