using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Calculadora
{
    internal class Program
    {
        enum Menu { Soma, Subitracao, Multiplicacao, Divisao, Potencia, Raiz, Sair }
        static void Main(string[] args)
        {
            int i = 1;

            Console.WriteLine("Digite seu nome:");
            string nome = Console.ReadLine();
            boasvindas(nome);
            string operacao = opcoes();
            Console.WriteLine($"Você digitou {operacao}");
            Console.WriteLine("Digite o primeiro número ");
            int primeiro = int.Parse(Console.ReadLine());
            Console.WriteLine("Digite o segundo número: ");
            int segundo = int.Parse(Console.ReadLine());
            
            string opcoes()

            {
                Console.WriteLine("Digite uma das opções abaixo:");
                foreach(string item in Enum.GetNames(typeof(Menu)))
                {
                    Console.WriteLine($"{i} - {item}");
                    i++;
                }                       
                string opcao = Console.ReadLine();
                return opcao;
            }

            void boasvindas(string name)
            {
                linha();
                Console.WriteLine($"Seja bem vindo a Calculadora {name}!!");
                linha();

            }
            
            void linha()
            {
                Console.WriteLine("======================================");
            }


        }
    }
}
