using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace cor
{
    internal class Program
    {
        //enum Cor { Azul=1, Verde, Amarelo, Vermelho }
        static void Main(string[] args)
        {
            Console.WriteLine(Calculadora.soma(1, 2));
            Console.ReadLine();
        }
        public static class Calculadora
        {
            public static double soma(double a, double b)
            {
                return a + b;
            }
        }
    }
}
