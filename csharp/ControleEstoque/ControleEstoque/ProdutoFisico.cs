using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ControleEstoque
{
    [System.Serializable]
    class ProdutoFisico : Produto, IEstoque
    {
        private float Frete { get; set; }
        public int Estoque { get; set; }

        public ProdutoFisico(string nome, int preco, float frete) : base(nome, preco)
        {
            Frete = frete;
            Estoque = 0;
        }

        public override string ToString()
        {
            return $"Nome: {Nome}\nPreco: {Preco}\nFrete: {Frete}\nEstoque: {Estoque}";

        }

        public void Adicionar(int quant)
        {
            Estoque+=quant;
        }

        public void Subitrair(int quant)
        {
            Estoque-=quant;
        }
    }
}
