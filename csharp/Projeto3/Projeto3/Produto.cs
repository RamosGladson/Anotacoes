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
        protected string _nome;
        protected float _preco;
        protected float _peso;
        protected float _volume;

        public Produto(string nome, float preco, float peso, float volume)
        {
            _nome = nome;
            _preco = preco;
            _peso = peso;
            _volume = volume;

        }
        public override string ToString()
        {
            return $"Nome: {_nome}\nPreço: R$ {_preco}\nPeso: {_peso} KG\nVolume: {_volume} metros cubicos";
        }
    }
}
