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
    public partial class main_game : Form
    {
        public main_game()
        {
            InitializeComponent();
        }

        private void go_to_main_menu_butt_Click(object sender, EventArgs e)
        {
            this.Close();
        }

        private void spravk_lent_butt_Click(object sender, EventArgs e)
        {
            using (Form sprv = new spravk())
            {
                sprv.ShowDialog();
            }
        }

        private void spisok_krest_butt_Click(object sender, EventArgs e)
        {
            using (Form tablk = new tabl_krest())
            {
                tablk.ShowDialog();
            }
        }

        private void birzha_butt_Click(object sender, EventArgs e)
        {
            using (Form sellt = new sell_tovar())
            {
                sellt.ShowDialog();
            }
        }

        private void main_game_Load(object sender, EventArgs e)
        {
             this.kolvo_krest_text.Text = "Крестьяне: " + (Program.derevn.get_kolvo_krest())+ " чел.";;
			 this.skorost_zhiz_text.Text = "Скорость жизни: " + (Program.derevn.get_speed_life());
			 this.den_procv_text.Text = "Дни Процветания: " + (Program.derevn.get_days_procv());
			 this.budget_text.Text = "Бюджет: " + (Program.derevn.get_budget_village()) + " руб.";
			 this.hleb_text.Text = "Хлеб: " + (Program.derevn.get_kolvo_hleb()) + " ед.";
			 this.skot_text.Text = "Домашний скот: " + (Program.derevn.get_kolvo_skot()) + " ед.";
			 if(Program.derevn.get_flag_season()==0)
				this.time_helper.Text = "До конца Лета осталось " + (40 -(Program.derevn.get_hours_procv() - Program.derevn.get_hours_from_begin_of_season())) + " Часов Процветания.";
			 if(Program.derevn.get_flag_season()==1)
			 {
				this.time_helper.Text = "До конца Зимы осталось " + (20 -(Program.derevn.get_hours_procv() - Program.derevn.get_hours_from_begin_of_season())) + " Часов Процветания.";
				this.BackgroundImage = Image.FromFile("zima.jpg"); //изменить фон на зимний
			 }
        }

        private void main_timer_Tick(object sender, EventArgs e)
        {
			 this.save_complete.Visible = false;
			 if(Program.f_endgame==1) //игра закончилась, закрыть все формы
				 this.Close();
			 Program.derevn.set_hours_procv(Program.derevn.get_hours_procv()+1); //кол-во часов процветания увеличилось на 1
			 if((Program.derevn.get_hours_procv()%10)==0) //если прошло 10 часов процветания
			 {
				 Program.derevn.set_days_procv(Program.derevn.get_days_procv()+1);
			 }
			 if(Program.derevn.get_kolvo_krest()==0) //если нет крестьян
			 {
				 Program.derevn.set_otschet_hours_net_krest(Program.derevn.get_otschet_hours_net_krest()+1);
			 }
			 if(Program.derevn.get_otschet_hours_net_krest()==2) //если закончилось время отсчёта без крестьян
			 {
				 Program.f_endgame=1;
				 this.Close();
			 }
			 if(Program.derevn.get_kolvo_krest()!=0) //если хотя бы один крестьянин нашёлся
			 {
				 Program.derevn.set_otschet_hours_net_krest(0);
			 }
			 if(Program.derevn.get_flag_season()==0 && Program.derevn.get_budget_village()!=0) //если лето и бюджет не нулевой
			 {
				 int kolv_k=Program.derevn.get_kolvo_krest();
				 for(int ko=0; ko<kolv_k; ko++)
				 {
					 if((Program.derevn.get_budget_village()-(Program.derevn.krests[ko].get_money_trat()*Program.derevn.get_speed_life()))>=0)
					 {
						 Program.derevn.set_kolvo_hleb(Program.derevn.get_kolvo_hleb()+Program.derevn.krests[ko].get_proizv_hleb());
						 Program.derevn.set_kolvo_skot(Program.derevn.get_kolvo_skot()+Program.derevn.krests[ko].get_proizv_skot());
						 Program.derevn.set_budget_village(Program.derevn.get_budget_village()-(Program.derevn.krests[ko].get_money_trat()*Program.derevn.get_speed_life()));
					 }
					 else
						 break;
				 }
			 }
			 if(Program.derevn.get_flag_season()==1) //если зима
			 {
				 int kolv_k=Program.derevn.get_kolvo_krest();
				 for(int ko=0; ko<kolv_k; ko++)
				 {
					 Program.derevn.set_kolvo_hleb(Program.derevn.get_kolvo_hleb()-(Program.derevn.krests[ko].get_eda_hleb()*Program.derevn.get_speed_life()));
					 Program.derevn.set_kolvo_skot(Program.derevn.get_kolvo_skot()-(Program.derevn.krests[ko].get_eda_skot()*Program.derevn.get_speed_life()));
					 if(Program.derevn.get_kolvo_hleb()>=0 && Program.derevn.get_kolvo_skot()>=0)
						 Program.derevn.krests[ko].set_otschet_hours_net_edi(0);
					 if(Program.derevn.get_kolvo_hleb()<0 || Program.derevn.get_kolvo_skot()<0)
					 {
						if(Program.derevn.get_kolvo_hleb()<0)
						{
							 Program.derevn.set_kolvo_hleb(0);
						}
						if(Program.derevn.get_kolvo_skot()<0)
						{
							 Program.derevn.set_kolvo_skot(0);
						}
						Program.derevn.krests[ko].set_otschet_hours_net_edi(Program.derevn.krests[ko].get_otschet_hours_net_edi()+1);
						if(Program.derevn.krests[ko].get_otschet_hours_net_edi()>=5)
						{
							string str_name= Program.derevn.krests[ko].get_name() + " " + Program.derevn.krests[ko].get_surname(); //для вывода имени и фамилии
							this.event_helper.Text = "Последнее событие: " + (DateTime.Now.Hour)+ ":" + (DateTime.Now.Minute)+ ":" + (DateTime.Now.Second) + " " + "Крестьянин " + str_name + " ушёл из деревни из-за недостатка пищи.";
							
							Program.derevn.Delete_krest(ko+1); //удалить крестьянина (методу передаётся нумерация от единицы, а цикл нумеруется от нуля)
							kolv_k=kolv_k-1; //крестьян стало на 1 меньше

							if(kolv_k==ko)
								break;
			 
						}
					 }
				 }
			 }

			 if(Program.derevn.get_flag_season()==0 && (Program.derevn.get_hours_procv() - Program.derevn.get_hours_from_begin_of_season())==40) //если сейчас лето и прошло 40 часов П. от начала лета (4 дня П. или 2 минуты)
			 {
				 Program.derevn.set_flag_season(1); //теперь флаг соответствует зиме
				 this.BackgroundImage = Image.FromFile("zima.jpg"); //изменить фон на зимний
				 Program.derevn.set_hours_from_begin_of_season(Program.derevn.get_hours_procv());
			 }

			 if(Program.derevn.get_flag_season()==1 && (Program.derevn.get_hours_procv() - Program.derevn.get_hours_from_begin_of_season())==20) //если сейчас зима и прошло 20 часов П. от начала зимы (2 дня П. или 1 минута)
			 {
				 Program.derevn.set_flag_season(0); //теперь флаг соответствует лету
				 this.BackgroundImage = Image.FromFile("leto.jpg"); //изменить фон на летний
				 Program.derevn.set_hours_from_begin_of_season(Program.derevn.get_hours_procv());
				 Program.derevn.set_speed_life( Program.derevn.get_speed_life()+1); //множитель Скорость жизни увеличился на 1
				 int f_izmen_price; //флаг изменения цены на товар (0, если уменьшить; 1, если увеличить)
				 double proc_izm; //процент от начального значения цены, на которое она изменится
				 //ДЛЯ ЦЕНЫ НА ХЛЕБ
				 f_izmen_price = Program.randk.Next(0, 2); //случайное число в интервале от 0 до 1 включительно
				 proc_izm = Program.randk.Next(5, 31); //случайное число в интервале от 5 до 30 включительно
				 proc_izm = proc_izm / 100; //перевод процентного значения в десятичное
				 if(f_izmen_price==0)
				 {
					 Program.derevn.set_price_hleb(Convert.ToInt32(Program.derevn.get_price_hleb() - Program.derevn.get_price_hleb() * proc_izm));
				 }
				 if(f_izmen_price==1)
				 {
					 Program.derevn.set_price_hleb(Convert.ToInt32(Program.derevn.get_price_hleb() + Program.derevn.get_price_hleb() * proc_izm));
				 }
				 //ДЛЯ ЦЕНЫ НА СКОТ
				 f_izmen_price = Program.randk.Next(0, 2); //случайное число в интервале от 0 до 1 включительно
				 proc_izm = Program.randk.Next(5, 31); //случайное число в интервале от 5 до 30 включительно
				 proc_izm = proc_izm / 100; //перевод процентного значения в десятичное
				 if(f_izmen_price==0)
				 {
					 Program.derevn.set_price_skot(Convert.ToInt32(Program.derevn.get_price_skot() - Program.derevn.get_price_skot() * proc_izm));
				 }
				 if(f_izmen_price==1)
				 {
					 Program.derevn.set_price_skot(Convert.ToInt32(Program.derevn.get_price_skot() + Program.derevn.get_price_skot() * proc_izm));
				 }
			 }

			 if(Program.derevn.get_flag_season()==1 && (Program.derevn.get_hours_procv() - Program.derevn.get_hours_from_begin_of_season())==10) //если сейчас зима и прошло 10 часов П. от начала зимы (середина зимы) (1 день П. или 0,5 минуты)
			 {
				 int f_event; //флаг случайного события (0 - приход нового крестьянина, 1 - нападение волков на скот)
				 f_event =Program.randk.Next(0, 2); //случайное число в интервале от 0 до 1 включительно

				 double proc_izm; //процент от начального значения кол-ва скота, на которое оно изменится
				 proc_izm = Program.randk.Next(5, 31); //случайное число в интервале от 5 до 30 включительно
				 proc_izm = proc_izm / 100; //перевод процентного значения в десятичное
				 int poteri = Convert.ToInt32(Program.derevn.get_kolvo_skot() * proc_izm); //отдельная переменная для кол-ва потерянного скота

				 if(f_event==1 && poteri>0) //нападение волков
				 {
					 Program.derevn.set_kolvo_skot(Program.derevn.get_kolvo_skot() - poteri);
                     this.event_helper.Text = "Последнее событие: " + (DateTime.Now.Hour) + ":" + (DateTime.Now.Minute) + ":" + (DateTime.Now.Second) + " " + "Стая волков из леса напала на ваш скот. Потеряно " + (poteri) + " ед. скота.";
				 }
				 else //приход крестьянина
				 {
					Program.derevn.Add_rand_krest(); //добавление нового случайного крестьянина
					int koo =  Program.derevn.get_kolvo_krest() - 1; //получить номер последнего крестьянина
					string str_name= Program.derevn.krests[koo].get_name() + " " + Program.derevn.krests[koo].get_surname(); //для вывода имени и фамилии
                    this.event_helper.Text = "Последнее событие: " + (DateTime.Now.Hour) + ":" + (DateTime.Now.Minute) + ":" + (DateTime.Now.Second) + " " + "Крестьянин " + str_name + " вышел из лесу и присоединился к вам.";
				 }
			 }

			 //ВЫВОД ИНФОРМАЦИИ О ДЕРЕВНЕ
			 this.kolvo_krest_text.Text = "Крестьяне: " + (Program.derevn.get_kolvo_krest())+ " чел.";;
			 this.skorost_zhiz_text.Text = "Скорость жизни: " + (Program.derevn.get_speed_life());
			 this.den_procv_text.Text = "Дни Процветания: " + (Program.derevn.get_days_procv());
			 this.budget_text.Text = "Бюджет: " + (Program.derevn.get_budget_village()) + " руб.";
			 this.hleb_text.Text = "Хлеб: " + (Program.derevn.get_kolvo_hleb()) + " ед.";
			 this.skot_text.Text = "Домашний скот: " + (Program.derevn.get_kolvo_skot()) + " ед.";
			 if(Program.derevn.get_flag_season()==0)
				this.time_helper.Text = "До конца Лета осталось " + (40 -(Program.derevn.get_hours_procv() - Program.derevn.get_hours_from_begin_of_season())) + " Часов Процветания.";
			 if(Program.derevn.get_flag_season()==1)
				this.time_helper.Text = "До конца Зимы осталось " + (20 -(Program.derevn.get_hours_procv() - Program.derevn.get_hours_from_begin_of_season())) + " Часов Процветания.";
        }

        private void timer_refresh_Tick(object sender, EventArgs e)
        {
            //ВЫВОД ИНФОРМАЦИИ О ДЕРЕВНЕ
            this.kolvo_krest_text.Text = "Крестьяне: " + (Program.derevn.get_kolvo_krest()) + " чел."; ;
            this.skorost_zhiz_text.Text = "Скорость жизни: " + (Program.derevn.get_speed_life());
            this.den_procv_text.Text = "Дни Процветания: " + (Program.derevn.get_days_procv());
            this.budget_text.Text = "Бюджет: " + (Program.derevn.get_budget_village()) + " руб.";
            this.hleb_text.Text = "Хлеб: " + (Program.derevn.get_kolvo_hleb()) + " ед.";
            this.skot_text.Text = "Домашний скот: " + (Program.derevn.get_kolvo_skot()) + " ед.";
            if (Program.derevn.get_flag_season() == 0)
                this.time_helper.Text = "До конца Лета осталось " + (40 - (Program.derevn.get_hours_procv() - Program.derevn.get_hours_from_begin_of_season())) + " Часов Процветания.";
            if (Program.derevn.get_flag_season() == 1)
                this.time_helper.Text = "До конца Зимы осталось " + (20 - (Program.derevn.get_hours_procv() - Program.derevn.get_hours_from_begin_of_season())) + " Часов Процветания.";
        }

        private void save_game_butt_Click(object sender, EventArgs e)
        {
            Program.derevn.Save_game(); //сохранить игру в файл
            this.save_complete.Visible = true; //показать надпись об успешном сохранении
        }
    }
}
