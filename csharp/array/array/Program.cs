using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace array
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int[,,] myarray = new int[2, 2, 3]
            {
                {
                    {0, 1, 2},
                    {3, 4, 5}
                }
                ,

                {
                    {6, 7, 8},
                    {9, 10, 11}
                }
            };

            foreach(int i in myarray)
            {
                Console.WriteLine(i);
            }
     
            Console.Read();

        }
    }
}
