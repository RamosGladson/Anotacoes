using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Formula1
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int velocidade = 1, vezes = 0;
            
            while (velocidade > 0)
            {
                Console.WriteLine("digite a velocidade:");
                velocidade = int.Parse(Console.ReadLine());
                if (velocidade > 200)
                {
                    vezes++;
                }

            }
            Console.WriteLine($"você ultrapassou a velocidade permitida {vezes} vezes");
            Console.ReadLine();
        }
    }
}
