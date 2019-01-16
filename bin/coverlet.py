#!/usr/bin/python3
import os
import argparse
import config
import logger

DEFAULT_OPENCOVER_OUTPUT='coverage.opencover.xml'
DEFAULT_LCOV_OUTPUT     ='coverage.info'

def validate_args(args):
    if not args.testfolder:
        raise ValueError("--testfolder required")
    if not args.target:
        raise ValueError("--target required")

def parse_arguments(raw_args):
    parser = argparse.ArgumentParser()
    parser.add_argument('-tf', '--testfolder',
        default=os.getenv('testfolder', config.calculationFolder )
        )
    parser.add_argument('-t', '--target',
        default=os.getenv('target', config.calculationTarget )
        )
    #parser.add_argument('-f', '--format',
    #    action='append'
    #    )
    #parser.add_argument('-o', '--output',
    #    default=os.getenv('output', 'output.opencover.xml')
    #    )
    parser.add_argument('--test', dest='test', action='store_true')
    parser.add_argument('--no-test', dest='test', action='store_false')
    parser.set_defaults(test=True)
    return parser.parse_known_args(raw_args)

def coverlet(args):
    coverletPath = os.path.join('bin', 'coverlet')
    print(args)
    cmd = "%(coverlet)s %(target)s" \
            + ' --exclude "[xunit.runner.*]*" ' \
            + ' --target dotnet --targetargs "test %(testfolder)s --no-build" '
            #+ ' -o %(output)s' \
            #+ ' --format %(format)s' \
            # lcov to show lines on Visual Studio Code
    cmd = cmd % {
        'coverlet': coverletPath,
        'testfolder': args.testfolder,
        'target': args.target
    }
    return cmd

def main(raw_args=None):
    log = logger.Logger(name='coverlet', format='level')
    log.infoTitle()
    args, child_args = parse_arguments(raw_args)
    validate_args(args)
    cmd = coverlet(args)
    print("child_args:",child_args)
    cmd += " " + " ".join(child_args)
    args.test and os.system("dotnet test")
    print(">>>>" + cmd + " ")
    os.system(cmd)
    log.infoEndTitle()

if __name__ == '__main__':
    main()
