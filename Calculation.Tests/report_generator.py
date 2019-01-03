#!/usr/bin/python3
import os
#import configargparse
import argparse

def parse_arguments(raw_args):
    calculationXml = os.path.join('..', 'calculation.opencover.xml')
    primeXml = os.path.join('..', 'prime.opencover.xml')
    defaultCoverageFiles = calculationXml + ';' + primeXml
    parser = argparse.ArgumentParser()
    #default_config_files="report-generator.conf.txt")
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
    #REPORT_GENERATOR_DLL="ReportGenerator.dll"
    #REPORT_GENERATOR_PATH = os.path.join(HOME, ".nuget", "packages", "reportgenerator", "4.0.4", "tools", "netcoreapp2.0", REPORT_GENERATOR_DLL)
    args = parse_arguments(raw_args)
    cmd = "dotnet " + reportgenerator + reportgeneratorargs(args)
    print(cmd)
    #os.path.join('..', 
    os.system(cmd)


if __name__ == '__main__':
    main()
#HOME=os.path.expanduser("~")
#REPORT_GENERATOR="reportgenerator"
#CALCULATION_COVERAGE_FILE="calculation.opencover.xml"
#PRIME_COVERAGE_FILE="prime.opencover.xml"
#ARGS=' "-reports:' + CALCULATION_COVERAGE_FILE \
#        + ';' + PRIME_COVERAGE_FILE + '"'\
#        + ' "-targetdir:report-generator-coverage"' \
#        + ' "-reporttypes:HTML;HTMLChart;XML;PngChart;Badges"' \
#        + ' "-historydir:"report-generator-history' \
#        #+ ' -verbosity:Info'
