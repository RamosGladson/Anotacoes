using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;
using System.Runtime.Serialization.Formatters.Binary;

namespace arquivobinario
{
    internal class Program
    {
        [System.Serializable]
        struct Produto
        {
            public string nome;
            public float valor;
        }
        static void Main(string[] args)
        {


            List<string> cursos = new List<string>();
            
            FileStream fs = new FileStream("Meu_arquivo.txt",FileMode.OpenOrCreate);
            BinaryFormatter formatter = new BinaryFormatter();
            cursos.Add("Java");
            cursos.Add("C#");
            cursos.Add("Costura");
            
            Produto banana = new Produto();
            banana.nome = "b1";
            banana.valor = 0.56f;
            /*
            formatter.Serialize(fs, cursos);
            formatter.Serialize(fs, banana);
            */

            

            List<string> lista = (List<string>)formatter.Deserialize(fs);
            Produto prod = (Produto)formatter.Deserialize(fs);
            
            foreach (string s in lista)
            {
                Console.WriteLine(s);
            }

            Console.WriteLine(prod.nome);
            fs.Close();
            Console.ReadLine();
        }
        
    }
}














