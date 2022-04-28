using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace urgencia
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int a = 0;
            Console.WriteLine("Digite urgencia");
            a = int.Parse(Console.ReadLine());

            if (a < 4)
            {
                Console.WriteLine("Baixo");
            }
            else
            {
                if (a < 7)
                {
                    Console.WriteLine("Médio");
                }
                else
                {
                    if (a < 10)
                    {
                        Console.WriteLine("Alto");

                    }
                    else
                    {
                        Console.WriteLine("Grave");
                    }
                }
            }
            Console.ReadLine();
        }
    }
    

}