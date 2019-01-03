using System;
using System.Collections.Generic;
using System.Text;

namespace Calculation.Basic
{
    public class Addition : ICalculation
    {
        private readonly decimal x;
        private readonly decimal y;

        public Addition(decimal x, decimal y)
        {
            this.x = x;
            this.y = y;
        }

        public decimal Calculate()
        {
            return x + y;
        }

        public void NotCoveredByTests()
        {
            string foo = "this method is not being tested";
        }

        public string CoveredOnNextBuild()
        {
            return "this method is covered on a second build";
        }
    }
}
