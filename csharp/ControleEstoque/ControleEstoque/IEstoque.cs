using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ControleEstoque
{
    internal interface IEstoque
    { 
        void Adicionar(int quant);
        void Subitrair(int quant);
    }
}
