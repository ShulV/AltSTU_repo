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
    public partial class tabl_naim : Form
    {
        public tabl_naim()
        {
            InitializeComponent();
        }

        private void tabl_naim_Activated(object sender, EventArgs e)
        {
        if(Program.f_endgame==1) //игра закончилась, закрыть все формы
		    Close();
		else
		{
			//очистить все строки перед выводом
			while (0 != spisok.RowCount)
				spisok.Rows.RemoveAt(0);

			int kolvo_str=Program.birzh_trud.get_kolvo_krest(); //получить кол-во крестьян в списке
			for(int num=0; num<kolvo_str; num++)
			{
				spisok.Rows.Add(); //добавить новую строку в таблицу
				spisok.Rows[num].Cells[0].Value = (num+1); //записать порядковый номер крестьянина
                spisok.Rows[num].Cells[1].Value = (Program.birzh_trud.krests[num].get_name() + " " + Program.birzh_trud.krests[num].get_surname()); //внести в ячейку таблицы
				spisok.Rows[num].Cells[2].Value = (Program.birzh_trud.krests[num].get_proizv_hleb()) + "/" + (Program.birzh_trud.krests[num].get_proizv_skot());
                spisok.Rows[num].Cells[3].Value = (Program.birzh_trud.krests[num].get_eda_hleb() * Program.derevn.get_speed_life()) + "/" + (Program.birzh_trud.krests[num].get_eda_skot() * Program.derevn.get_speed_life());
                spisok.Rows[num].Cells[4].Value = (Program.birzh_trud.krests[num].get_money_trat() * Program.derevn.get_speed_life());
				spisok.Rows[num].Cells[5].Value = (Program.birzh_trud.krests[num].get_naim());
			}

		}

        }

        private void tabl_naim_Load(object sender, EventArgs e)
        {
            if(Program.derevn.get_flag_season()==1) //если зима, закрыть форму
			{
				this.Close();
			}
			if(Program.birzh_trud.krests!=null)
			{
                Program.birzh_trud.krests=null;
			}
            Program.birzh_trud.krests = new Krest[5]; //массив крестьян для найма
            Program.birzh_trud.set_kolvo_krest(5);
            for (int kk = 0; kk < 5; kk++)
            {
                Program.birzh_trud.krests[kk] = new Krest();
            }
			for(int v=0; v<5; v++)
			{
                Program.birzh_trud.krests[v].Init_rand();
			}
        }

        private void num_krest_pole_TextChanged(object sender, EventArgs e)
        {
            int kolvo_strr = Program.birzh_trud.get_kolvo_krest(); //получить кол-во крестьян в списке
            if (this.num_krest_pole.Text !="") //если поле с номером строки не пустое
            {
                double nummk = Convert.ToDouble(this.num_krest_pole.Text); //номер выбранного крестьянина
                if ((nummk > kolvo_strr) || (nummk < 1)) //если выбр. строка больше общего кол-ва строк, то отключить кнопку
                {
                    this.naim_butt.Enabled = false;
                }
                else
                {
                    this.naim_butt.Enabled = true;
                    if ((Program.derevn.get_budget_village() - Program.birzh_trud.krests[Convert.ToInt32(nummk) - 1].get_naim()) < 0)
                        this.naim_butt.Enabled = false;
                }
            }
            else
                this.naim_butt.Enabled = false;
            if (Program.derevn.get_flag_season() == 1) //если зима, закрыть форму
            {
                Close();
            }
        }

        private void naim_butt_Click(object sender, EventArgs e)
        {
             int nummk = Convert.ToInt32(this.num_krest_pole.Text); //номер выбранного крестьянина
             Program.derevn.set_budget_village(Program.derevn.get_budget_village() - Program.birzh_trud.krests[nummk - 1].get_naim());
             Program.derevn.Naim_krest(Program.birzh_trud, nummk);
             Program.birzh_trud.Delete_krest(nummk); //крестьянин перешёл из одного массива в другой. Из начального массива он удаляется
			 num_krest_pole_TextChanged(sender,e); //повторная проверка
			 tabl_naim_Activated(sender,e); //обновить таблицу
        }

        private void timer_proverk_krest_Tick(object sender, EventArgs e)
        {
            if (Program.f_endgame == 1) //игра закончилась, закрыть все формы
                Close();
            else
            {
                num_krest_pole_TextChanged(sender, e); //повторная проверка
                if (Program.derevn.get_flag_season() == 0) //таблицу обновлять только летом
                {
                    tabl_naim_Activated(sender, e); //обновить таблицу
                }
            }
        }
    }
}
