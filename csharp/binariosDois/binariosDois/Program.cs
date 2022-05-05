using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;
using System.Runtime.Serialization.Formatters.Binary;

namespace binariosDois
{
    internal class Program
    {
        static void Main(string[] args)
        {
            FileStream arquivo = new FileStream("binario.bin", FileMode.OpenOrCreate);
            BinaryFormatter formatter = new BinaryFormatter();

            /*
            formatter.Serialize(arquivo, 120);
            formatter.Serialize(arquivo, "hoje é um bom dia");
            */
            int n = (int)formatter.Deserialize(arquivo);
            string ola = (string)formatter.Deserialize(arquivo);
            Console.WriteLine(ola);
            Console.WriteLine(n);



            arquivo.Close();

        }
    }
}
