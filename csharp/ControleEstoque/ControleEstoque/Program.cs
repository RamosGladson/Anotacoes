using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Threading;
using System.IO;
using System.Runtime.Serialization.Formatters.Binary;



namespace ControleEstoque
{
    internal class Program
    {

        #region Manipulação de dados
        static void CarregaArquivo()
        {
            FileStream arquivo = new FileStream("Produtos.prd", FileMode.OpenOrCreate);
            try
            {
                BinaryFormatter formatter = new BinaryFormatter();

                produtos = (List<Produto>)formatter.Deserialize(arquivo);

                if (produtos == null)
                {
                    produtos = new List<Produto>();
                }
            }
            catch (Exception ex)
            {
                produtos = new List<Produto>();
            }
            arquivo.Close();

        }
        static void Salvar()
        {
            FileStream arquivo = new FileStream("Produtos.prd", FileMode.OpenOrCreate);
            BinaryFormatter formatter = new BinaryFormatter();

            formatter.Serialize(arquivo, produtos);

            arquivo.Close();

        }

        #endregion

        #region Funções do Programa
        static void MostraMenu()
        {
            Titulo("Sistema de cadastro de produtos");
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
            Console.WriteLine("Saindo");
            Espera();
        }



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
        static void Titulo(string titulo)
        {
            Linha();
            Console.WriteLine(titulo);
            Linha();
        }
        static void Linha()
        {
            Console.WriteLine("=======================================");

        }
        #endregion

        static List<IEstoque> produtos = new List<IEstoque>();
        enum Menu { Listar = 1, Incluir, Excluir, AdicionarEstoque, SubitrairEstoque, Sair }
        static void Main(string[] args)
        {
            CarregaArquivo();
            bool escolheuFicar = true;
            string simNao;
            while (escolheuFicar)
            {
                MostraMenu();
                Linha();
                int opcao = RecebeOpção();
                switch ((Menu)opcao)
                {

                    case Menu.Listar:
                        Listar();
                        Console.WriteLine("Pressione enter para sair");
                        Console.ReadLine();
                        break;

                    case Menu.Incluir:
                        IncluirProduto();
                        break;                    

                    case Menu.Excluir:
                        Console.WriteLine("Deseja listar os produtos?[sim/nao]");
                        simNao = Console.ReadLine();
                        Espera();
                        if (simNao == "sim")
                        {
                            Listar();
                            ExcluirProduto();
                        }
                        else
                        {
                            Titulo("Excluir produtos");
                            ExcluirProduto();
                        }

                        break;

                    case Menu.AdicionarEstoque:
                        AdicionarEstoque();
                        break;

                    case Menu.SubitrairEstoque:
                        SubitrairEstoque();
                        break;

                    case Menu.Sair:
                        escolheuFicar = false;
                        Sair();
                        break;

                    default:
                        Console.WriteLine("Opção inválida!");
                        break;

                }
                Espera();
            }
    }
}
