#!/usr/bin/python3
import os
import shutil
import argparse

def parse_arguments(raw_args):
    parser = argparse.ArgumentParser()
    parser.add_argument('-k', '--key',
        required=True,
        )
    return parser.parse_args(raw_args)


def build(args):
    sonarqubeXml="SonarQube.Analysis.xml"
    defaultSonarqubeXml=os.path.join("bin",".store","dotnet-sonarscanner","4.5.0","dotnet-sonarscanner", "4.5.0", "tools", "netcoreapp2.1", "any",
            sonarqubeXml)

    sonarscanner=os.path.join("bin", "dotnet-sonarscanner")  + ' '
    os.system("dotnet restore")
    os.system("dotnet tool install dotnet-sonarscanner --tool-path=bin")
    os.system("dotnet tool install coverlet.console --tool-path=bin")
    shutil.copy2(sonarqubeXml, defaultSonarqubeXml)
    shutil.copy2(sonarqubeXml, "bin")


    key=""
    if (args.key):
        key=' /k:"' + args.key + '"'

    os.system(
            sonarscanner + ' begin ' + key)

    os.system("dotnet build")
    os.system("python " + os.path.join("bin","test_and_report.py"))
    os.system(sonarscanner +  "end")

def main(raw_args=None):
    args = parse_arguments(raw_args)
    build(args)

if __name__ == '__main__':
    main()
