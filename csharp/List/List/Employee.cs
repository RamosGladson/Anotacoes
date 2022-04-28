using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace List
{
    internal class Employee
    {
        public int Id { get; set; }
        private string Name { get; set; }
        private double Salary { get; set; }

        public Employee(int id, string name, double salary)
        {
            Id = id;
            Name = name;
            Salary = salary;
        }

        public void IncreaseSalary(double aumento)
        {
            Salary = Salary*(1 + aumento/100);
        }
        

        public override string ToString()
        {
            return $"O empregado {Id} de nome {Name} tem salário {Salary}";
        }
    }

    

    
}
