using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;

namespace manipulacao
{
    internal class Program
    {
        static void Main(string[] args)
        {
            StreamWriter arquivo = File.AppendText("teste.txt");
            arquivo.WriteLine("olá mundo");
            arquivo.Close();
            Console.WriteLine("Já foi escrito");
            Console.ReadLine();

        }
    }
}
