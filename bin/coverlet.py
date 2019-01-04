#!/usr/bin/python3
import os
import argparse

def validate_args(args):
    if not args.testfolder:
        raise ValueError("--testfolder required")
    if not args.target:
        raise ValueError("--target required")

def parse_arguments(raw_args):
    parser = argparse.ArgumentParser()
    parser.add_argument('-tf', '--testfolder',
        default=os.getenv('testfolder', None )
        )
    parser.add_argument('-f', '--format',
        default=os.getenv('format', 'opencover')
        )
    parser.add_argument('-o', '--output',
        default=os.getenv('output', 'output.opencover.xml')
        )
    parser.add_argument('-t', '--target',
        default=os.getenv('target', None )
        )
    parser.add_argument('--test', dest='test', action='store_true')
    parser.add_argument('--no-test', dest='test', action='store_false')
    parser.set_defaults(test='True')
    return parser.parse_args(raw_args)

def coverlet(args):
    print(args)
    coverletPath = os.path.join('bin', 'coverlet')
    cmd = "%(coverlet)s %(target)s" \
            + ' --exclude "[xunit.runner.*]*" ' \
            + ' --target dotnet --targetargs "test %(testfolder)s --no-build" ' \
            + ' -o %(output)s' \
            + ' --format %(format)s' \
            # lcov to show lines on Visual Studio Code
    cmd = cmd % {
        'coverlet': coverletPath,
        'target': args.target,
        'testfolder': args.testfolder,
        'output': args.output,
        'format': args.format
        } 
    print(">>>>" + cmd)
    return cmd

def main(raw_args=None):
    args = parse_arguments(raw_args)
    validate_args(args)
    cmd = coverlet(args)
    args.test and os.system("dotnet test")
    os.system(cmd)

if __name__ == '__main__':
    main()
