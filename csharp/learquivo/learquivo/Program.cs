using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;

namespace learquivo
{
    internal class Program
    {
        static void Main(string[] args)
        {
            StreamReader leitor = new StreamReader("Ola mundo.txt");

            List<string> linhas = new List<string>();

            string linha = "";
            while (linha != null)
            {
                linha=leitor.ReadLine();
                if (linha != null)
                {
                    linhas.Add(linha);
                }
                else
                {
                    leitor.Close();
                }
                               
            }
            foreach (string line in linhas)
            {
                Console.WriteLine(line);
            }
            Console.WriteLine("Fim");

            Console.ReadLine();
        }
    }
}
