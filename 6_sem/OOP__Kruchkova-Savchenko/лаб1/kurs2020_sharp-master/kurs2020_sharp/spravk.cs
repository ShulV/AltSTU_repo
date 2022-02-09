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
    public partial class spravk : Form
    {
        public spravk()
        {
            InitializeComponent();
        }

        private void cloz_Click(object sender, EventArgs e)
        {
            this.Close();
        }

        private void timer_endgame_Tick(object sender, EventArgs e)
        {
            if (Program.f_endgame == 1) //игра закончилась, закрыть все формы
                this.Close();
        }
    }
}
