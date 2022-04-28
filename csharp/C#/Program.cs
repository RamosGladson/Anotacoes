ContaBanco conta1 = new ContaBanco("João", 100);
ContaBanco conta2 = new ContaBanco("Mariana", 200);


Console.WriteLine(conta1.Saldo);


public class ContaBanco
{
 private string nome;

 public decimal Saldo
 { 
     get;
     private set;
 }

 public ContaBanco(string nome_, decimal saldo_)
 {
     if (string.IsNullOrWhiteSpace(nome_))
     {
         throw new ArgumentException($"Erro 1", nameof(nome_));
     }
     if (saldo_ < 0)
     {
         throw new Exception("Saldo inválido");
     }
     nome = nome_;
     Saldo = saldo_;
 }
 public string GetNome()
 {
     return nome;
 }
 public decimal GetSaldo()
 {
     return Saldo;
 }
 public void Deposito(decimal montante)
 {
     if (montante < 0)
     {
         Console.WriteLine("Depósito não efetuado, valor inválido");
         return;
     }
     Saldo += montante;
 }
 public void Saque(decimal montante)
 {
     if (montante > Saldo)
     {
        Console.WriteLine("Saque maior que saldo");
         return;
     }
     Saldo -= montante;
 }

}
