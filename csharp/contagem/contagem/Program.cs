using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading;


namespace contagem
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Lançamento do foguete em:");
            for (int i = 1000; i >= 0; i--)
            {
                Console.WriteLine(i);
                Thread.Sleep(200);
            }
        }
    }
}
