using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Threading;
using System.IO;
using System.Runtime.Serialization.Formatters.Binary;

namespace menu
{
    internal class Program
    {
        #region Variaveis e tipos
        [System.Serializable]
        struct Cliente
        {
            public string nome;
            public string email;
            public string cpf;

            public override string ToString()
            {
                return $"Nome:{nome}\nemail:{email}\ncpf:{cpf}";
            }
        }

        static List<Cliente> clientes = new List<Cliente>();

        enum Menu { Listagem = 1, Adicionar, Remover, Sair }

        #endregion


        #region funções

        #region perfumaria
        static void Linha()
        {
            Console.WriteLine("==========================");
        }
        static void BoasVindas()
        {
            Console.WriteLine("Bem Vindo!!!");
        }
        static void ContagemRegressiva(int contador)
        {
            for (int i = contador; i > 0; i--)
            {
                Console.WriteLine(i);
                Thread.Sleep(1000);
            }
        }
        static void Bye()
        {
            Linha();
            Console.WriteLine("Finalizando em :");
            Thread.Sleep(1000);
            ContagemRegressiva(3);
        }

        #endregion

        #region manipulação de arquivo
        static void Salvar()
        {
            FileStream arquivo = new FileStream("Clientes.meu", FileMode.OpenOrCreate);
            BinaryFormatter gravador = new BinaryFormatter();

            gravador.Serialize(arquivo, clientes);

            arquivo.Close();
        }

        static void Carregar()
        {
            FileStream arquivo = new FileStream("Clientes.meu", FileMode.OpenOrCreate);
            try
            {

                BinaryFormatter gravador = new BinaryFormatter();

                clientes = (List<Cliente>)gravador.Deserialize(arquivo);



                if (clientes == null)
                {
                    clientes = new List<Cliente>();
                }
            }
            catch (Exception e)
            {
                clientes = new List<Cliente>();
            }
            arquivo.Close();

        }

        #endregion
        #region funções do programa
        static void Remover()
        {
            Console.WriteLine("Entre com o cpf do cliente a ser removido");
            string cpf = Console.ReadLine();
            Cliente n = clientes.Where(x => x.cpf == cpf).FirstOrDefault();
            clientes.Remove(n);
            Salvar();

        }

        static void Adcionar()
        {
            Cliente cliente = new Cliente();
            Console.WriteLine("Cadastro de cliente");
            Console.Write("Nome do cliente: ");
            cliente.nome = Console.ReadLine();
            Console.Write("Endereço de email: ");
            cliente.email = Console.ReadLine();
            Console.Write("CPF:");
            cliente.cpf = Console.ReadLine();
            Console.WriteLine("Cadastro concluido!");
            Thread.Sleep(500);
            clientes.Add(cliente);
            Console.Clear();
            Salvar();

        }
       
        static void Listagem()
        {
            if (clientes.Count > 0)
            {
                foreach (Cliente item in clientes)
                {
                    Linha();
                    Console.WriteLine(item);
                }
            }
            else
            {
                Console.WriteLine("Não há clientes cadastrados");
            }

            Console.WriteLine("Limpando a tela em:");
            ContagemRegressiva(3);
            Console.Clear();
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
        static int RecebeOpcao()
        {
            Console.WriteLine("Digite sua opção");
            int opcao = int.Parse(Console.ReadLine());
            return opcao;
        }
        #endregion

        #endregion

        static void Main(string[] args)
        {
            Carregar();
            bool escolheuFicar = true;
            while (escolheuFicar)
            {
                Linha();
                BoasVindas();
                Linha();
                MostraMenu();
                int opcao = RecebeOpcao();
                Console.WriteLine($"Voce digitou {(Menu)opcao}");
                Thread.Sleep(1000);
                Console.Clear();

                if (opcao > 0 && opcao < 5)
                {
                    switch ((Menu)opcao)
                    {
                        case Menu.Listagem:
                            Console.WriteLine("Cadastro de Clientes:");
                            Listagem();
                            break;

                        case Menu.Adicionar:
                            Adcionar();
                            break;

                        case Menu.Remover:
                            Remover();
                            break;

                        case Menu.Sair:
                            escolheuFicar = false;
                            Bye();
                            break;

                        default:
                            break;
                    }

                }
                else
                {
                    Console.WriteLine("Você digitou uma opção inválida, digite novamente");
                    Thread.Sleep(2000);
                    Console.Clear();

                }
            }



        }



    }
}
