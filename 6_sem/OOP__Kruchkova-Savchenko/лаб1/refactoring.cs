using System.Windows.Forms;

private int count_record_number(string path) {
    const int COLUMNS_IN_RECORDS_FILE = 2;
    using (StreamReader reader = new StreamReader(path)) //открытие файла для чтения
    {
        int rec_number = 0;//начальное значение кол-ва рекордов в файле
        while (strread != null) //пока не прочитает весь файл
        {
            //структура файла: строка имя,строка рекорд,строка для разделения
            for(int i=0; i < COLUMNS_IN_RECORDS_FILE + 1; i++)
                strread = reader.ReadLine(); //получить строку из файла
            rec_number += 1; //увеличить кол-во рекордов на 1
        }
        rec_number--; //уменьшить кол-во рекордов на 1 (в конце цикла while добавляется лишнее)
    }
}

private void fill_table_from_file(string path, int rec_num) {
    DataGridView table = new DataGridView();
    using (StreamReader reader = new StreamReader(path)) //открытие файла для чтения
    {
        for (int i = 0; i < rec_number; i++)
        {
            table.Rows.Add(); //добавить новую строку в таблицу
            table.Rows[i].Cells[0].Value = reader.ReadLine(); //внести в ячейку таблицы имя игрока
            table.Rows[i].Cells[1].Value = reader.ReadLine(); //внести в ячейку таблицы рекорд игрока
            strread = reader.ReadLine(); //получить строку из файла (разделитель рекордов "///////")
        }
    }
}

private void tableBubbleSort(string path, int rec_num) {
    for (int i = 1; i < rec_number; i++)
    {
        for (int j = 0; j < rec_number - i; j++)
            if (Convert.ToDouble(table.Rows[j].Cells[1].Value) < Convert.ToDouble(table.Rows[j + 1].Cells[1].Value))
            {
                Object temp0 = table.Rows[j + 1].Cells[0].Value;
                Object temp1 = table.Rows[j + 1].Cells[1].Value;

                table.Rows[j + 1].Cells[0].Value = table.Rows[j].Cells[0].Value;
                table.Rows[j + 1].Cells[1].Value = table.Rows[j].Cells[1].Value;

                table.Rows[j].Cells[0].Value = temp0;
                table.Rows[j].Cells[1].Value = temp1;
            }
    }
}

private void record_tabl_Load(object sender, EventArgs e) {
    string path= "records.txt"; //путь для чтения рекордов
    if (System.IO.File.Exists("records.txt")) //если файл существует
    {
        string strread = "strread"; //строка для чтения из файла

        int rec_num = count_record_number(path); //начальное значение кол-ва рекордов в файле

        fill_table_from_file(path, rec_num);

        //сортировка игроков по убыванию рекордов (метод пузырька)
        tableBubbleSort(path, rec_num);
    }
    else return 1;
}
