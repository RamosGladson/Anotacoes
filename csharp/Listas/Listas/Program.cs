using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading;

namespace Listas
{
    internal class Program
    {
        enum Menu { Adicionar = 1, Listar, Remover, RemoverPeloNome, Sair }
        static void Main(string[] args)
        {
            List<string> list = new List<string>();
            iniciar();
            void iniciar()
            {
                
                bool escolheuFicar = true;
                while (escolheuFicar)
                {
                    linha();
                    Console.WriteLine("Escolha uma das opções abaixo:");
                    int i = 0;
                    linha();
                    foreach (string item in Enum.GetNames(typeof(Menu)))
                    {
                        i++;
                        Console.WriteLine($"{i} - {item}");
                    }
                    linha();
                    int opcao = int.Parse(Console.ReadLine());
                    Console.WriteLine($"Voce escolheu {(Menu)opcao}");
                    Thread.Sleep(2000);
                    switch (opcao)
                    {
                        case 1:
                            Console.Clear();
                            adicionarFilme();
                            break;
                        case 2:
                            
                            Console.Clear();
                            mostrarFilme();
                            limparTela();
                            break;
                        case 3:
                            Console.Clear();
                            removerFilme();
                            break;
                        case 4:
                            Console.Clear();
                            removerFilmeNome();
                            break;
                        case 5:
                            Console.Clear();
                            escolheuFicar = sair();
                            break;
                        default:
                            break;
                    }
                }

            }           
            void adicionarFilme()
            {
                bool escolheuFicar = true;
                while (escolheuFicar)
                {
                    Console.WriteLine("Digite o nome de um filme");
                    list.Add(Console.ReadLine());
                    Console.WriteLine("Adicionar mais um? [sim/nao]");
                    string adicionar = Console.ReadLine();
                    if (adicionar != "sim")
                    {
                        Console.Clear();
                        escolheuFicar = false;
                    }
                }
            }
            void mostrarFilme()
            {
                int i = 0;
                foreach (string item in list)
                {
                    i++;
                    Console.WriteLine($"{i} - {item}");
                }
                Thread.Sleep(2000);
               
               
                
            }     
            void removerFilme()
            {
                Console.WriteLine("Qual filme deseja remover?");
                mostrarFilme();
                int escolha  = int.Parse(Console.ReadLine());
                list.RemoveAt(escolha);
            }
            void removerFilmeNome()
            {                
                mostrarFilme();
                Console.WriteLine("Digite o nome a ser deletado:");
                string nome = Console.ReadLine();
                list.RemoveAll(item => item == nome);
            }
            void linha()
            {
                Console.WriteLine("==============================");
            }
            void limparTela()
            {
                Console.WriteLine("Deseja limpar a tela? [sim/nao]");
                string limpar = "";
                limpar = Console.ReadLine();
                if (limpar == "sim")
                {
                    Console.Clear();
                }
            }
            bool sair()
            {
                Console.WriteLine("Saindo...");
                bool escolheuFicar = false;
                Thread.Sleep(1000);
                return escolheuFicar;
            }
                        
        }
    }
}
