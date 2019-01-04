#!/usr/bin/python3
import os
import coverlet
import config
#import shutil

lcovOutput='lcov.info'
lcovFormat='lcov'

def main():
    coverlet.main([
        '--testfolder', config.primeFolder,
        '--format', lcovFormat,
        '--output', lcovOutput,
        '--target', config.primeTarget,
        '--no-test'
        ])

    os.rename(lcovOutput, os.path.join(config.primeFolder, lcovOutput))
    coverlet.main([
        '--testfolder', config.calculationFolder,
        '--format', lcovFormat,
        '--output', lcovOutput,
        '--target', config.calculationTarget,
        '--no-test'
        ])
    os.rename(lcovOutput, os.path.join(config.calculationFolder, lcovOutput))

if __name__ == '__main__':
    main()
