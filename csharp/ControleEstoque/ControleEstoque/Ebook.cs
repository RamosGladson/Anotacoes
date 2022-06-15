using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ControleEstoque
{
    [System.Serializable]
    internal class Ebook : Produto, IEstoque
    {
        private string Autor { get; set; }
        public int Vendas { get; set; }

        public Ebook(string nome, int preco, string autor, int vendas) : base(nome, preco)
        {
            Autor = autor;
            Vendas = 0;
        }
        public override string ToString()
        {
            return $"Nome: {Nome}\nPreco: {Preco}\nAutor: {Autor}\nQuantidade Vendas: {Vendas}";
        }

        public void Adicionar(int quant)
        {
            Vendas+=quant;
        }

        public void Subitrair(int quant)
        {
            Vendas-=quant;
        }
    }
}
