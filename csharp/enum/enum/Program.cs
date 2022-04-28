using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace @enum
{
    internal class Program
    {
        enum opcao { Azul, Verde, Amarelo }
        static void Main(string[] args)
        {
        //    string[] nomes = {"joao", "maria", "jose" };
            for (int indice = 0; indice < 3; indice++)
            {
                Console.WriteLine($"{indice + 1}ª cor:{(opcao)indice}");
                Console.ReadLine();
            }
                

        

        }
    }
}
