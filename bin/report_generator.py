#!/usr/bin/python3
import os
#import configargparse
import argparse
import logger
import config

headerSign = "=" * 10


def parse_arguments(raw_args):
    calculationXml = os.path.join('..', 'calculation.opencover.xml')
    primeXml = os.path.join('..', 'prime.opencover.xml')
    defaultCoverageFiles = calculationXml + ';' + primeXml
    parser = argparse.ArgumentParser()
    parser.add_argument('-c','--coverage',
        default=os.getenv('coverage',defaultCoverageFiles),
        help='coverage file')
    parser.add_argument('-td', '--targetdir',
        default=os.getenv('targetdir',
            os.path.join('..',
                'report-generator-coverage')))
    parser.add_argument('-hd', '--historydir',
        default=os.getenv('historydir', 
            os.path.join('..',
                'report-generator-history')))
    parser.add_argument('-rt', '--reporttypes',
        default=os.getenv('reporttypes',
            'HTML;HTMLChart;XML;PngChart;Badges'))
    parser.add_argument('-cd', '--chdir',
        type=bool, default=True)
    parser.add_argument('-v', '--verbosity',
        type=int, default=3)
    parser.add_argument('-q', '--quiet',
        dest='verbosity', action='store_const', const=0)

    #print(parser.format_values())
    return parser.parse_args(raw_args)


def reportgeneratorargs(args):
    print(args)
    return ' "-reports:'  + args.coverage    + '"' \
        + ' "-targetdir:'   + args.targetdir   + '"' \
        + ' "-reporttypes:' + args.reporttypes + '"' \
        + ' "-historydir:'  + args.historydir  + '"' 
        #+ ' -verbosity:Info'

def main(raw_args=None):
    reportgenerator = "reportgenerator"
    args = parse_arguments(raw_args)
    log = logger.Logger(name=reportgenerator, format='level')

    log.infoTitle()

    if args.chdir:
        os.chdir(config.calculationFolder)

    cmd = "dotnet " + reportgenerator + reportgeneratorargs(args)
    print(cmd)
    os.system(cmd)


    if args.chdir:
        os.chdir('..')

    log.infoEndTitle()

if __name__ == '__main__':
    main()
