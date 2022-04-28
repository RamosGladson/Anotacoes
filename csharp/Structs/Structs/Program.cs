using System;
using System.Collections.Generic; // listas
using System.Linq; // manipulação de listas
using System.Text;
using System.Threading;
namespace Structs
{
    
    internal class Program
    {
        struct Cachorro
        {
            public int peso;
            public int idade;
            public Cachorro(int peso, int idade)
            {
                this.peso = peso;
                this.idade = idade;
            }
        }

        static void Main(string[] args)
        {
            Cachorro meg = new Cachorro(2, 5);
            Console.WriteLine(meg.peso);
            Thread.Sleep(10000);
        }
    }
}
