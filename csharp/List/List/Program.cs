using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Threading;

namespace List
{
    internal class Program
    {
        static void Main(string[] args)
        {
            List<Employee> empregados = new List<Employee>();

            void Linha()
            {
                Console.WriteLine("==============================================");
            }

            void ListaEmpregados()
            {
                foreach (Employee empregado in empregados)
                {
                    Console.WriteLine(empregado);
                }
            }

            Console.WriteLine("Quantos empregados deseja cadastrar?");
            int quant = int.Parse(Console.ReadLine());            
            for (int i = 0; i < quant; i++)
            {
                Console.WriteLine($"Digite o id do {i + 1}º funcionario ");
                int id = int.Parse(Console.ReadLine());
                Console.WriteLine($"Digite nome do {i + 1}º funcionario ");
                string nome = Console.ReadLine();
                Console.WriteLine($"Digite o salario do {i + 1}º funcionario");
                double salario = double.Parse(Console.ReadLine());
                empregados.Add(new Employee(id, nome, salario));

            }
            Linha();
            ListaEmpregados();
            Linha();
            Console.WriteLine("Informe o id do funcionario a ter elevação do salario:");
            int id_usuario = int.Parse(Console.ReadLine());
            Employee emp = empregados.Find(x => x.Id == id_usuario);
            if (emp != null)
            {
                Console.WriteLine("Qual percentual a ser elevado?");
                double percentagem = double.Parse(Console.ReadLine());
                emp.IncreaseSalary(percentagem);
            }
            else
            {
                Console.WriteLine("Funcionario inexistente");
            }
            
            //Thread.Sleep(1000);
            ListaEmpregados();
            Console.ReadLine();



        }
    }
}
