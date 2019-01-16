#!/usr/bin/python3
import os
import sys
import shutil
import argparse
import config
import coverlet
import report_generator
import json

def get_version(version=None, increment=True):
    with open("config.json","r+") as fp:
        config_json = json.load(fp)
        if not version:
            version = config_json['version']
        else:
            increment=False
        major, minor, patch = version.split('.')
        if (increment):
            patch = int(patch)
            patch += 1
            patch = str(patch)
        version = "%(major)s.%(minor)s.%(patch)s" % {
            'major': major,
            'minor': minor,
            'patch': patch
        }
        #print("version is: ", version)
        config_json['version'] = version

        fp.seek(0)
        json.dump(config_json, fp)

        return version
        

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
    parser.add_argument('-v', '--version')
    parser.add_argument('--increment-version',
        dest='increment_version', action='store_true')
    parser.add_argument('--no-increment-version',
        dest='increment_version', action='store_true')
    parser.set_defaults(increment_version=True)
    parser.add_argument('-d', '--define',
        action='append')
    parser.add_argument('--test',
        dest='test', action='store_true')
    parser.add_argument('--no-test',
        dest='test', action='store_false')
    parser.set_defaults(test=True)
    return parser.parse_known_args(raw_args)

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

    if not args.define:
        args.define=[]
    #args.define.append( 'sonar.projectVersion=' + get_version(args.version, args.increment_version) )
    
    defined_variables=[' /d:' + parameter for parameter in args.define]
    defined_variables=" ".join(defined_variables)
    #print(args.define, defined_variables)
    return key + xml + " /v:" + get_version(args.version, args.increment_version) + defined_variables

def sonar_cmd(args):

    return '"' + args.sonar_scanner + '"'

def coverlet_call(target, folder, output, child_args):
    print("child_args:", child_args)
    arglist = [
        '--testfolder', folder,
        '--target', target,
        '--format', config.outputFormat,
        #'--output', config.primeOutput,
        '--format', 'lcov',
        #'--output', 'prime.lcov.info',
        '--no-test'
        ]
    arglist.extend(child_args)
    print('coverlet.main ', arglist)
    coverlet.main(arglist)
    os.rename(coverlet.DEFAULT_OPENCOVER_OUTPUT, output)
    #Update lcov.info to see line coverage on VS Code
    os.rename(coverlet.DEFAULT_LCOV_OUTPUT, os.path.join(folder, 'lcov.info'))

def test(child_args):
    os.system("dotnet test")

    coverlet_call(target=config.primeTarget, folder=config.primeFolder, output=config.primeOutput, child_args=child_args)
    coverlet_call(target=config.calculationTarget, folder=config.calculationFolder, output=config.calculationOutput, child_args=child_args)

    #lcov.main()
    #Generate the report using Report Generator
    report_generator.main([])

def build(args, child_args):
    sonarqubeXml="SonarQube.Analysis.xml"
    defaultSonarqubeXml=os.path.join("bin",".store","dotnet-sonarscanner","4.5.0","dotnet-sonarscanner", "4.5.0", "tools", "netcoreapp2.1", "any",
            sonarqubeXml)

    os.system("dotnet restore")
    os.system("dotnet tool install dotnet-sonarscanner --tool-path=bin")
    os.system("dotnet tool install coverlet.console --tool-path=bin")
    shutil.copy2(sonarqubeXml, defaultSonarqubeXml)
    shutil.copy2(sonarqubeXml, "bin")

    sonarscanner = sonar_cmd(args)
    sonar_full_cmd = sonarscanner + ' begin ' + sonar_args(args)
    print('+ ' + sonar_full_cmd)
    os.system( sonar_full_cmd )

    os.system("dotnet build")
    if (args.test):
        test(child_args)
        #sys.argv = [sys.argv[0]]
        #test_and_report.main()
        #os.system("python " + os.path.join("bin","test_and_report.py"))
    os.system(sonarscanner +  ' end')

def main(raw_args=None):
    args, child_args = parse_arguments(raw_args)
    build(args, child_args)

if __name__ == '__main__':
    main()
