using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ControleEstoque
{
    [System.Serializable]
    internal class Curso : Produto, IEstoque
    {
        private string Professor { get; set; }
        public int Vagas { get; set; }
        public Curso(string nome, int preco, string professor) : base(nome, preco)
        {
            Professor = professor;
            Vagas = 0;
        }

        public override string ToString()
        {
            return $"Nome: {Nome}\nPreco: {Preco}\nProfessor: {Professor}\nVagas disponíveis: {Vagas}";
        }

        public void Adicionar(int quant)
        {
            Vagas += quant;
        }

        public void Subitrair(int quant)
        {
            Vagas -= quant;
        }

    }
}
