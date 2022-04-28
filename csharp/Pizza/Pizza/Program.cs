using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Pizza
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine(CalculaArea(30));
            Console.Read();

            double CalculaArea(double raio)
            {
                double area = (raio * raio) * 3.14;
                return area;    
            }
        }
    }
}
