using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.IO;

namespace kurs2020_sharp
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void quit_butt_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void spravk_butt_Click(object sender, EventArgs e)
        {
            using (Form spr = new spravk())
            {
                spr.ShowDialog();
            }
        }

        private void new_game_butt_Click(object sender, EventArgs e)
        {
            Program.f_endgame = 0; //флаг конца игры (будет равен 1, когда игрок проиграет)
            Program.derevn.Init_new_game(); //инициализация деревни перед началом новой игры
            using (Form mg = new main_game())
            {
                mg.ShowDialog();
            }
        }

        private void records_butt_Click(object sender, EventArgs e)
        {
            using (Form rectab = new record_tabl())
            {
                rectab.ShowDialog();
            }
        }

        private void load_game_butt_Click(object sender, EventArgs e)
        {
            Program.f_endgame = 0; //флаг конца игры (будет равен 1, когда игрок проиграет)
            Program.derevn.Init_load_game(); //инициализация деревни из файла перед продолжением сохранённой игры
            using (Form mg = new main_game())
            {
                mg.ShowDialog();
            }
        }

        private void Form1_Activated(object sender, EventArgs e)
        {
            if(Program.f_endgame==1)
			 {
				Program.f_endgame=0;
                Form ig = new itog_game();
                ig.Show();
			 }
			 if(!(System.IO.File.Exists("village.txt")) || !(System.IO.File.Exists("krests.txt"))) //проверка, есть ли файлы сохранения. Если хотя бы одного нет, то кнопка загрузки игры отключается
			 {
				 this.load_game_butt.Enabled=false;
			 }
			 else
			 {
				 this.load_game_butt.Enabled=true;
			 }
        }
    }
}
