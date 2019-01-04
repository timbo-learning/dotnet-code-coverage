

namespace Calculation.Basic
{
    public class Subtraction : ICalculation
    {
        private readonly decimal x;
        private readonly decimal y;

        public Subtraction(decimal x, decimal y)
        {
            this.x = x;
            this.y = y;
        }

        public decimal Calculate()
        {
            return x - y;
        }

        public void CodedOnFourthBuild()
        {
            string foo = "";
            if (x % 2 == 0)
            {
                foo = "branch 1 coverage test";
            } else
            {
                foo = "branch 2 coverage test";
            }

            foo = "really";
            foo += " long";
            foo += " operation";
            foo += " with";
            foo += " a";
            foo += " lot";
            foo += " of";
            foo += " lines";
            foo += " to";
            foo += " be";
            foo += " tested";
        }
    }
}

