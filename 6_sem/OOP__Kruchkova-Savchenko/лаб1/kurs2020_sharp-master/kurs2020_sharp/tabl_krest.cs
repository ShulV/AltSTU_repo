using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace kurs2020_sharp
{
    public partial class tabl_krest : Form
    {
        public tabl_krest()
        {
            InitializeComponent();
        }

        private void trud_butt_Click(object sender, EventArgs e)
        {
            using (Form tabnaim = new tabl_naim())
            {
                tabnaim.ShowDialog();
            }
        }

        private void tabl_krest_Activated(object sender, EventArgs e)
        {
            if(Program.f_endgame==1) //игра закончилась, закрыть все формы
				 this.Close();
		    else
		    {
			    //очистить все строки перед выводом
			    while (0 != spisok.RowCount)
				    spisok.Rows.RemoveAt(0);

			    int kolvo_str=Program.derevn.get_kolvo_krest(); //получить кол-во крестьян в списке
			    for(int num=0; num<kolvo_str; num++)
			    {
				    spisok.Rows.Add(); //добавить новую строку в таблицу
				    spisok.Rows[num].Cells[0].Value = (num+1); //записать порядковый номер крестьянина
				    spisok.Rows[num].Cells[1].Value = (Program.derevn.krests[num].get_name() + " " + Program.derevn.krests[num].get_surname()); //внести в ячейку таблицы
				    spisok.Rows[num].Cells[2].Value = (Program.derevn.krests[num].get_proizv_hleb()) + "/" + (Program.derevn.krests[num].get_proizv_skot());
				    spisok.Rows[num].Cells[3].Value = (Program.derevn.krests[num].get_eda_hleb()*Program.derevn.get_speed_life()) + "/" + (Program.derevn.krests[num].get_eda_skot()*Program.derevn.get_speed_life());
				    spisok.Rows[num].Cells[4].Value = (Program.derevn.krests[num].get_money_trat()*Program.derevn.get_speed_life());
			    }
		    }

        }

        private void num_krest_pole_TextChanged(object sender, EventArgs e)
        {
            int kolvo_strr=Program.derevn.get_kolvo_krest(); //получить кол-во крестьян в списке
			if (this.num_krest_pole.Text!="") //если поле с номером строки не пустое
			{
				if((Convert.ToDouble(this.num_krest_pole.Text) > kolvo_strr) || (Convert.ToDouble(this.num_krest_pole.Text)<1)) //если выбр. строка больше общего кол-ва строк, то отключить кнопку
				{
					this.izgnat_butt.Enabled = false;
				}
				else
					this.izgnat_butt.Enabled = true;
			}
			else
				this.izgnat_butt.Enabled = false;
			if(Program.derevn.get_flag_season()==1) //если зима, кнопка Изгнать недоступна в любом случае
			{
				this.label1.Enabled = false;
				this.num_krest_pole.Enabled = false;
				this.izgnat_butt.Enabled = false;
				this.trud_butt.Enabled = false;
			}
			if(Program.derevn.get_flag_season()==0) //если лето, включить кнопку открытия Биржи труда
			{
				this.label1.Enabled = true;
				this.num_krest_pole.Enabled = true;
				this.trud_butt.Enabled = true;
			}
        }

        private void izgnat_butt_Click(object sender, EventArgs e)
        {
             Program.derevn.Delete_krest(Convert.ToInt32(this.num_krest_pole.Text)); //удалить крестьянина
             num_krest_pole_TextChanged(sender, e); //повторная проверка
			 tabl_krest_Activated(sender,e); //обновить таблицу
        }

        private void tabl_krest_Load(object sender, EventArgs e)
        {
            num_krest_pole_TextChanged(sender, e); //проверка
        }

        private void timer_proverk_krest_Tick(object sender, EventArgs e)
        {
            if (Program.f_endgame == 1) //игра закончилась, закрыть все формы
                this.Close();
            else
            {
                num_krest_pole_TextChanged(sender, e); //повторная проверка
                tabl_krest_Activated(sender, e); //обновить таблицу
            }
        }


    }
}
