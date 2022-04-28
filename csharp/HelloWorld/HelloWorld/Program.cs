using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;


namespace HelloWorld
{
    internal class Program
    {
        enum opcao { Atualizar = 1, Sair };
        
        static void Main(string[] args)
        {
            Console.WriteLine($"Digite {(opcao)1} ou {(opcao)2}");
            opcao escolha = Console.ReadLine();
            Console.ReadLine();
          
        }
    }
}
