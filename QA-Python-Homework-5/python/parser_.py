from optparse import OptionParser
import os

def parser():
    parser = OptionParser()
    parser.add_option('--json', action='store_true', dest='json' , default=False)
    parser.add_option('-f','--filedir',dest='filedir',default=os.path.abspath(os.path.join(os.path.dirname(__file__),'..','log','access.log')))
    return parser.parse_args()