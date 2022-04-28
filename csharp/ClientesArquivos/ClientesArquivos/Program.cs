using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading;


namespace ClientesArquivos
{
    internal class Program
    {
        [System.Serializable]
        struct Cliente
        {
            public string nome;
            public string email;
            public string cpf;
        }

        
        enum Menu { Listar = 1, Adicionar, Remover, Sair }
        static void Main(string[] args)
        {
            List<Cliente> clientes = new List<Cliente>();
            bool escolheuFicar = true;
            while (escolheuFicar)
            {
                Linha();
                Titulo("              Menu");
                Linha();
                ExibeMenu();
                Linha();
                Menu escolha = Opcao();

                switch (escolha)
                {
                    case Menu.Listar:
                        ExibeLista();
                        break;
                    case Menu.Adicionar:
                        Adicionar();
                        break;
                    case Menu.Remover:
                        Remover();
                        break;
                    case Menu.Sair:
                        Sair();
                        escolheuFicar = false;
                        break;
                    default:
                        break;
                }
                
                Thread.Sleep(1000);
                Console.Clear();

            }

            void Sair()
            {
                Console.Write("Saindo em");
                Thread.Sleep(1000);
                Console.Write(" 3 ");
                Thread.Sleep(1000);
                Console.Write(" 2 ");
                Thread.Sleep(1000);
                Console.Write(" 1 ");
                Thread.Sleep(1000);
            }

            void ExibeLista()
            {
                Console.WriteLine("Segue a lista:");
                foreach (var item in clientes)
                {
                    Console.WriteLine(item);
                }
            }

            void Adicionar()
            {
                Cliente cliente = new Cliente();
                Titulo("Adicionar");
                Console.WriteLine("Digite nome:");
                cliente.nome = Console.ReadLine();
                Console.WriteLine("Digite email:");
                cliente.email = Console.ReadLine();
                Console.WriteLine("Digite cpf:");
                cliente.cpf = Console.ReadLine();
                clientes.Add(cliente);
                foreach (Cliente item in cliente)
                {
                    Console.WriteLine(item);
                }
                Console.WriteLine($"{cliente.nome} adicionado com sucesso. Retornando ao menu.");
                Thread.Sleep(1000);
                
            }

            void Remover()
            {
                Console.WriteLine("Remover");
            }

            void ExibeMenu()
            {
                int i = 1;

                foreach (Menu menu in Enum.GetValues(typeof(Menu)))
                {

                    Console.WriteLine($"{i}-{menu}");
                    i++;
                }

            }

            void Linha()
            {
                Console.WriteLine("-----------------------------------");
            }

            void Titulo(string titulo)
            {
                Console.WriteLine(titulo);
            }

            Menu Opcao()
            {
                Console.WriteLine("Escolha uma da opções acima:");
                
                int item = int.Parse(Console.ReadLine());
                Menu opcao = (Menu)item;
                return opcao;
            }

            
        }
    }
}
