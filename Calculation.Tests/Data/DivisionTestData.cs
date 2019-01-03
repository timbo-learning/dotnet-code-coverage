using System;
using System.Collections;
using System.Collections.Generic;
using System.Text;
using Calculation.Basic;

namespace Calculation.Tests.Data
{
    class DivisionTestData : IEnumerable<object[]>
    {
        public IEnumerator<object[]> GetEnumerator()
        {
            var x = new decimal(5);
            yield return new object[] { new Division(0, 5), new decimal(0)/5 };
            yield return new object[] { new Division(1, 100), 0.01 };
            yield return new object[] { new Division(2, -2), -1 };
            yield return new object[] { new Division(2, 3), new decimal(2)/3 };
            yield return new object[] { new Division(99, 1), 99 };
        }

        IEnumerator IEnumerable.GetEnumerator() => GetEnumerator();
    }
}
