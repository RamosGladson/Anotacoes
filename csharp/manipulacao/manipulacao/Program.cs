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
            //Console.WriteLine("Digite o nome do arquivo a ser lido");
//            string nome = Console.ReadLine();

            StreamReader leitor = new StreamReader("teste.txt");
            List<string> list = new List<string>();
            string linha = "";

            while (linha!=null)
            {
                linha = leitor.ReadLine();
                if (linha != null)
                {                    
                    list.Add(linha);
                }
                
            }
            leitor.Close();

            foreach (string line in list)
            {
                Console.WriteLine(line);
            }

            Console.WriteLine("fim");            
            Console.ReadLine();
            

            
        }
    }
}
