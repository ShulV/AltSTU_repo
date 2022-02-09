namespace kurs2020_sharp
{
    partial class itog_game
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
            this.label2 = new System.Windows.Forms.Label();
            this.label1 = new System.Windows.Forms.Label();
            this.label3 = new System.Windows.Forms.Label();
            this.your_scores = new System.Windows.Forms.Label();
            this.label5 = new System.Windows.Forms.Label();
            this.name_player = new System.Windows.Forms.TextBox();
            this.ok_record = new System.Windows.Forms.Button();
            this.close = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // label2
            // 
            this.label2.Font = new System.Drawing.Font("Palatino Linotype", 20.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.label2.ForeColor = System.Drawing.SystemColors.ControlText;
            this.label2.Location = new System.Drawing.Point(0, 9);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(284, 39);
            this.label2.TabIndex = 2;
            this.label2.Text = "Игра окончена!";
            this.label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // label1
            // 
            this.label1.Font = new System.Drawing.Font("Microsoft Sans Serif", 11.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.label1.Location = new System.Drawing.Point(0, 48);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(284, 62);
            this.label1.TabIndex = 3;
            this.label1.Text = "Все крестьяне покинули деревню.\r\nПред вашим взором только \r\nзаброшенные просторы." +
                "";
            this.label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // label3
            // 
            this.label3.Font = new System.Drawing.Font("Palatino Linotype", 12.75F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.label3.ForeColor = System.Drawing.Color.FromArgb(((int)(((byte)(0)))), ((int)(((byte)(192)))), ((int)(((byte)(0)))));
            this.label3.Location = new System.Drawing.Point(-1, 112);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(223, 39);
            this.label3.TabIndex = 4;
            this.label3.Text = "Итоговый счёт (Дни П.):";
            this.label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // your_scores
            // 
            this.your_scores.Font = new System.Drawing.Font("Palatino Linotype", 14.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.your_scores.ForeColor = System.Drawing.Color.FromArgb(((int)(((byte)(64)))), ((int)(((byte)(0)))), ((int)(((byte)(64)))));
            this.your_scores.Location = new System.Drawing.Point(213, 118);
            this.your_scores.Name = "your_scores";
            this.your_scores.Size = new System.Drawing.Size(69, 60);
            this.your_scores.TabIndex = 5;
            this.your_scores.Text = "12345";
            // 
            // label5
            // 
            this.label5.AutoSize = true;
            this.label5.Location = new System.Drawing.Point(36, 152);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(221, 13);
            this.label5.TabIndex = 6;
            this.label5.Text = "Введите ваше имя: (для списка рекордов)";
            // 
            // name_player
            // 
            this.name_player.Location = new System.Drawing.Point(79, 168);
            this.name_player.MaxLength = 20;
            this.name_player.Name = "name_player";
            this.name_player.Size = new System.Drawing.Size(128, 20);
            this.name_player.TabIndex = 7;
            this.name_player.Text = "player";
            this.name_player.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            this.name_player.TextChanged += new System.EventHandler(this.name_player_TextChanged);
            // 
            // ok_record
            // 
            this.ok_record.Font = new System.Drawing.Font("Microsoft Sans Serif", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.ok_record.Location = new System.Drawing.Point(17, 194);
            this.ok_record.Name = "ok_record";
            this.ok_record.Size = new System.Drawing.Size(118, 44);
            this.ok_record.TabIndex = 8;
            this.ok_record.Text = "записать и закрыть";
            this.ok_record.UseVisualStyleBackColor = true;
            this.ok_record.Click += new System.EventHandler(this.ok_record_Click);
            // 
            // close
            // 
            this.close.DialogResult = System.Windows.Forms.DialogResult.Cancel;
            this.close.Font = new System.Drawing.Font("Microsoft Sans Serif", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.close.Location = new System.Drawing.Point(154, 194);
            this.close.Name = "close";
            this.close.Size = new System.Drawing.Size(118, 44);
            this.close.TabIndex = 9;
            this.close.Text = "закрыть без сохранения рекорда";
            this.close.UseVisualStyleBackColor = true;
            this.close.Click += new System.EventHandler(this.close_Click);
            // 
            // itog_game
            // 
            this.AcceptButton = this.ok_record;
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.CancelButton = this.close;
            this.ClientSize = new System.Drawing.Size(284, 261);
            this.ControlBox = false;
            this.Controls.Add(this.close);
            this.Controls.Add(this.ok_record);
            this.Controls.Add(this.name_player);
            this.Controls.Add(this.label5);
            this.Controls.Add(this.your_scores);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.label2);
            this.MaximizeBox = false;
            this.MaximumSize = new System.Drawing.Size(300, 300);
            this.MinimizeBox = false;
            this.MinimumSize = new System.Drawing.Size(300, 300);
            this.Name = "itog_game";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "Конец игры";
            this.TopMost = true;
            this.Load += new System.EventHandler(this.itog_game_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.Label your_scores;
        private System.Windows.Forms.Label label5;
        private System.Windows.Forms.TextBox name_player;
        private System.Windows.Forms.Button ok_record;
        private System.Windows.Forms.Button close;
    }
}