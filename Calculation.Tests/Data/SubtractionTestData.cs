using System;
using System.Collections;
using System.Collections.Generic;
using System.Text;
using Calculation.Basic;

namespace Calculation.Tests.Data
{
    class SubtractionTestData : IEnumerable<object[]>
    {
        public IEnumerator<object[]> GetEnumerator()
        {
            yield return new object[] { new Subtraction(0, 0), 0 };
            yield return new object[] { new Subtraction(2, 2), 0 };
            yield return new object[] { new Subtraction(2, -2), 4 };
        }

        IEnumerator IEnumerable.GetEnumerator() => GetEnumerator();
    }
}
