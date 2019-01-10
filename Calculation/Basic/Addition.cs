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

        public string NotCoveredByTests()
        {
            string foo = "this method is not being tested";
            return foo;
        }

        public string CoveredOnNextBuild()
        {
            string foo = "this method is covered on a second build";
            return foo;
        }

        public void JenkinsBuild()
        {
            decimal z = x;
            z++;
            z += y;
            z += x;
            z++;
            z++;
            z++;
            z++;
            z++;
            z++;
            z++;
        }
    }
}
