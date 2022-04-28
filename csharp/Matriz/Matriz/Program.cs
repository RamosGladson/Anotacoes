using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Matriz
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Digite a ordem da matriz quadrada:");
            int n = int.Parse(Console.ReadLine());
            int[,] matriz = new int[n, n];
            for (int i = 0; i < n; i++)
            {
                for (int j = 0; j < n; j++)
                {
                    Console.WriteLine($"Digite o {j + 1}º numero da {i + 1}ª linha");
                    matriz[i, j] = int.Parse(Console.ReadLine());
                }
            }
            for (int i = 0; i < n; i++)
            {
                Console.WriteLine(matriz[i, i]);
            }
            
            



            Console.ReadLine();

        }
    }
}
