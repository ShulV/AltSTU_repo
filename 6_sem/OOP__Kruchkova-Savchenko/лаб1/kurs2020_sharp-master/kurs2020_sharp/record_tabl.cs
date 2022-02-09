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
    public partial class record_tabl : Form
    {
        public record_tabl()
        {
            InitializeComponent();
        }

        private void record_tabl_Load(object sender, EventArgs e)
        {
             string path= "records.txt"; //путь для чтения рекордов
			 if(System.IO.File.Exists("records.txt")) //если файл существует
			 {
			    int kolvo_rec=0; //начальное значение кол-ва рекордов в файле
				string strread="strread"; //строка для чтения из файла
                using (StreamReader reader = new StreamReader(path)) //открытие файла для чтения
                {
				    while(strread!=null) //пока не прочитает весь файл
                    {
                        strread=reader.ReadLine(); //получить строку из файла
                        strread=reader.ReadLine(); //получить строку из файла
                        strread=reader.ReadLine(); //получить строку из файла
                        kolvo_rec+=1; //увеличить кол-во рекордов на 1
                    }
                    kolvo_rec = kolvo_rec -1 ; //уменьшить кол-во рекордов на 1 (в конце цикла while добавляется лишее)
                    reader.Close(); //закрыть файл
                }
                using (StreamReader reader = new StreamReader(path)) //открытие файла для чтения
                {
				    for(int g=0; g<kolvo_rec; g++)
				    {
					    spisok.Rows.Add(); //добавить новую строку в таблицу
					    spisok.Rows[g].Cells[0].Value = reader.ReadLine(); //внести в ячейку таблицы имя игрока
					    spisok.Rows[g].Cells[1].Value = reader.ReadLine(); //внести в ячейку таблицы рекорд игрока
                        strread=reader.ReadLine(); //получить строку из файла (разделитель рекордов "///////")
				    }
				    reader.Close(); //закрыть файл
                }
				//сортировка игроков по убыванию рекордов (метод пузырька)
				for(int v=1; v<kolvo_rec; v++)
				{
				    for(int b=0; b<kolvo_rec-v; b++)
				        if(Convert.ToDouble(spisok.Rows[b].Cells[1].Value) < Convert.ToDouble(spisok.Rows[b+1].Cells[1].Value))
				        {
                            Object vsp0 = spisok.Rows[b+1].Cells[0].Value;
                            Object vsp1 = spisok.Rows[b+1].Cells[1].Value;

                            spisok.Rows[b+1].Cells[0].Value = spisok.Rows[b].Cells[0].Value;
                            spisok.Rows[b+1].Cells[1].Value = spisok.Rows[b].Cells[1].Value;

                            spisok.Rows[b].Cells[0].Value = vsp0;
                            spisok.Rows[b].Cells[1].Value = vsp1;
						}
				}
			 }
        }
    }
}
