#!/usr/bin/python3
import os
import coverlet
import lcov
import report_generator
from config import *

def main(args=None):

    coverlet.main([
        '--testfolder', primeFolder,
        '--format', outputFormat,
        '--output', primeOutput,
        '--target', primeTarget,
        '--test'
        ])

    coverlet.main([
        '--testfolder', calculationFolder,
        '--format', outputFormat,
        '--output', calculationOutput,
        '--target', calculationTarget,
        '--no-test'
        ])
    #os.system('python3 coverlet.py ' + \
    #    ' -tf ' + primeFolder  + \
    #    ' -f  ' + outputFormat + \
    #    ' -o  ' + primeOutput  + \
    #    '-t  ' + primeBin)

    #Update lcov.info to see line coverage on VS Code
    lcov.main()

    #Generate the report using Report Generator
    report_generator.main()


if __name__ == '__main__':
    main()
