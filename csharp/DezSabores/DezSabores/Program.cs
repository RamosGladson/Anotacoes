using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace DezSabores
{
    internal class Program
    {
        enum Pizza {Calabresa, QuatroQueijos, Bacon, Frango, File, Abobora, Abacate, Banana, Abacaxi, Chocolate };
        static void Main(string[] args)
        {
            for (int i = 0; i < 10; i++)
            {
                Console.WriteLine($"Temos o sabor: {(Pizza)i}, aproveite a refeição");
            }
            Console.ReadLine();

        }
    }
}
