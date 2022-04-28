using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace horário_mercado
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int hora = 0;
            while (hora >=0)
            {
                Console.WriteLine("Digite a hora:");
                hora = int.Parse(Console.ReadLine());

                if (hora >=7 && hora <= 17)
                {
                    Console.WriteLine("Aberto!");
                }
                else
                {
                    Console.WriteLine("Fechado!");
                }
            }
        }
    }
}
