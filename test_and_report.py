#!/usr/bin/python3
import os
import coverlet
import lcov

primeFolder = "PrimeService.Tests"
calculationFolder = "Calculation.Tests"
primeTarget        = os.path.join(
    primeFolder   , 'bin', 'Debug', 'netcoreapp2.1', 'PrimeService.Tests.dll')
calculationTarget  = os.path.join(
    calculationFolder , 'bin', 'Debug', 'netcoreapp2.1', 'Calculation.Tests.dll')
primeOutput = 'prime.opencover.xml'
calculationOutput = 'calculation.opencover.xml'
outputFormat = 'opencover'


def main():
    #Update lcov.info to see line coverage on VS Code
    lcov.main()

    coverlet.main([
        '--testfolder', primeFolder,
        '--format', outputFormat,
        '--output', primeOutput,
        '--target', primeTarget,
        '--no-test'
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


if __name__ == '__main__':
    main()
