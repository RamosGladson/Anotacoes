using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading;

namespace Calculadora2
{
    internal class Program
    {
        
        enum Menu 
        {
            Soma = 1, 
            Subtracao, 
            Multiplicacao, 
            Divisao, 
            Potencia, 
            Raiz, 
            Sair
        }
        static void Main(string[] args)
        {
            double num1, num2;
            
            bool escolheuFicar = true;
            while (escolheuFicar)
            {
                int i = 1;
                Linha();
                Console.WriteLine("Seja bem vindo, escolha uma das opções abaixo:");
                foreach (string item in Enum.GetNames(typeof(Menu)))
                {

                    Console.WriteLine($"{i}-{item}");
                    i++;

                }
                Linha();
                int opcao = int.Parse(Console.ReadLine());
                Console.WriteLine($"Você escolheu {(Menu)opcao}");
                Thread.Sleep(700);
                if (opcao < 8)
                {
                    switch (opcao)
                    {
                        case 1:

                            Console.WriteLine("Soma");
                            Thread.Sleep(200);
                            RecebeNumeros();
                            Soma();

                            break;

                        case 2:
                            Console.WriteLine("Subitracao");
                            Thread.Sleep(200);
                            RecebeNumeros();
                            Subitracao();
                            break;

                        case 3:

                            Console.WriteLine("Multiplicacao");
                            Thread.Sleep(200);
                            RecebeNumeros();
                            Multiplicacao();
                            break;

                        case 4:
                            Console.WriteLine("Divisao");
                            Thread.Sleep(200);
                            RecebeNumeros();
                            Divisao();
                            break;

                        case 5:

                            Console.WriteLine("Potência");
                            Thread.Sleep(200);
                            RecebeNumeros();
                            Potencia();
                            break;
                        case 6:

                            Console.WriteLine("Raiz");
                            Thread.Sleep(200);
                            RecebeNumero();
                            Raiz();
                            break;

                        case 7:
                            Console.WriteLine("Sair");
                            Console.WriteLine("Saindo");
                            Thread.Sleep(200);
                            escolheuFicar = false;

                            break;

                        default:
                            break;
                    }

                }
                else
                {
                    Console.WriteLine("Resposta inválida!");
                    
                }
                Console.WriteLine("Limpando em 3 2 1");
                Thread.Sleep(1500);
                Console.Clear();
                

            }
            void Linha()
            {
                Console.WriteLine("-----------------------------------------------");
            }
            void RecebeNumeros()
            {
                Console.WriteLine("Digite o primeiro número:");
                num1 = int.Parse(Console.ReadLine());
                Console.WriteLine("Digite o segundo número:");
                num2 = int.Parse(Console.ReadLine());
            }
            void RecebeNumero()
            {
                Console.WriteLine("Digite um número para extrair raiz:");
                num1 = int.Parse(Console.ReadLine());
            }
            void Soma()
            {
                double resultado = num1 + num2;
                Linha();
                Console.WriteLine($"A soma entre {num1} e {num2} é igual a {resultado}");
                Linha();
            }
            void Subitracao()
            {
                double resultado = num1 - num2;
                Linha();
                Console.WriteLine($"A subitração entre {num1} e {num2} é igual a {resultado}");
                Linha();
            }
            void Multiplicacao()
            {
                double resultado = num1 * num2;
                Linha();
                Console.WriteLine($"A multiplicacao de {num1} por {num2} é igual a {resultado}");
                Linha();
            }
            void Divisao()
            {
                double resultado = num1/num2;
                Linha();
                Console.WriteLine($"A divisao entre {num1} e {num2} é igual a {resultado}");
                Linha();
            }
            void Potencia()
            {                
                double resultado = Math.Pow(num1, num2);
                Linha();
                Console.WriteLine($"A potencia de {num1} por {num2} é igual a {resultado}");
                Linha();
            }
            void Raiz()
            {
                double resultado = Math.Sqrt(num1);
                Linha();
                Console.WriteLine($"A raiz quadrada de {num1} é igual a {resultado}");
                Linha();
            }           
        }   
    }
}
