#!/usr/bin/python

# a cli survey tool

import sys
import getopt
import time
import string

from survey.survey import Survey
from survey.question import Question

survey_file=''
response_file=''

def getargs(argv):
    'analyze command input'
    global survey_file
    global response_file

    try:
        opts, args = getopt.getopt(argv,"hs:r:",["survey-file=","response-file="])
    except getopt.GetoptError:
        print ('COMMAND -s <survey-files> -r <response-file>')
        sys.exit(2)
    for opt, arg in opts:
        if opt in("-h", "--help"):
            print ('COMMAND -s <survey-files> -r <response-file>')
            sys.exit()
        elif opt in ("-s", "--survey-file"):
            survey_file = arg
        elif opt in ("-r", "--response-file"):
            response_file = arg
    
    if not survey_file:
        print ('survey file required.')
        sys.exit(2)

    if not response_file:
        print ('response file required.')
        sys.exit(2)

if __name__ == "__main__":
    getargs(sys.argv[1:])

    app = Survey(survey_file, response_file)
    app.participation()
    app.print_result()
