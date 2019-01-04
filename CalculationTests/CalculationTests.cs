using System;
using Xunit;
using Calculation.Basic;
using Calculation.Tests.Data;
using FluentAssertions;

namespace Calculation.Basic.Tests
{
    public class CalculationTests
    {
        [Theory]
        [ClassData(typeof(AdditionTestData))]
        [ClassData(typeof(SubtractionTestData))]
        [ClassData(typeof(MultiplicationTestData))]
        [ClassData(typeof(DivisionTestData))]
        public void Calculate(ICalculation calculation, decimal result)
        {
            calculation.Calculate().Should().Be(result);
        }

        [Fact]
        public void CoveredOnSecondBuild()
        {
            Addition calculation = new Addition(1, 1);
            calculation.CoveredOnNextBuild();
        }

        [Fact]
        public void TestedOnFourthBuild()
        {
            Subtraction calculation = new Subtraction(2, 0);
            calculation.CodedOnFourthBuild();
        }

        [Fact]
        public void TestedOnFifthBuild()
        {
            Subtraction calculation = new Subtraction(3, 0);
            calculation.CodedOnFourthBuild();
        }
    }
}
