using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Triangulo
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine(CalculoAreaTriangulo(250, 350));
            Console.Read();
            double CalculoAreaTriangulo(double cateto1, double cateto2)
            {
                double area = (cateto1 * cateto2) / 2;
                return area;    

            }

        }
    }
}
