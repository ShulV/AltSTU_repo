namespace kurs2020_sharp
{
    partial class Form1
    {
        /// <summary>
        /// Требуется переменная конструктора.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Освободить все используемые ресурсы.
        /// </summary>
        /// <param name="disposing">истинно, если управляемый ресурс должен быть удален; иначе ложно.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Код, автоматически созданный конструктором форм Windows

        /// <summary>
        /// Обязательный метод для поддержки конструктора - не изменяйте
        /// содержимое данного метода при помощи редактора кода.
        /// </summary>
        private void InitializeComponent()
        {
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(Form1));
            this.info_avtor = new System.Windows.Forms.Label();
            this.spravk_butt = new System.Windows.Forms.Button();
            this.igra_menu_text = new System.Windows.Forms.Label();
            this.glavn_menu_text = new System.Windows.Forms.Label();
            this.new_game_butt = new System.Windows.Forms.Button();
            this.load_game_butt = new System.Windows.Forms.Button();
            this.records_butt = new System.Windows.Forms.Button();
            this.quit_butt = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // info_avtor
            // 
            this.info_avtor.AutoSize = true;
            this.info_avtor.BackColor = System.Drawing.Color.Transparent;
            this.info_avtor.Font = new System.Drawing.Font("Microsoft Sans Serif", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.info_avtor.ForeColor = System.Drawing.SystemColors.ControlLightLight;
            this.info_avtor.Location = new System.Drawing.Point(3, 3);
            this.info_avtor.Name = "info_avtor";
            this.info_avtor.Size = new System.Drawing.Size(224, 15);
            this.info_avtor.TabIndex = 8;
            this.info_avtor.Text = "© Гулин Алексей, ПИ-92. АлтГТУ 2020";
            // 
            // spravk_butt
            // 
            this.spravk_butt.Font = new System.Drawing.Font("Franklin Gothic Demi", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.spravk_butt.Location = new System.Drawing.Point(316, 3);
            this.spravk_butt.Name = "spravk_butt";
            this.spravk_butt.Size = new System.Drawing.Size(28, 32);
            this.spravk_butt.TabIndex = 5;
            this.spravk_butt.Text = "?";
            this.spravk_butt.UseVisualStyleBackColor = true;
            this.spravk_butt.Click += new System.EventHandler(this.spravk_butt_Click);
            // 
            // igra_menu_text
            // 
            this.igra_menu_text.BackColor = System.Drawing.Color.Transparent;
            this.igra_menu_text.Font = new System.Drawing.Font("Franklin Gothic Heavy", 15.75F, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.igra_menu_text.ForeColor = System.Drawing.Color.Navy;
            this.igra_menu_text.Location = new System.Drawing.Point(1, 38);
            this.igra_menu_text.Name = "igra_menu_text";
            this.igra_menu_text.Size = new System.Drawing.Size(343, 29);
            this.igra_menu_text.TabIndex = 10;
            this.igra_menu_text.Text = "Игра \"Управление деревней\"";
            this.igra_menu_text.TextAlign = System.Drawing.ContentAlignment.TopCenter;
            // 
            // glavn_menu_text
            // 
            this.glavn_menu_text.BackColor = System.Drawing.Color.Transparent;
            this.glavn_menu_text.Font = new System.Drawing.Font("Franklin Gothic Heavy", 20.25F, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.glavn_menu_text.ForeColor = System.Drawing.Color.FromArgb(((int)(((byte)(0)))), ((int)(((byte)(64)))), ((int)(((byte)(64)))));
            this.glavn_menu_text.Location = new System.Drawing.Point(0, 62);
            this.glavn_menu_text.Name = "glavn_menu_text";
            this.glavn_menu_text.Size = new System.Drawing.Size(344, 44);
            this.glavn_menu_text.TabIndex = 11;
            this.glavn_menu_text.Text = "Главное меню";
            this.glavn_menu_text.TextAlign = System.Drawing.ContentAlignment.TopCenter;
            // 
            // new_game_butt
            // 
            this.new_game_butt.Font = new System.Drawing.Font("Franklin Gothic Demi", 14.25F, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.new_game_butt.Location = new System.Drawing.Point(60, 121);
            this.new_game_butt.Name = "new_game_butt";
            this.new_game_butt.Size = new System.Drawing.Size(220, 48);
            this.new_game_butt.TabIndex = 1;
            this.new_game_butt.Text = "Новая игра";
            this.new_game_butt.UseVisualStyleBackColor = true;
            this.new_game_butt.Click += new System.EventHandler(this.new_game_butt_Click);
            // 
            // load_game_butt
            // 
            this.load_game_butt.Font = new System.Drawing.Font("Franklin Gothic Demi", 11.25F, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.load_game_butt.Location = new System.Drawing.Point(60, 185);
            this.load_game_butt.Name = "load_game_butt";
            this.load_game_butt.Size = new System.Drawing.Size(220, 48);
            this.load_game_butt.TabIndex = 2;
            this.load_game_butt.Text = "Загрузка\r\nнезаконченной игры";
            this.load_game_butt.UseVisualStyleBackColor = true;
            this.load_game_butt.Click += new System.EventHandler(this.load_game_butt_Click);
            // 
            // records_butt
            // 
            this.records_butt.Font = new System.Drawing.Font("Franklin Gothic Demi", 14.25F, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.records_butt.Location = new System.Drawing.Point(60, 248);
            this.records_butt.Name = "records_butt";
            this.records_butt.Size = new System.Drawing.Size(220, 48);
            this.records_butt.TabIndex = 3;
            this.records_butt.Text = "Список рекордов";
            this.records_butt.UseVisualStyleBackColor = true;
            this.records_butt.Click += new System.EventHandler(this.records_butt_Click);
            // 
            // quit_butt
            // 
            this.quit_butt.DialogResult = System.Windows.Forms.DialogResult.Cancel;
            this.quit_butt.Font = new System.Drawing.Font("Franklin Gothic Demi", 14.25F, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.quit_butt.Location = new System.Drawing.Point(60, 311);
            this.quit_butt.Name = "quit_butt";
            this.quit_butt.Size = new System.Drawing.Size(220, 48);
            this.quit_butt.TabIndex = 4;
            this.quit_butt.Text = "Выход из игры";
            this.quit_butt.UseVisualStyleBackColor = true;
            this.quit_butt.Click += new System.EventHandler(this.quit_butt_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackgroundImage = ((System.Drawing.Image)(resources.GetObject("$this.BackgroundImage")));
            this.CancelButton = this.quit_butt;
            this.ClientSize = new System.Drawing.Size(346, 387);
            this.ControlBox = false;
            this.Controls.Add(this.quit_butt);
            this.Controls.Add(this.records_butt);
            this.Controls.Add(this.load_game_butt);
            this.Controls.Add(this.new_game_butt);
            this.Controls.Add(this.glavn_menu_text);
            this.Controls.Add(this.igra_menu_text);
            this.Controls.Add(this.spravk_butt);
            this.Controls.Add(this.info_avtor);
            this.Icon = ((System.Drawing.Icon)(resources.GetObject("$this.Icon")));
            this.MaximumSize = new System.Drawing.Size(362, 426);
            this.MinimumSize = new System.Drawing.Size(362, 426);
            this.Name = "Form1";
            this.RightToLeftLayout = true;
            this.ShowIcon = false;
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "Главное меню";
            this.Activated += new System.EventHandler(this.Form1_Activated);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label info_avtor;
        private System.Windows.Forms.Button spravk_butt;
        private System.Windows.Forms.Label igra_menu_text;
        private System.Windows.Forms.Label glavn_menu_text;
        private System.Windows.Forms.Button new_game_butt;
        private System.Windows.Forms.Button load_game_butt;
        private System.Windows.Forms.Button records_butt;
        private System.Windows.Forms.Button quit_butt;
    }
}

