using System;
using System.Collections;
using System.Collections.Generic;
using System.Text;
using Calculation.Basic;

namespace Calculation.Tests.Data
{
    class AdditionTestData : IEnumerable<object[]>
    {
        public IEnumerator<object[]> GetEnumerator()
        {
            yield return new object[] { new Addition(0, 0), 0 };
            yield return new object[] { new Addition(2, 2), 4 };
            yield return new object[] { new Addition(2, -2), 0 };
        }

        IEnumerator IEnumerable.GetEnumerator() => GetEnumerator();
    }
}
