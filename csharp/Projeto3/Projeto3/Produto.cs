using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;


namespace Projeto3
{
    [System.Serializable]
    internal class Produto
    {
        public string Nome { get; set; }
        public float Preco { get; protected set; }
        public float Peso { get; protected set; }
        public float Volume { get; protected set; }

        public Produto(string nome, float preco, float peso, float volume)
        {
            Nome = nome;
            Preco = preco;
            Peso = peso;
            Volume = volume;

        }
        public void SetNome()
        {
            Nome = Console.ReadLine();
        }
        public override string ToString()
        {
            return $"Nome: {Nome}\nPreço: R$ {Preco}\nPeso: {Peso} KG\nVolume: {Volume} metros cubicos";
        }
    }
}
