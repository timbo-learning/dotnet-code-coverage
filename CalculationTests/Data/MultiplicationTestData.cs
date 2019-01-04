using System;
using System.Collections;
using System.Collections.Generic;
using System.Text;
using Calculation.Basic;

namespace Calculation.Tests.Data
{
    class MultiplicationTestData : IEnumerable<object[]>
    {
        public IEnumerator<object[]> GetEnumerator()
        {
            yield return new object[] { new Multiplication(0, 5), 0 };
            yield return new object[] { new Multiplication(2, 2), 4 };
            yield return new object[] { new Multiplication(2, -2), -4 };
            yield return new object[] { new Multiplication(9, 9), 81 };
            yield return new object[] { new Multiplication(22, 10), 220 };
        }

        IEnumerator IEnumerable.GetEnumerator() => GetEnumerator();
    }
}
