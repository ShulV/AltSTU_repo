namespace kurs2020_sharp
{
    partial class record_tabl
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
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(record_tabl));
            this.spisok = new System.Windows.Forms.DataGridView();
            this.name_tabl = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.rec_tabl = new System.Windows.Forms.DataGridViewTextBoxColumn();
            ((System.ComponentModel.ISupportInitialize)(this.spisok)).BeginInit();
            this.SuspendLayout();
            // 
            // spisok
            // 
            this.spisok.AllowUserToAddRows = false;
            this.spisok.AllowUserToDeleteRows = false;
            this.spisok.AllowUserToResizeColumns = false;
            this.spisok.AllowUserToResizeRows = false;
            this.spisok.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)));
            this.spisok.BackgroundColor = System.Drawing.Color.Maroon;
            this.spisok.ClipboardCopyMode = System.Windows.Forms.DataGridViewClipboardCopyMode.Disable;
            this.spisok.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.spisok.Columns.AddRange(new System.Windows.Forms.DataGridViewColumn[] {
            this.name_tabl,
            this.rec_tabl});
            this.spisok.EditMode = System.Windows.Forms.DataGridViewEditMode.EditProgrammatically;
            this.spisok.Location = new System.Drawing.Point(12, 12);
            this.spisok.MultiSelect = false;
            this.spisok.Name = "spisok";
            this.spisok.ReadOnly = true;
            this.spisok.RowHeadersVisible = false;
            this.spisok.RowHeadersWidthSizeMode = System.Windows.Forms.DataGridViewRowHeadersWidthSizeMode.AutoSizeToAllHeaders;
            this.spisok.ScrollBars = System.Windows.Forms.ScrollBars.Vertical;
            this.spisok.SelectionMode = System.Windows.Forms.DataGridViewSelectionMode.FullRowSelect;
            this.spisok.ShowEditingIcon = false;
            this.spisok.Size = new System.Drawing.Size(503, 467);
            this.spisok.TabIndex = 15;
            this.spisok.TabStop = false;
            // 
            // name_tabl
            // 
            this.name_tabl.AutoSizeMode = System.Windows.Forms.DataGridViewAutoSizeColumnMode.None;
            this.name_tabl.Frozen = true;
            this.name_tabl.HeaderText = "Имя игрока";
            this.name_tabl.MaxInputLength = 200;
            this.name_tabl.Name = "name_tabl";
            this.name_tabl.ReadOnly = true;
            this.name_tabl.SortMode = System.Windows.Forms.DataGridViewColumnSortMode.Programmatic;
            this.name_tabl.Width = 170;
            // 
            // rec_tabl
            // 
            this.rec_tabl.AutoSizeMode = System.Windows.Forms.DataGridViewAutoSizeColumnMode.None;
            this.rec_tabl.Frozen = true;
            this.rec_tabl.HeaderText = "Значение рекорда (кол-во набранных Дней Процветания)";
            this.rec_tabl.MaxInputLength = 200;
            this.rec_tabl.Name = "rec_tabl";
            this.rec_tabl.ReadOnly = true;
            this.rec_tabl.SortMode = System.Windows.Forms.DataGridViewColumnSortMode.Programmatic;
            this.rec_tabl.Width = 330;
            // 
            // record_tabl
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackgroundImage = ((System.Drawing.Image)(resources.GetObject("$this.BackgroundImage")));
            this.ClientSize = new System.Drawing.Size(527, 491);
            this.Controls.Add(this.spisok);
            this.DoubleBuffered = true;
            this.MinimizeBox = false;
            this.MinimumSize = new System.Drawing.Size(543, 530);
            this.Name = "record_tabl";
            this.ShowIcon = false;
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "Список рекордов";
            this.Load += new System.EventHandler(this.record_tabl_Load);
            ((System.ComponentModel.ISupportInitialize)(this.spisok)).EndInit();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.DataGridView spisok;
        private System.Windows.Forms.DataGridViewTextBoxColumn name_tabl;
        private System.Windows.Forms.DataGridViewTextBoxColumn rec_tabl;
    }
}