#!/usr/bin/python3
import os
import argparse

def parse_arguments(raw_args):
    parser = argparse.ArgumentParser()
    parser.add_argument('-tf', '--testfolder',
        default=os.getenv('testfolder', 'Calculation.Tests')
        )
    parser.add_argument('-f', '--format',
        default=os.getenv('format', 'opencover')
        )
    parser.add_argument('-o', '--output',
        default=os.getenv('output', 'output.opencover.xml')
        )
    parser.add_argument('-t', '--target',
        default=os.getenv('target', 'calculation')
        )
    parser.add_argument('--test', dest='test', action='store_true')
    parser.add_argument('--no-test', dest='test', action='store_false')
    parser.set_defaults(test='True')
    return parser.parse_args(raw_args)

def coverlet(args):
    print(args)
    cmd = "coverlet %(target)s" \
            + ' --exclude "[xunit.runner.*]*" ' \
            + ' --target dotnet --targetargs "test %(testfolder)s --no-build" ' \
            + ' -o %(output)s' \
            + ' --format %(format)s' \
            # lcov to show lines on Visual Studio Code
    cmd = cmd % {
        'target': args.target,
        'testfolder': args.testfolder,
        'output': 'prime.opencover.xml',
        'format': 'opencover'
        } 
    print(">>>>" + cmd)
    return cmd

def main(raw_args=None):
    args = parse_arguments(raw_args)
    cmd = coverlet(args)
    args.test and os.system("dotnet test")
    os.system(cmd)

if __name__ == '__main__':
    main()
