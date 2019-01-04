#!/usr/bin/python3
import os
import coverlet
import lcov
import Calculation.Tests.report_generator

primeFolder = "PrimeServiceTests"
calculationFolder = "CalculationTests"
primeTarget        = os.path.join(
    primeFolder   , 'bin', 'Debug', 'netcoreapp2.1', 'PrimeServiceTests.dll')
calculationTarget  = os.path.join(
    calculationFolder , 'bin', 'Debug', 'netcoreapp2.1', 'CalculationTests.dll')
primeOutput = 'prime.opencover.xml'
calculationOutput = 'calculation.opencover.xml'
outputFormat = 'opencover'


def main():

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


if __name__ == '__main__':
    main()
