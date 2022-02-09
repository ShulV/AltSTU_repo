namespace kurs2020_sharp
{
    partial class spravk
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
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(spravk));
            this.spravka_info = new System.Windows.Forms.TextBox();
            this.cloz = new System.Windows.Forms.Button();
            this.timer_endgame = new System.Windows.Forms.Timer(this.components);
            this.SuspendLayout();
            // 
            // spravka_info
            // 
            this.spravka_info.Location = new System.Drawing.Point(12, 12);
            this.spravka_info.Multiline = true;
            this.spravka_info.Name = "spravka_info";
            this.spravka_info.ReadOnly = true;
            this.spravka_info.ScrollBars = System.Windows.Forms.ScrollBars.Vertical;
            this.spravka_info.Size = new System.Drawing.Size(311, 326);
            this.spravka_info.TabIndex = 1;
            this.spravka_info.TabStop = false;
            this.spravka_info.Text = resources.GetString("spravka_info.Text");
            // 
            // cloz
            // 
            this.cloz.Cursor = System.Windows.Forms.Cursors.Hand;
            this.cloz.DialogResult = System.Windows.Forms.DialogResult.Cancel;
            this.cloz.Location = new System.Drawing.Point(12, 344);
            this.cloz.Name = "cloz";
            this.cloz.Size = new System.Drawing.Size(311, 23);
            this.cloz.TabIndex = 2;
            this.cloz.Text = "Закрыть";
            this.cloz.UseVisualStyleBackColor = true;
            this.cloz.Click += new System.EventHandler(this.cloz_Click);
            // 
            // timer_endgame
            // 
            this.timer_endgame.Enabled = true;
            this.timer_endgame.Interval = 1003;
            this.timer_endgame.Tick += new System.EventHandler(this.timer_endgame_Tick);
            // 
            // spravk
            // 
            this.AcceptButton = this.cloz;
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.CancelButton = this.cloz;
            this.ClientSize = new System.Drawing.Size(335, 373);
            this.Controls.Add(this.cloz);
            this.Controls.Add(this.spravka_info);
            this.Icon = ((System.Drawing.Icon)(resources.GetObject("$this.Icon")));
            this.MaximizeBox = false;
            this.MaximumSize = new System.Drawing.Size(351, 412);
            this.MinimizeBox = false;
            this.MinimumSize = new System.Drawing.Size(351, 412);
            this.Name = "spravk";
            this.ShowInTaskbar = false;
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "Справка";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.TextBox spravka_info;
        private System.Windows.Forms.Button cloz;
        private System.Windows.Forms.Timer timer_endgame;
    }
}