import os 

primeFolder = "PrimeServiceTests"
calculationFolder = "CalculationTests"
primeTarget        = os.path.join(
    primeFolder   , 'bin', 'Debug', 'netcoreapp2.1', 'PrimeServiceTests.dll')
calculationTarget  = os.path.join(
    calculationFolder , 'bin', 'Debug', 'netcoreapp2.1', 'CalculationTests.dll')
primeOutput       = 'prime.opencover.xml'
calculationOutput = 'calculation.opencover.xml'
outputFormat = 'opencover'
