using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace lista2
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int i = 0, aux = 0, a = 0;
            Console.WriteLine("Quantos números vc quer digitar?");
            a = int.Parse(Console.ReadLine());

            int[] num = new int[a];
            while (i < num.Length)
            {
                
                Console.WriteLine($"digite {i+1}º numero");
                num[i] = int.Parse(Console.ReadLine());
                i++;
            }
            

            for (int c = 0; c < num.Length; c++)
            {
                for (i = 0; i < num.Length - 1; i++)
                {
                    if (num[i] > num[i + 1])
                    {
                        aux = num[i];
                        num[i] = num[i + 1];
                        num[i + 1] = aux;
                    }
                }
            }
            Console.WriteLine($"O menor valor é {num[0]}");
            foreach (int j in num)
            {
                Console.WriteLine(j);
            }
            Console.ReadLine();
            
        }
    }
}
