import sys
import time
import logging
import random as rng

class ConstantGenerator(object):
    def __init__(self):
        self.constants_list = self.load_constants()
        self.mathmatical_opers = self.load_math_opers()
        self.logger = self.load_logger()

    def load_constants(self):
        lc_constants_list = []
        with open('constants.txt', 'r+') as f:
            for line in f.readlines():
                lc_constants_list.append(line)
        return lc_constants_list

    def load_math_opers(self):
        return ['**', '//', '*', '/', '+', '-']

    def load_logger(self):
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s/%(name)s/%(levelname)s/%(message)s')
        file_handler = logging.FileHandler('rawlogs.txt')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        return logger

    def f(self):
        fResult = '{} {} {}'.format(float(rng.choice(self.constants_list)), rng.choice(self.mathmatical_opers),
                                    float(rng.choice(self.constants_list)))
        print(fResult)
        self.logger.info('Expression: {}'.format(fResult))
        print(eval(fResult))
        self.logger.info('Result: {}'.format(eval(fResult)))

def main(argv):
    cg = ConstantGenerator()
    sTime = time.time()
    for i in range(int(argv[0])):
        try:
            cg.f()
        except Exception as e:
            print(str(e))
            cg.logger.debug('ERROR: {}'.format(str(e)))
            continue
    print(time.time() - sTime)
    cg.logger.info('Duration: {}'.format(time.time() - sTime))

if __name__ == '__main__':
    main(sys.argv[1:])
