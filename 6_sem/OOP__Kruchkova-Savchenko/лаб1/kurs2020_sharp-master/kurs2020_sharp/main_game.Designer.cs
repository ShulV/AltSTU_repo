namespace kurs2020_sharp
{
    partial class main_game
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.components = new System.ComponentModel.Container();
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(main_game));
            this.label1 = new System.Windows.Forms.Label();
            this.lent_menu = new System.Windows.Forms.MenuStrip();
            this.save_game_butt = new System.Windows.Forms.ToolStripMenuItem();
            this.spravk_lent_butt = new System.Windows.Forms.ToolStripMenuItem();
            this.go_to_main_menu_butt = new System.Windows.Forms.ToolStripMenuItem();
            this.vihod_info = new System.Windows.Forms.Label();
            this.save_complete = new System.Windows.Forms.Label();
            this.skorost_zhiz_text = new System.Windows.Forms.Label();
            this.den_procv_text = new System.Windows.Forms.Label();
            this.kolvo_krest_text = new System.Windows.Forms.Label();
            this.budget_text = new System.Windows.Forms.Label();
            this.hleb_text = new System.Windows.Forms.Label();
            this.skot_text = new System.Windows.Forms.Label();
            this.spisok_krest_butt = new System.Windows.Forms.Button();
            this.birzha_butt = new System.Windows.Forms.Button();
            this.pomoshnik_box = new System.Windows.Forms.GroupBox();
            this.event_helper = new System.Windows.Forms.Label();
            this.time_helper = new System.Windows.Forms.Label();
            this.main_timer = new System.Windows.Forms.Timer(this.components);
            this.timer_refresh = new System.Windows.Forms.Timer(this.components);
            this.lent_menu.SuspendLayout();
            this.pomoshnik_box.SuspendLayout();
            this.SuspendLayout();
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(210)))), ((int)(((byte)(210)))), ((int)(((byte)(210)))));
            this.label1.Location = new System.Drawing.Point(2, 2);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(227, 26);
            this.label1.TabIndex = 11;
            this.label1.Text = "1 Час Процветания = 3 реальные секунды\r\n1 День Процветания = 30 реальных секунд";
            // 
            // lent_menu
            // 
            this.lent_menu.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
            this.lent_menu.Dock = System.Windows.Forms.DockStyle.None;
            this.lent_menu.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.save_game_butt,
            this.spravk_lent_butt,
            this.go_to_main_menu_butt});
            this.lent_menu.Location = new System.Drawing.Point(382, 0);
            this.lent_menu.Name = "lent_menu";
            this.lent_menu.RightToLeft = System.Windows.Forms.RightToLeft.No;
            this.lent_menu.Size = new System.Drawing.Size(464, 24);
            this.lent_menu.TabIndex = 12;
            this.lent_menu.Text = "lent_menu";
            // 
            // save_game_butt
            // 
            this.save_game_butt.Image = ((System.Drawing.Image)(resources.GetObject("save_game_butt.Image")));
            this.save_game_butt.Name = "save_game_butt";
            this.save_game_butt.Size = new System.Drawing.Size(122, 20);
            this.save_game_butt.Text = "Сохранить игру";
            this.save_game_butt.Click += new System.EventHandler(this.save_game_butt_Click);
            // 
            // spravk_lent_butt
            // 
            this.spravk_lent_butt.Image = ((System.Drawing.Image)(resources.GetObject("spravk_lent_butt.Image")));
            this.spravk_lent_butt.Name = "spravk_lent_butt";
            this.spravk_lent_butt.Size = new System.Drawing.Size(81, 20);
            this.spravk_lent_butt.Text = "Справка";
            this.spravk_lent_butt.Click += new System.EventHandler(this.spravk_lent_butt_Click);
            // 
            // go_to_main_menu_butt
            // 
            this.go_to_main_menu_butt.Image = ((System.Drawing.Image)(resources.GetObject("go_to_main_menu_butt.Image")));
            this.go_to_main_menu_butt.Name = "go_to_main_menu_butt";
            this.go_to_main_menu_butt.Size = new System.Drawing.Size(161, 20);
            this.go_to_main_menu_butt.Text = "Выход в главное меню";
            this.go_to_main_menu_butt.Click += new System.EventHandler(this.go_to_main_menu_butt_Click);
            // 
            // vihod_info
            // 
            this.vihod_info.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
            this.vihod_info.AutoSize = true;
            this.vihod_info.Location = new System.Drawing.Point(621, 28);
            this.vihod_info.Name = "vihod_info";
            this.vihod_info.Size = new System.Drawing.Size(223, 13);
            this.vihod_info.TabIndex = 13;
            this.vihod_info.Text = "Не забудь сохранить игру перед выходом!";
            // 
            // save_complete
            // 
            this.save_complete.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
            this.save_complete.AutoSize = true;
            this.save_complete.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(192)))), ((int)(((byte)(255)))), ((int)(((byte)(192)))));
            this.save_complete.Location = new System.Drawing.Point(474, 28);
            this.save_complete.Name = "save_complete";
            this.save_complete.Size = new System.Drawing.Size(137, 13);
            this.save_complete.TabIndex = 14;
            this.save_complete.Text = "Игра успешно сохранена!";
            this.save_complete.Visible = false;
            // 
            // skorost_zhiz_text
            // 
            this.skorost_zhiz_text.AutoSize = true;
            this.skorost_zhiz_text.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.skorost_zhiz_text.Font = new System.Drawing.Font("Georgia", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.skorost_zhiz_text.Location = new System.Drawing.Point(12, 50);
            this.skorost_zhiz_text.Name = "skorost_zhiz_text";
            this.skorost_zhiz_text.Size = new System.Drawing.Size(212, 31);
            this.skorost_zhiz_text.TabIndex = 15;
            this.skorost_zhiz_text.Text = "Скорость жизни: ";
            // 
            // den_procv_text
            // 
            this.den_procv_text.AutoSize = true;
            this.den_procv_text.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.den_procv_text.Font = new System.Drawing.Font("Georgia", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.den_procv_text.Location = new System.Drawing.Point(12, 91);
            this.den_procv_text.Name = "den_procv_text";
            this.den_procv_text.Size = new System.Drawing.Size(232, 31);
            this.den_procv_text.TabIndex = 16;
            this.den_procv_text.Text = "Дни Процветания: ";
            // 
            // kolvo_krest_text
            // 
            this.kolvo_krest_text.AutoSize = true;
            this.kolvo_krest_text.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.kolvo_krest_text.Font = new System.Drawing.Font("Georgia", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.kolvo_krest_text.Location = new System.Drawing.Point(12, 134);
            this.kolvo_krest_text.Name = "kolvo_krest_text";
            this.kolvo_krest_text.Size = new System.Drawing.Size(146, 31);
            this.kolvo_krest_text.TabIndex = 17;
            this.kolvo_krest_text.Text = "Крестьяне: ";
            // 
            // budget_text
            // 
            this.budget_text.AutoSize = true;
            this.budget_text.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.budget_text.Font = new System.Drawing.Font("Georgia", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.budget_text.Location = new System.Drawing.Point(12, 178);
            this.budget_text.Name = "budget_text";
            this.budget_text.Size = new System.Drawing.Size(164, 31);
            this.budget_text.TabIndex = 18;
            this.budget_text.Text = "Бюджет: руб.";
            // 
            // hleb_text
            // 
            this.hleb_text.AutoSize = true;
            this.hleb_text.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.hleb_text.Font = new System.Drawing.Font("Georgia", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.hleb_text.Location = new System.Drawing.Point(12, 220);
            this.hleb_text.Name = "hleb_text";
            this.hleb_text.Size = new System.Drawing.Size(85, 31);
            this.hleb_text.TabIndex = 19;
            this.hleb_text.Text = "Хлеб: ";
            // 
            // skot_text
            // 
            this.skot_text.AutoSize = true;
            this.skot_text.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.skot_text.Font = new System.Drawing.Font("Georgia", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.skot_text.Location = new System.Drawing.Point(12, 262);
            this.skot_text.Name = "skot_text";
            this.skot_text.Size = new System.Drawing.Size(208, 31);
            this.skot_text.TabIndex = 20;
            this.skot_text.Text = "Домашний скот: ";
            // 
            // spisok_krest_butt
            // 
            this.spisok_krest_butt.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
            this.spisok_krest_butt.Font = new System.Drawing.Font("DejaVu Serif Condensed", 14.25F, ((System.Drawing.FontStyle)((System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic))), System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.spisok_krest_butt.Location = new System.Drawing.Point(612, 83);
            this.spisok_krest_butt.Name = "spisok_krest_butt";
            this.spisok_krest_butt.Size = new System.Drawing.Size(220, 48);
            this.spisok_krest_butt.TabIndex = 21;
            this.spisok_krest_butt.TabStop = false;
            this.spisok_krest_butt.Text = "Список крестьян";
            this.spisok_krest_butt.UseVisualStyleBackColor = true;
            this.spisok_krest_butt.Click += new System.EventHandler(this.spisok_krest_butt_Click);
            // 
            // birzha_butt
            // 
            this.birzha_butt.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
            this.birzha_butt.Font = new System.Drawing.Font("DejaVu Serif Condensed", 14.25F, ((System.Drawing.FontStyle)((System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic))), System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.birzha_butt.Location = new System.Drawing.Point(612, 147);
            this.birzha_butt.Name = "birzha_butt";
            this.birzha_butt.Size = new System.Drawing.Size(220, 48);
            this.birzha_butt.TabIndex = 22;
            this.birzha_butt.TabStop = false;
            this.birzha_butt.Text = "Товарная биржа";
            this.birzha_butt.UseVisualStyleBackColor = true;
            this.birzha_butt.Click += new System.EventHandler(this.birzha_butt_Click);
            // 
            // pomoshnik_box
            // 
            this.pomoshnik_box.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left)
                        | System.Windows.Forms.AnchorStyles.Right)));
            this.pomoshnik_box.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(255)))), ((int)(((byte)(255)))), ((int)(((byte)(200)))));
            this.pomoshnik_box.BackgroundImage = ((System.Drawing.Image)(resources.GetObject("pomoshnik_box.BackgroundImage")));
            this.pomoshnik_box.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch;
            this.pomoshnik_box.Controls.Add(this.event_helper);
            this.pomoshnik_box.Controls.Add(this.time_helper);
            this.pomoshnik_box.Font = new System.Drawing.Font("Calibri", 12.75F, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.pomoshnik_box.Location = new System.Drawing.Point(12, 389);
            this.pomoshnik_box.Name = "pomoshnik_box";
            this.pomoshnik_box.RightToLeft = System.Windows.Forms.RightToLeft.Yes;
            this.pomoshnik_box.Size = new System.Drawing.Size(820, 100);
            this.pomoshnik_box.TabIndex = 23;
            this.pomoshnik_box.TabStop = false;
            this.pomoshnik_box.Text = "Информация от Помощника";
            // 
            // event_helper
            // 
            this.event_helper.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left)
                        | System.Windows.Forms.AnchorStyles.Right)));
            this.event_helper.BackColor = System.Drawing.Color.Transparent;
            this.event_helper.Cursor = System.Windows.Forms.Cursors.Default;
            this.event_helper.Font = new System.Drawing.Font("Cambria", 14.25F, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.event_helper.Location = new System.Drawing.Point(6, 51);
            this.event_helper.Name = "event_helper";
            this.event_helper.RightToLeft = System.Windows.Forms.RightToLeft.No;
            this.event_helper.Size = new System.Drawing.Size(808, 46);
            this.event_helper.TabIndex = 1;
            this.event_helper.Text = " ";
            // 
            // time_helper
            // 
            this.time_helper.AutoSize = true;
            this.time_helper.BackColor = System.Drawing.Color.Transparent;
            this.time_helper.Font = new System.Drawing.Font("Cambria", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.time_helper.Location = new System.Drawing.Point(6, 24);
            this.time_helper.Name = "time_helper";
            this.time_helper.RightToLeft = System.Windows.Forms.RightToLeft.No;
            this.time_helper.Size = new System.Drawing.Size(540, 22);
            this.time_helper.TabIndex = 0;
            this.time_helper.Text = "До конца этого времени года осталось 11 Часов Процветания.";
            // 
            // main_timer
            // 
            this.main_timer.Enabled = true;
            this.main_timer.Interval = 3000;
            this.main_timer.Tick += new System.EventHandler(this.main_timer_Tick);
            // 
            // timer_refresh
            // 
            this.timer_refresh.Enabled = true;
            this.timer_refresh.Interval = 512;
            this.timer_refresh.Tick += new System.EventHandler(this.timer_refresh_Tick);
            // 
            // main_game
            // 
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.None;
            this.BackgroundImage = ((System.Drawing.Image)(resources.GetObject("$this.BackgroundImage")));
            this.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch;
            this.ClientSize = new System.Drawing.Size(844, 501);
            this.Controls.Add(this.pomoshnik_box);
            this.Controls.Add(this.birzha_butt);
            this.Controls.Add(this.spisok_krest_butt);
            this.Controls.Add(this.skot_text);
            this.Controls.Add(this.hleb_text);
            this.Controls.Add(this.budget_text);
            this.Controls.Add(this.kolvo_krest_text);
            this.Controls.Add(this.den_procv_text);
            this.Controls.Add(this.skorost_zhiz_text);
            this.Controls.Add(this.save_complete);
            this.Controls.Add(this.vihod_info);
            this.Controls.Add(this.lent_menu);
            this.Controls.Add(this.label1);
            this.Icon = ((System.Drawing.Icon)(resources.GetObject("$this.Icon")));
            this.MainMenuStrip = this.lent_menu;
            this.MinimizeBox = false;
            this.MinimumSize = new System.Drawing.Size(860, 540);
            this.Name = "main_game";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "Игра \"Управление деревней\"";
            this.WindowState = System.Windows.Forms.FormWindowState.Maximized;
            this.Load += new System.EventHandler(this.main_game_Load);
            this.lent_menu.ResumeLayout(false);
            this.lent_menu.PerformLayout();
            this.pomoshnik_box.ResumeLayout(false);
            this.pomoshnik_box.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.MenuStrip lent_menu;
        private System.Windows.Forms.ToolStripMenuItem save_game_butt;
        private System.Windows.Forms.ToolStripMenuItem spravk_lent_butt;
        private System.Windows.Forms.ToolStripMenuItem go_to_main_menu_butt;
        private System.Windows.Forms.Label vihod_info;
        private System.Windows.Forms.Label save_complete;
        private System.Windows.Forms.Label skorost_zhiz_text;
        private System.Windows.Forms.Label den_procv_text;
        private System.Windows.Forms.Label kolvo_krest_text;
        private System.Windows.Forms.Label budget_text;
        private System.Windows.Forms.Label hleb_text;
        private System.Windows.Forms.Label skot_text;
        private System.Windows.Forms.Button spisok_krest_butt;
        private System.Windows.Forms.Button birzha_butt;
        private System.Windows.Forms.GroupBox pomoshnik_box;
        private System.Windows.Forms.Label event_helper;
        private System.Windows.Forms.Label time_helper;
        private System.Windows.Forms.Timer main_timer;
        private System.Windows.Forms.Timer timer_refresh;
    }
}