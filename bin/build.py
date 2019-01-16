#!/usr/bin/python3
import os
import sys
import shutil
import argparse
import test_and_report

def parse_arguments(raw_args):
    parser = argparse.ArgumentParser()
    parser.add_argument('-k', '--key',
        required=True,
        )
    parser.add_argument('-s','--sonar-xml'
        #default="SonarQube.Analysis.xml"
        )
    parser.add_argument('-cwd', '--use-cwd-for-xml',
        default=True
        )
    parser.add_argument('-ss','--sonar-scanner',
        default=os.path.join("bin", "dotnet-sonarscanner")
        )
    parser.add_argument('-d', '--define',
        nargs='*')
    parser.add_argument('--test',
        dest='test', action='store_true')
    parser.add_argument('--no-test',
        dest='test', action='store_false')
    parser.set_defaults(test=False)
    return parser.parse_args(raw_args)

def sonar_args(args):

    key=""
    if (args.key):
        key=' /k:"' + args.key + '"'

    # /s: not working properly
    xml=""
    if (args.sonar_xml):
        cwd=""
        if (args.use_cwd_for_xml):
            cwd=os.getcwd() + '/'
        xml=' /s:"' + cwd + args.sonar_xml + '"'

    defined_variables=""
    for parameter in args.define:
        defined_variables+=' /d:' + parameter

    return key + xml + defined_variables

def sonar_cmd(args):

    return '"' + args.sonar_scanner + '"'

def build(args):
    sonarqubeXml="SonarQube.Analysis.xml"
    defaultSonarqubeXml=os.path.join("bin",".store","dotnet-sonarscanner","4.5.0","dotnet-sonarscanner", "4.5.0", "tools", "netcoreapp2.1", "any",
            sonarqubeXml)

    os.system("dotnet restore")
    os.system("dotnet tool install dotnet-sonarscanner --tool-path=bin")
    os.system("dotnet tool install coverlet.console --tool-path=bin")
    shutil.copy2(sonarqubeXml, defaultSonarqubeXml)
    shutil.copy2(sonarqubeXml, "bin")

    sonarscanner = sonar_cmd(args)
    sonar_full_cmd = sonarscanner + ' begin ' + sonar_args(args))
    print('+ ' + sonar_full_cmd)
    os.system( sonar_full_cmd )

    os.system("dotnet build")
    if (not args.test):
        sys.argv = [sys.argv[0]]
        test_and_report.main()
        #os.system("python " + os.path.join("bin","test_and_report.py"))
    os.system(sonarscanner +  ' end')

def main(raw_args=None):
    args = parse_arguments(raw_args)
    build(args)

if __name__ == '__main__':
    main()
