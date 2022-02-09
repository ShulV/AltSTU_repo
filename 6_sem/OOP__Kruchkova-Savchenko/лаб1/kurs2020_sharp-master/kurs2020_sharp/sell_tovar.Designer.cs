namespace kurs2020_sharp
{
    partial class sell_tovar
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
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(sell_tovar));
            this.price_hleb_text = new System.Windows.Forms.Label();
            this.price_skot_text = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.num_sell = new System.Windows.Forms.MaskedTextBox();
            this.sell_butt = new System.Windows.Forms.Button();
            this.hleb_or_skot = new System.Windows.Forms.GroupBox();
            this.skot_radio = new System.Windows.Forms.RadioButton();
            this.hleb_radio = new System.Windows.Forms.RadioButton();
            this.timer_proverka = new System.Windows.Forms.Timer(this.components);
            this.hleb_or_skot.SuspendLayout();
            this.SuspendLayout();
            // 
            // price_hleb_text
            // 
            this.price_hleb_text.AutoSize = true;
            this.price_hleb_text.BackColor = System.Drawing.SystemColors.Control;
            this.price_hleb_text.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.price_hleb_text.Font = new System.Drawing.Font("Georgia", 20.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.price_hleb_text.Location = new System.Drawing.Point(23, 55);
            this.price_hleb_text.Name = "price_hleb_text";
            this.price_hleb_text.Size = new System.Drawing.Size(355, 33);
            this.price_hleb_text.TabIndex = 3;
            this.price_hleb_text.Text = "Текущая цена за ед. хлеба:";
            // 
            // price_skot_text
            // 
            this.price_skot_text.AutoSize = true;
            this.price_skot_text.BackColor = System.Drawing.SystemColors.Control;
            this.price_skot_text.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.price_skot_text.Font = new System.Drawing.Font("Georgia", 20.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.price_skot_text.Location = new System.Drawing.Point(23, 115);
            this.price_skot_text.Name = "price_skot_text";
            this.price_skot_text.Size = new System.Drawing.Size(402, 33);
            this.price_skot_text.TabIndex = 4;
            this.price_skot_text.Text = "Текущая цена за голову скота:";
            // 
            // label2
            // 
            this.label2.BackColor = System.Drawing.SystemColors.Control;
            this.label2.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.label2.Font = new System.Drawing.Font("Century", 15.75F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.label2.ForeColor = System.Drawing.Color.FromArgb(((int)(((byte)(0)))), ((int)(((byte)(0)))), ((int)(((byte)(64)))));
            this.label2.Location = new System.Drawing.Point(41, 195);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(283, 34);
            this.label2.TabIndex = 17;
            this.label2.Text = "Продажа ресурсов, шт.";
            this.label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // num_sell
            // 
            this.num_sell.Location = new System.Drawing.Point(41, 242);
            this.num_sell.Mask = "000000000000000000000000000000000000000000000";
            this.num_sell.Name = "num_sell";
            this.num_sell.PromptChar = ' ';
            this.num_sell.Size = new System.Drawing.Size(283, 20);
            this.num_sell.TabIndex = 19;
            this.num_sell.TabStop = false;
            this.num_sell.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            this.num_sell.TextChanged += new System.EventHandler(this.num_sell_TextChanged);
            // 
            // sell_butt
            // 
            this.sell_butt.Enabled = false;
            this.sell_butt.Font = new System.Drawing.Font("Verdana", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.sell_butt.Location = new System.Drawing.Point(124, 280);
            this.sell_butt.Name = "sell_butt";
            this.sell_butt.Size = new System.Drawing.Size(119, 28);
            this.sell_butt.TabIndex = 21;
            this.sell_butt.TabStop = false;
            this.sell_butt.Text = "Продать";
            this.sell_butt.UseVisualStyleBackColor = true;
            this.sell_butt.Click += new System.EventHandler(this.sell_butt_Click);
            // 
            // hleb_or_skot
            // 
            this.hleb_or_skot.BackgroundImage = ((System.Drawing.Image)(resources.GetObject("hleb_or_skot.BackgroundImage")));
            this.hleb_or_skot.Controls.Add(this.skot_radio);
            this.hleb_or_skot.Controls.Add(this.hleb_radio);
            this.hleb_or_skot.Location = new System.Drawing.Point(366, 195);
            this.hleb_or_skot.Name = "hleb_or_skot";
            this.hleb_or_skot.Size = new System.Drawing.Size(165, 113);
            this.hleb_or_skot.TabIndex = 22;
            this.hleb_or_skot.TabStop = false;
            // 
            // skot_radio
            // 
            this.skot_radio.AutoSize = true;
            this.skot_radio.BackColor = System.Drawing.Color.Transparent;
            this.skot_radio.Font = new System.Drawing.Font("Microsoft Sans Serif", 11.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.skot_radio.Location = new System.Drawing.Point(16, 66);
            this.skot_radio.Name = "skot_radio";
            this.skot_radio.Size = new System.Drawing.Size(137, 22);
            this.skot_radio.TabIndex = 1;
            this.skot_radio.Text = "Домашний скот";
            this.skot_radio.UseVisualStyleBackColor = false;
            this.skot_radio.CheckedChanged += new System.EventHandler(this.skot_radio_CheckedChanged);
            // 
            // hleb_radio
            // 
            this.hleb_radio.AutoSize = true;
            this.hleb_radio.BackColor = System.Drawing.Color.Transparent;
            this.hleb_radio.Checked = true;
            this.hleb_radio.Font = new System.Drawing.Font("Microsoft Sans Serif", 11.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.hleb_radio.Location = new System.Drawing.Point(16, 29);
            this.hleb_radio.Name = "hleb_radio";
            this.hleb_radio.Size = new System.Drawing.Size(62, 22);
            this.hleb_radio.TabIndex = 0;
            this.hleb_radio.TabStop = true;
            this.hleb_radio.Text = "Хлеб";
            this.hleb_radio.UseVisualStyleBackColor = false;
            // 
            // timer_proverka
            // 
            this.timer_proverka.Enabled = true;
            this.timer_proverka.Interval = 1003;
            this.timer_proverka.Tick += new System.EventHandler(this.timer_proverka_Tick);
            // 
            // sell_tovar
            // 
            this.AcceptButton = this.sell_butt;
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackgroundImage = ((System.Drawing.Image)(resources.GetObject("$this.BackgroundImage")));
            this.ClientSize = new System.Drawing.Size(571, 371);
            this.Controls.Add(this.hleb_or_skot);
            this.Controls.Add(this.sell_butt);
            this.Controls.Add(this.num_sell);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.price_skot_text);
            this.Controls.Add(this.price_hleb_text);
            this.MaximizeBox = false;
            this.MaximumSize = new System.Drawing.Size(587, 410);
            this.MinimizeBox = false;
            this.MinimumSize = new System.Drawing.Size(587, 410);
            this.Name = "sell_tovar";
            this.ShowIcon = false;
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "Товарная биржа";
            this.Activated += new System.EventHandler(this.sell_tovar_Activated);
            this.hleb_or_skot.ResumeLayout(false);
            this.hleb_or_skot.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label price_hleb_text;
        private System.Windows.Forms.Label price_skot_text;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.MaskedTextBox num_sell;
        private System.Windows.Forms.Button sell_butt;
        private System.Windows.Forms.GroupBox hleb_or_skot;
        private System.Windows.Forms.RadioButton skot_radio;
        private System.Windows.Forms.RadioButton hleb_radio;
        private System.Windows.Forms.Timer timer_proverka;
    }
}