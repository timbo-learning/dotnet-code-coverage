#!/usr/bin/python3
import os
#import configargparse
import argparse

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
        default=os.getenv('targetdir','report-generator-coverage'))
    parser.add_argument('-hd', '--historydir',
        default=os.getenv('historydir', 'report-generator-history'))
    parser.add_argument('-rt', '--reporttypes',
        default=os.getenv('reporttypes',
            'HTML;HTMLChart;XML;PngChart;Badges'))
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
    
    args.verbosity >= 3 and print("\nINFO: " + headerSign + "Report Generator" + headerSign + "\n")

    cmd = "dotnet " + reportgenerator + reportgeneratorargs(args)
    print(cmd)
    os.system(cmd)
    args.verbosity >= 3 and print("INFO: " + headerSign + "End of Report Generator" + headerSign)

if __name__ == '__main__':
    main()
