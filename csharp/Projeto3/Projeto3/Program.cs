using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Threading;

namespace Projeto3
{




    internal class Program
    {
        #region Funções do Programa

        static void CarregaArquivo()
        {

        }
        static void MostraMenu()
        {
            int i = 1;
            foreach (string menu in Enum.GetNames(typeof(Menu)))
            {
                Console.WriteLine($"{i} - {menu}");
                i++;
            }
        }

        static int RecebeOpção()
        {
            Console.WriteLine("Escolha uma das opções acima:");
            int opcao = int.Parse(Console.ReadLine());
            Espera();
            return opcao;
        }
        static void Sair()
        {
            Console.WriteLine("Sair");
            Espera();
        }

        #region Funções Cadastro de Produtos
        static void Listar()
        {
            Console.WriteLine("Listar");
            Espera();
        }

        static void IncluirProduto()
        {
            Console.WriteLine("Incluindo Produto");
            Espera();
        }

        static void AlterarProduto()
        {
            Console.WriteLine("Alterar Produto");
            Espera();
        }

        static void ExcluirProduto()
        {
            Console.WriteLine("Excluir Produto");
            Espera();
        }

        #endregion

        #region Funções controle do estoque


        static void Comprar()
        {
            Console.WriteLine("Comprar");
            Espera();
        }

        static void Vender()
        {
            Console.WriteLine("Vender");
            Espera();
        }

        

        #endregion
        #endregion

        #region Perfumaria
        static void Espera()
        {
            Thread.Sleep(2000);
            Limpa();
        }

        static void Limpa()
        {
            Console.Clear();
        }
        static void Titulo()
        {
            Console.WriteLine("Sistema de estoque");
        }
        static void Linha()
        {
            Console.WriteLine("========================");

        }
        #endregion
        enum Menu { Listar = 1, Incluir, Alterar, Excluir, Comprar, Vender, Sair }
        static void Main(string[] args)
        {
            CarregaArquivo();
            bool escolheuFicar = true;
            while (escolheuFicar)
            {
                Linha();
                Titulo();
                Linha();
                MostraMenu();
                int opcao = RecebeOpção();
                switch ((Menu)opcao)
                {

                    case Menu.Listar:
                        Listar();
                        break;
                    
                    case Menu.Incluir:
                        IncluirProduto();
                        break;
                    
                    case Menu.Alterar:
                        AlterarProduto();
                        break;

                    case Menu.Excluir:
                        ExcluirProduto();
                        break;

                    case Menu.Comprar:
                        Comprar();
                        break;

                    case Menu.Vender:
                        Vender();
                        break;

                    case Menu.Sair:
                        escolheuFicar=false;
                        Sair();
                        break;

                    default:
                        Console.WriteLine("Opção inválida!");
                        break;

                }

            }
        }

    }
}
