using System;

namespace ImageCorrection
{
    partial class Form1
    {
        /// <summary>
        /// Обязательная переменная конструктора.
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
        /// Требуемый метод для поддержки конструктора — не изменяйте 
        /// содержимое этого метода с помощью редактора кода.
        /// </summary>
        private void InitializeComponent()
        {
            System.Windows.Forms.DataVisualization.Charting.ChartArea chartArea1 = new System.Windows.Forms.DataVisualization.Charting.ChartArea();
            System.Windows.Forms.DataVisualization.Charting.Series series1 = new System.Windows.Forms.DataVisualization.Charting.Series();
            this.chart = new System.Windows.Forms.DataVisualization.Charting.Chart();
            this.loadButton = new System.Windows.Forms.Button();
            this.openFileDialog1 = new System.Windows.Forms.OpenFileDialog();
            this.addBrightnessButton = new System.Windows.Forms.Button();
            this.brightnessInput = new System.Windows.Forms.NumericUpDown();
            this.addContrastButton = new System.Windows.Forms.Button();
            this.contrastInput = new System.Windows.Forms.NumericUpDown();
            this.binarizationButton = new System.Windows.Forms.Button();
            this.binarizationInput = new System.Windows.Forms.NumericUpDown();
            this.grayscaleButton = new System.Windows.Forms.Button();
            this.negativeButton = new System.Windows.Forms.Button();
            this.label1 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.uniformButton = new System.Windows.Forms.Button();
            this.aquarelButton = new System.Windows.Forms.Button();
            this.progressBar = new System.Windows.Forms.ProgressBar();
            this.label3 = new System.Windows.Forms.Label();
            this.medianButton = new System.Windows.Forms.Button();
            this.gaussAntiNoiseButton = new System.Windows.Forms.Button();
            this.noiseButton = new System.Windows.Forms.Button();
            this.label4 = new System.Windows.Forms.Label();
            this.gaussNoiseButton = new System.Windows.Forms.Button();
            this.sharpnessButton = new System.Windows.Forms.Button();
            this.label5 = new System.Windows.Forms.Label();
            this.embossingButton = new System.Windows.Forms.Button();
            this.sobelButton = new System.Windows.Forms.Button();
            this.label6 = new System.Windows.Forms.Label();
            this.previtButton = new System.Windows.Forms.Button();
            this.robertsButton = new System.Windows.Forms.Button();
            this.reloadButton = new System.Windows.Forms.Button();
            this.pictureBox1 = new System.Windows.Forms.PictureBox();
            this.porog = new System.Windows.Forms.NumericUpDown();
            ((System.ComponentModel.ISupportInitialize)(this.chart)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.brightnessInput)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.contrastInput)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.binarizationInput)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.porog)).BeginInit();
            this.SuspendLayout();
            // 
            // chart
            // 
            chartArea1.Name = "ChartArea1";
            this.chart.ChartAreas.Add(chartArea1);
            this.chart.Location = new System.Drawing.Point(756, 93);
            this.chart.Name = "chart";
            series1.ChartArea = "ChartArea1";
            series1.Name = "Series1";
            this.chart.Series.Add(series1);
            this.chart.Size = new System.Drawing.Size(563, 406);
            this.chart.TabIndex = 1;
            this.chart.Text = "chart1";
            // 
            // loadButton
            // 
            this.loadButton.Location = new System.Drawing.Point(12, 3);
            this.loadButton.Name = "loadButton";
            this.loadButton.Size = new System.Drawing.Size(75, 23);
            this.loadButton.TabIndex = 2;
            this.loadButton.Text = "Загрузить";
            this.loadButton.UseVisualStyleBackColor = true;
            this.loadButton.Click += new System.EventHandler(this.loadButton_Click);
            // 
            // openFileDialog1
            // 
            this.openFileDialog1.FileName = "openFileDialog1";
            this.openFileDialog1.Filter = "Image Files (*.bmp;*.png;*.jpg;*.jpeg)|*.bmp;*.png;*.jpg;*.jpeg";
            // 
            // addBrightnessButton
            // 
            this.addBrightnessButton.Enabled = false;
            this.addBrightnessButton.Location = new System.Drawing.Point(229, 5);
            this.addBrightnessButton.Name = "addBrightnessButton";
            this.addBrightnessButton.Size = new System.Drawing.Size(114, 23);
            this.addBrightnessButton.TabIndex = 4;
            this.addBrightnessButton.Text = "Увеличить яркость";
            this.addBrightnessButton.UseVisualStyleBackColor = true;
            this.addBrightnessButton.Click += new System.EventHandler(this.addBrightnessButton_Click);
            // 
            // brightnessInput
            // 
            this.brightnessInput.Enabled = false;
            this.brightnessInput.Location = new System.Drawing.Point(343, 7);
            this.brightnessInput.Maximum = new decimal(new int[] {
            500,
            0,
            0,
            0});
            this.brightnessInput.Minimum = new decimal(new int[] {
            500,
            0,
            0,
            -2147483648});
            this.brightnessInput.Name = "brightnessInput";
            this.brightnessInput.Size = new System.Drawing.Size(56, 20);
            this.brightnessInput.TabIndex = 5;
            // 
            // addContrastButton
            // 
            this.addContrastButton.Enabled = false;
            this.addContrastButton.Location = new System.Drawing.Point(405, 4);
            this.addContrastButton.Name = "addContrastButton";
            this.addContrastButton.Size = new System.Drawing.Size(147, 23);
            this.addContrastButton.TabIndex = 4;
            this.addContrastButton.Text = "Увеличить контрастность";
            this.addContrastButton.UseVisualStyleBackColor = true;
            this.addContrastButton.Click += new System.EventHandler(this.addContrastButton_Click);
            // 
            // contrastInput
            // 
            this.contrastInput.Enabled = false;
            this.contrastInput.Location = new System.Drawing.Point(552, 6);
            this.contrastInput.Maximum = new decimal(new int[] {
            500,
            0,
            0,
            0});
            this.contrastInput.Minimum = new decimal(new int[] {
            500,
            0,
            0,
            -2147483648});
            this.contrastInput.Name = "contrastInput";
            this.contrastInput.Size = new System.Drawing.Size(54, 20);
            this.contrastInput.TabIndex = 5;
            // 
            // binarizationButton
            // 
            this.binarizationButton.Enabled = false;
            this.binarizationButton.Location = new System.Drawing.Point(612, 5);
            this.binarizationButton.Name = "binarizationButton";
            this.binarizationButton.Size = new System.Drawing.Size(91, 23);
            this.binarizationButton.TabIndex = 6;
            this.binarizationButton.Text = "Бинаризация";
            this.binarizationButton.UseVisualStyleBackColor = true;
            this.binarizationButton.Click += new System.EventHandler(this.binarizationButton_Click);
            // 
            // binarizationInput
            // 
            this.binarizationInput.Enabled = false;
            this.binarizationInput.Location = new System.Drawing.Point(703, 7);
            this.binarizationInput.Maximum = new decimal(new int[] {
            500,
            0,
            0,
            0});
            this.binarizationInput.Minimum = new decimal(new int[] {
            500,
            0,
            0,
            -2147483648});
            this.binarizationInput.Name = "binarizationInput";
            this.binarizationInput.Size = new System.Drawing.Size(50, 20);
            this.binarizationInput.TabIndex = 7;
            // 
            // grayscaleButton
            // 
            this.grayscaleButton.Enabled = false;
            this.grayscaleButton.Location = new System.Drawing.Point(761, 5);
            this.grayscaleButton.Name = "grayscaleButton";
            this.grayscaleButton.Size = new System.Drawing.Size(160, 23);
            this.grayscaleButton.TabIndex = 6;
            this.grayscaleButton.Text = "Переход к оттенкам серого";
            this.grayscaleButton.UseVisualStyleBackColor = true;
            this.grayscaleButton.Click += new System.EventHandler(this.grayscaleButton_Click);
            // 
            // negativeButton
            // 
            this.negativeButton.Enabled = false;
            this.negativeButton.Location = new System.Drawing.Point(927, 6);
            this.negativeButton.Name = "negativeButton";
            this.negativeButton.Size = new System.Drawing.Size(70, 23);
            this.negativeButton.TabIndex = 6;
            this.negativeButton.Text = "Негатив";
            this.negativeButton.UseVisualStyleBackColor = true;
            this.negativeButton.Click += new System.EventHandler(this.negativeButton_Click);
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(152, 9);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(65, 13);
            this.label1.TabIndex = 8;
            this.label1.Text = "Коррекция:";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(1056, 39);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(58, 13);
            this.label2.TabIndex = 8;
            this.label2.Text = "Фильтры:";
            // 
            // uniformButton
            // 
            this.uniformButton.Location = new System.Drawing.Point(498, 34);
            this.uniformButton.Name = "uniformButton";
            this.uniformButton.Size = new System.Drawing.Size(92, 23);
            this.uniformButton.TabIndex = 9;
            this.uniformButton.Text = "Равномерный";
            this.uniformButton.UseVisualStyleBackColor = true;
            this.uniformButton.Click += new System.EventHandler(this.uniformButton_Click);
            // 
            // aquarelButton
            // 
            this.aquarelButton.Location = new System.Drawing.Point(228, 64);
            this.aquarelButton.Name = "aquarelButton";
            this.aquarelButton.Size = new System.Drawing.Size(100, 23);
            this.aquarelButton.TabIndex = 9;
            this.aquarelButton.Text = "Акварелизация";
            this.aquarelButton.UseVisualStyleBackColor = true;
            this.aquarelButton.Click += new System.EventHandler(this.aquarelButton_Click);
            // 
            // progressBar
            // 
            this.progressBar.Location = new System.Drawing.Point(13, 34);
            this.progressBar.Name = "progressBar";
            this.progressBar.Size = new System.Drawing.Size(113, 23);
            this.progressBar.TabIndex = 11;
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(394, 39);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(98, 13);
            this.label3.TabIndex = 8;
            this.label3.Text = "Шумоподавление:";
            // 
            // medianButton
            // 
            this.medianButton.Location = new System.Drawing.Point(596, 34);
            this.medianButton.Name = "medianButton";
            this.medianButton.Size = new System.Drawing.Size(78, 23);
            this.medianButton.TabIndex = 9;
            this.medianButton.Text = "Медианный";
            this.medianButton.UseVisualStyleBackColor = true;
            this.medianButton.Click += new System.EventHandler(this.medianButton_Click);
            // 
            // gaussAntiNoiseButton
            // 
            this.gaussAntiNoiseButton.Location = new System.Drawing.Point(680, 34);
            this.gaussAntiNoiseButton.Name = "gaussAntiNoiseButton";
            this.gaussAntiNoiseButton.Size = new System.Drawing.Size(51, 23);
            this.gaussAntiNoiseButton.TabIndex = 9;
            this.gaussAntiNoiseButton.Text = "Гаусс";
            this.gaussAntiNoiseButton.UseVisualStyleBackColor = true;
            this.gaussAntiNoiseButton.Click += new System.EventHandler(this.gaussAntiNoiseButton_Click);
            // 
            // noiseButton
            // 
            this.noiseButton.Location = new System.Drawing.Point(229, 34);
            this.noiseButton.Name = "noiseButton";
            this.noiseButton.Size = new System.Drawing.Size(77, 23);
            this.noiseButton.TabIndex = 9;
            this.noiseButton.Text = "Случайный";
            this.noiseButton.UseVisualStyleBackColor = true;
            this.noiseButton.Click += new System.EventHandler(this.noiseButton_Click);
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Location = new System.Drawing.Point(152, 39);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(40, 13);
            this.label4.TabIndex = 8;
            this.label4.Text = "Шумы:";
            // 
            // gaussNoiseButton
            // 
            this.gaussNoiseButton.Location = new System.Drawing.Point(312, 34);
            this.gaussNoiseButton.Name = "gaussNoiseButton";
            this.gaussNoiseButton.Size = new System.Drawing.Size(57, 23);
            this.gaussNoiseButton.TabIndex = 9;
            this.gaussNoiseButton.Text = "Гаусс";
            this.gaussNoiseButton.UseVisualStyleBackColor = true;
            this.gaussNoiseButton.Click += new System.EventHandler(this.gaussNoiseButton_Click);
            // 
            // sharpnessButton
            // 
            this.sharpnessButton.Location = new System.Drawing.Point(1120, 35);
            this.sharpnessButton.Name = "sharpnessButton";
            this.sharpnessButton.Size = new System.Drawing.Size(65, 23);
            this.sharpnessButton.TabIndex = 9;
            this.sharpnessButton.Text = "Резкость";
            this.sharpnessButton.UseVisualStyleBackColor = true;
            this.sharpnessButton.Click += new System.EventHandler(this.sharpnessButton_Click);
            // 
            // label5
            // 
            this.label5.AutoSize = true;
            this.label5.Location = new System.Drawing.Point(152, 69);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(58, 13);
            this.label5.TabIndex = 8;
            this.label5.Text = "Эффекты:";
            // 
            // embossingButton
            // 
            this.embossingButton.Location = new System.Drawing.Point(334, 64);
            this.embossingButton.Name = "embossingButton";
            this.embossingButton.Size = new System.Drawing.Size(69, 23);
            this.embossingButton.TabIndex = 9;
            this.embossingButton.Text = "Тиснение";
            this.embossingButton.UseVisualStyleBackColor = true;
            this.embossingButton.Click += new System.EventHandler(this.embossinglButton_Click);
            // 
            // sobelButton
            // 
            this.sobelButton.Location = new System.Drawing.Point(852, 34);
            this.sobelButton.Name = "sobelButton";
            this.sobelButton.Size = new System.Drawing.Size(56, 23);
            this.sobelButton.TabIndex = 9;
            this.sobelButton.Text = "Собель";
            this.sobelButton.UseVisualStyleBackColor = true;
            this.sobelButton.Click += new System.EventHandler(this.sobelButton_Click);
            // 
            // label6
            // 
            this.label6.AutoSize = true;
            this.label6.Location = new System.Drawing.Point(758, 39);
            this.label6.Name = "label6";
            this.label6.Size = new System.Drawing.Size(88, 13);
            this.label6.TabIndex = 8;
            this.label6.Text = "Оконтуривание:";
            // 
            // previtButton
            // 
            this.previtButton.Location = new System.Drawing.Point(914, 34);
            this.previtButton.Name = "previtButton";
            this.previtButton.Size = new System.Drawing.Size(56, 23);
            this.previtButton.TabIndex = 9;
            this.previtButton.Text = "Превит";
            this.previtButton.UseVisualStyleBackColor = true;
            this.previtButton.Click += new System.EventHandler(this.previtButton_Click);
            // 
            // robertsButton
            // 
            this.robertsButton.Location = new System.Drawing.Point(976, 34);
            this.robertsButton.Name = "robertsButton";
            this.robertsButton.Size = new System.Drawing.Size(61, 23);
            this.robertsButton.TabIndex = 9;
            this.robertsButton.Text = "Робертс";
            this.robertsButton.UseVisualStyleBackColor = true;
            this.robertsButton.Click += new System.EventHandler(this.robertsButton_Click);
            // 
            // reloadButton
            // 
            this.reloadButton.AutoSizeMode = System.Windows.Forms.AutoSizeMode.GrowAndShrink;
            this.reloadButton.Enabled = false;
            this.reloadButton.Image = global::ImageCorrection.Properties.Resources.refresh__1_;
            this.reloadButton.Location = new System.Drawing.Point(93, 4);
            this.reloadButton.Name = "reloadButton";
            this.reloadButton.RightToLeft = System.Windows.Forms.RightToLeft.No;
            this.reloadButton.Size = new System.Drawing.Size(33, 23);
            this.reloadButton.TabIndex = 10;
            this.reloadButton.UseVisualStyleBackColor = true;
            this.reloadButton.Click += new System.EventHandler(this.reloadButton_Click);
            // 
            // pictureBox1
            // 
            this.pictureBox1.Location = new System.Drawing.Point(12, 93);
            this.pictureBox1.Name = "pictureBox1";
            this.pictureBox1.Size = new System.Drawing.Size(738, 406);
            this.pictureBox1.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage;
            this.pictureBox1.TabIndex = 0;
            this.pictureBox1.TabStop = false;
            // 
            // porog
            // 
            this.porog.Location = new System.Drawing.Point(854, 62);
            this.porog.Maximum = new decimal(new int[] {
            255,
            0,
            0,
            0});
            this.porog.Name = "porog";
            this.porog.Size = new System.Drawing.Size(50, 20);
            this.porog.TabIndex = 12;
            this.porog.Value = new decimal(new int[] {
            128,
            0,
            0,
            0});
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1331, 501);
            this.Controls.Add(this.porog);
            this.Controls.Add(this.progressBar);
            this.Controls.Add(this.reloadButton);
            this.Controls.Add(this.sharpnessButton);
            this.Controls.Add(this.robertsButton);
            this.Controls.Add(this.previtButton);
            this.Controls.Add(this.sobelButton);
            this.Controls.Add(this.embossingButton);
            this.Controls.Add(this.aquarelButton);
            this.Controls.Add(this.gaussAntiNoiseButton);
            this.Controls.Add(this.medianButton);
            this.Controls.Add(this.gaussNoiseButton);
            this.Controls.Add(this.noiseButton);
            this.Controls.Add(this.uniformButton);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.label5);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.label6);
            this.Controls.Add(this.label4);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.binarizationInput);
            this.Controls.Add(this.negativeButton);
            this.Controls.Add(this.grayscaleButton);
            this.Controls.Add(this.binarizationButton);
            this.Controls.Add(this.contrastInput);
            this.Controls.Add(this.brightnessInput);
            this.Controls.Add(this.addContrastButton);
            this.Controls.Add(this.addBrightnessButton);
            this.Controls.Add(this.loadButton);
            this.Controls.Add(this.chart);
            this.Controls.Add(this.pictureBox1);
            this.Name = "Form1";
            this.Text = "Form1";
            ((System.ComponentModel.ISupportInitialize)(this.chart)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.brightnessInput)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.contrastInput)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.binarizationInput)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.porog)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.PictureBox pictureBox1;
        private System.Windows.Forms.DataVisualization.Charting.Chart chart;
        private System.Windows.Forms.Button loadButton;
        private System.Windows.Forms.OpenFileDialog openFileDialog1;
        private System.Windows.Forms.Button addBrightnessButton;
        private System.Windows.Forms.NumericUpDown brightnessInput;
        private System.Windows.Forms.Button addContrastButton;
        private System.Windows.Forms.NumericUpDown contrastInput;
        private System.Windows.Forms.Button binarizationButton;
        private System.Windows.Forms.NumericUpDown binarizationInput;
        private System.Windows.Forms.Button grayscaleButton;
        private System.Windows.Forms.Button negativeButton;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Button uniformButton;
        private System.Windows.Forms.Button aquarelButton;
        private System.Windows.Forms.Button reloadButton;
        private System.Windows.Forms.ProgressBar progressBar;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.Button medianButton;
        private System.Windows.Forms.Button gaussAntiNoiseButton;
        private System.Windows.Forms.Button noiseButton;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.Button gaussNoiseButton;
        private System.Windows.Forms.Button sharpnessButton;
        private System.Windows.Forms.Label label5;
        private System.Windows.Forms.Button embossingButton;
        private System.Windows.Forms.Button sobelButton;
        private System.Windows.Forms.Label label6;
        private System.Windows.Forms.Button previtButton;
        private System.Windows.Forms.Button robertsButton;
        private System.Windows.Forms.NumericUpDown porog;
    }
}

