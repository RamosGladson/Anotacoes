using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ControleEstoque
{
    [System.Serializable]
    abstract class Produto
    {
        protected string Nome { get; set; }
        protected int Preco { get; set; }

        
        protected Produto(string nome, int preco)
        {
            Nome = nome;
            Preco = preco;
        }
    }
}
