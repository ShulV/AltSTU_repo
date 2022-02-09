using System;
using System.Collections.Generic;
using System.Linq;
using System.Windows.Forms;

namespace kurs2020_sharp
{
    static class Program
    {
        /// <summary>
        /// Главная точка входа для приложения.
        /// </summary>
        [STAThread]
        static void Main()
        {
            Application.EnableVisualStyles();
            Application.SetCompatibleTextRenderingDefault(false);
            Application.Run(new Form1());
        }

        //Обявления переменных
        public static Village derevn = new Village(); //объект, в котором хранится вся информация о деревне (глобальн.)
        public static Village birzh_trud = new Village(); //объект, в котором хранятся крестьяне для найма (глобальн.)
        public static int f_endgame = 0; //флаг о том, что игра окончена (игрок проиграл) (глобальн.)

        public static int r1 = (int)(DateTime.Now.Subtract(new DateTime(1970, 1, 1)).TotalSeconds); //ключ рандома, полученный по текущему времени
        public static Random randk = new Random(r1); //рандом
    }
}
