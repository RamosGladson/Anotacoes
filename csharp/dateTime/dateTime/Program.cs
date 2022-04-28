using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace dateTime
{
    internal class Program
    {
        static void Main(string[] args)
        {
            bool desejaFicar = true;
            while (desejaFicar)
            {
                DateTime d = DateTime.Now;
                Console.WriteLine($"A hora atual é{d}");
                Console.ReadLine();
            }
        }
    }
}
