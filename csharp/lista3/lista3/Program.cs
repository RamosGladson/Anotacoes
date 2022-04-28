using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace lista3
{
    internal class Program
    {
        static void Main(string[] args)
        {
            string[] produtos = new string[5];
            produtos[0] = "Chocolate";
            produtos[1] = "Refrigerante";
            produtos[2] = "Bolo";
            produtos[3] = "Sorvete";
            produtos[4] = "Pão";
            double[] precos = new double[5];
            precos[0] = 30;
            precos[1] = 50;
            precos[2] = 45;
            precos[3] = 60;
            precos[4] = 15;
            double[] atualizado = new double[5];

            for (int i = 0; i < 5; i++)
            {
                Console.WriteLine("{0,-15}...........................{1,5}", produtos[i], precos[i]);
                
            }
            Console.ReadLine();
            for (int i = 0; i < 5; i++)
            {
                atualizado[i] = precos[i] * 1.25;
            }
            Console.WriteLine("Preço atualizado:");
            for (int i = 0; i < 5; i++)
            {
                
                Console.WriteLine("{0,-15}...........................{1,10}", produtos[i], atualizado[i]);

            }
            Console.ReadLine();

        }
    }
}
