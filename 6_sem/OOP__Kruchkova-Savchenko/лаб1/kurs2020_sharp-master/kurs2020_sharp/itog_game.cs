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
    public partial class itog_game : Form
    {
        public itog_game()
        {
            InitializeComponent();
        }

        private void close_Click(object sender, EventArgs e)
        {
            this.Close();
        }

        private void itog_game_Load(object sender, EventArgs e)
        {
            this.your_scores.Text = Convert.ToString(Program.derevn.get_days_procv());
        }

        private void name_player_TextChanged(object sender, EventArgs e)
        {
            if(this.name_player.Text=="") //если поле с именем игрока пустое
			 {
				 this.ok_record.Enabled=false;
			 }
			 else
			 {
			    this.ok_record.Enabled=true;
			 }
        }

        private void ok_record_Click(object sender, EventArgs e)
        {
            string path= "records.txt"; //путь для записи рекордов
            using (StreamWriter stream = new StreamWriter(path, true)) //добавление записи в файл
            {
                stream.WriteLine(this.name_player.Text); //записать имя игрока в файл
                stream.WriteLine(this.your_scores.Text); //записать рекорд игрока в файл (реализовано так, чтобы рекорд нельзя было изменить, начав новую игру, не закрыв окно с финальным счётом)
                stream.WriteLine("///////"); //записать разделитель в файл (отделяет рекорды друг от друга)
                stream.Close();
            }
			 
			 this.Close();
        }
    }
}
