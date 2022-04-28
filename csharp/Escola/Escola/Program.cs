using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Escola
{
    internal class Program
    {
        static void Main(string[] args)
        {
            String[] alunos = new String[10];
            
            for (int i = 0; i < 10; i++)
            {
                Console.WriteLine($"Digite o nome do {i+1}º aluno:" );
                alunos[i] = Console.ReadLine();
            }

            foreach (string i in alunos)
            {
                Boasvindas(i);
                
            }
                
            Console.ReadLine();



            void Boasvindas(string aluno)   
            {
                Console.WriteLine($"Bem vindo(a){aluno}");
            }

        }
    }
}
