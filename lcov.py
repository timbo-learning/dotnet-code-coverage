#!/usr/bin/python3
import os
import coverlet
import test_and_report
#import shutil

lcovOutput='lcov.info'
lcovFormat='lcov'

def main():
    coverlet.main([
        '--testfolder', test_and_report.primeFolder,
        '--format', lcovFormat,
        '--output', lcovOutput,
        '--target', test_and_report.primeTarget,
        '--no-test'
        ])

    os.rename(lcovOutput, os.path.join(test_and_report.primeFolder, lcovOutput))
    coverlet.main([
        '--testfolder', test_and_report.calculationFolder,
        '--format', lcovFormat,
        '--output', lcovOutput,
        '--target', test_and_report.calculationTarget,
        '--no-test'
        ])
    os.rename(lcovOutput, os.path.join(test_and_report.calculationFolder, lcovOutput))

if __name__ == '__main__':
    main()
