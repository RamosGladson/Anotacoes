using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Threading;
using System.IO;
using System.Runtime.Serialization.Formatters.Binary;


namespace Projeto3
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
            Console.WriteLine("Sair");
            Espera();
        }

        #region Funções Cadastro de Produtos
        
        static void Listar()
        {
            Titulo("Lista de Produtos");
            foreach (Produto item in produtos)
            {
                Console.WriteLine(item);
                Linha();
            }
            
            
        }

        static void IncluirProduto()
        {
            bool maisProdutos = true;
            while (maisProdutos)
            {
                Console.WriteLine("Incluindo Produto");
                Espera();
                Console.Write("Digite o nome do produto: ");
                string nome = Console.ReadLine();
                Console.Write("Digite o preço do produto: ");
                float preco = float.Parse(Console.ReadLine());
                Console.Write("Digite o peso do produto: ");
                float peso = float.Parse(Console.ReadLine());
                Console.Write("Digite o volume do produto: ");
                float volume = float.Parse(Console.ReadLine());
                Produto produto = new Produto(nome, preco, peso, volume);
                produtos.Add(produto);
                Salvar();
                Console.WriteLine("Deseja incluir mais produtos?[sim/nao]");
                string simNao = Console.ReadLine();
                if (simNao == "sim")
                {
                }
                else
                {
                    maisProdutos=false;
                }
                Espera();
            }
            Salvar();
            Console.WriteLine("Produtos incluidos com sucesso");
            
        }

        static void AlterarProduto()
        {
            Console.WriteLine("Alterar Produto");

            Espera();
        }

        static void ExcluirProduto()
        {
            Titulo("Excluir Produto");            
            
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
        static void Titulo(string titulo)
        {
            Linha();
            Console.WriteLine(titulo);
            Linha();
        }
        static void Linha()
        {
            Console.WriteLine("===============================");

        }
        #endregion
        
        #region variaveis globais
        static List<Produto> produtos = new List<Produto>();
        enum Menu { Listar = 1, Incluir, Alterar, Excluir, Comprar, Vender, Sair }
        #endregion

        static void Main(string[] args)
        {
            CarregaArquivo();
            bool escolheuFicar = true;
            while (escolheuFicar)
            {   
                MostraMenu();
                Linha();
                int opcao = RecebeOpção();
                switch ((Menu)opcao)
                {

                    case Menu.Listar:
                        Listar();
                        Console.WriteLine("Pressione enter tecla para sair");
                        Console.ReadLine();
                        Espera();
                        break;
                    
                    case Menu.Incluir:
                        IncluirProduto();
                        break;
                    
                    case Menu.Alterar:
                        AlterarProduto();
                        break;

                    case Menu.Excluir:
                        Console.WriteLine("Deseja listar os produtos?");
                        string simNao=Console.ReadLine();
                        if (simNao == "sim")
                        {
                            Listar();
                        }
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
