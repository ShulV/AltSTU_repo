using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Diagnostics;
using System.Drawing;
using System.Drawing.Imaging;
using System.IO;
using System.Linq;
using System.Runtime.InteropServices;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace ImageCorrection
{
    public partial class Form1 : Form
    {
        private string _fileName;
        private Bitmap _bmp;
        private PixelCollection _pixels;
        private List<Control> managementControls;
        private Random _rand = new Random();
        private Loading loading => new Loading();

        public Form1()
        {
            InitializeComponent();
            managementControls = new List<Control>()
            {
                addBrightnessButton,
                brightnessInput,
                addContrastButton,
                contrastInput,
                binarizationButton,
                binarizationInput,
                grayscaleButton,
                negativeButton,
                reloadButton,
                noiseButton,
                gaussNoiseButton,
                uniformButton,
                medianButton,
                gaussAntiNoiseButton,
                sobelButton,
                previtButton,
                robertsButton,
                sharpnessButton,
                aquarelButton,
                embossingButton
            };
            managementControls.ForEach(control => control.Enabled = false);


            Loading.progressBar = progressBar;
        }

        private void loadButton_Click(object sender, EventArgs e)
        {
            using (loading)
            {
                var result = openFileDialog1.ShowDialog();
                if (result == DialogResult.OK)
                {
                    _fileName = openFileDialog1.FileName;
                    LoadImage();
                    managementControls.ForEach(control => control.Enabled = true);
                } 
            }
        }

        /// <summary>
        /// Загрузить картинку
        /// </summary>
        private void LoadImage()
        {
            _bmp = new Bitmap(_fileName);
            var pixels = _bmp.GetPixels();
            _pixels = pixels;
            UpdateImage(_pixels);
        }

        /// <summary>
        /// Установить пискели
        /// </summary>
        private void UpdateImage(PixelCollection pixels)
        {
            _pixels = pixels;

            if (pictureBox1.Image != null)
            {
                pictureBox1.Image.Dispose();
            }

            pictureBox1.Image = pixels.Create();
            pictureBox1.Refresh();

            UpdateChart(pixels);
        }

        /// <summary>
        /// Обновить график
        /// </summary>
        private void UpdateChart(PixelCollection pixels)
        {
            var dict = new Dictionary<int, int>(256);

            foreach (var pixel in pixels)
            {
                var brightness = (int)pixel.Brightness;
                if (!dict.ContainsKey(brightness))
                {
                    dict.Add(brightness, 0);
                }

                dict[brightness]++;
            }

            chart.Series[0].Points.Clear();

            foreach (var item in dict)
            {
                chart.Series[0].Points.AddXY(item.Key, item.Value % 5000);
            }

            chart.Update();
        }

        /// <summary>
        /// Перезагрузить картинку
        /// </summary>
        private void reloadButton_Click(object sender, EventArgs e)
        {
            using (loading)
            {
                LoadImage(); 
            }
        }

        /// <summary>
        /// Увеличить яркость
        /// </summary>
        private void addBrightnessButton_Click(object sender, EventArgs e)
        {
            using (loading)
            {
                var coefficient = (int)brightnessInput.Value;

                foreach (var pixel in _pixels)
                {
                    pixel.R = Normalize(pixel.R + coefficient);
                    pixel.G = Normalize(pixel.G + coefficient);
                    pixel.B = Normalize(pixel.B + coefficient);
                }

                UpdateImage(_pixels); 
            }
        }

        /// <summary>
        /// Увеличить контрастность
        /// </summary>
        private void addContrastButton_Click(object sender, EventArgs e)
        {
            using (loading)
            {
                var coefficient = (int)contrastInput.Value;

                var averageGray = 0d;

                foreach (var pixel in _pixels)
                {
                    averageGray += pixel.R * 0.2126 + pixel.G * 0.7152 + pixel.B * 0.0722;
                }

                averageGray /= _pixels.Count / 4d;

                foreach (var pixel in _pixels)
                {
                    pixel.R = Normalize(pixel.R + Math.Round((coefficient * (pixel.R - averageGray) + averageGray) / 255));
                    pixel.G = Normalize(pixel.G + Math.Round((coefficient * (pixel.G - averageGray) + averageGray) / 255));
                    pixel.B = Normalize(pixel.B + Math.Round((coefficient * (pixel.B - averageGray) + averageGray) / 255));
                }

                UpdateImage(_pixels); 
            }
        }

        /// <summary>
        /// Бинаризация
        /// </summary>
        private void binarizationButton_Click(object sender, EventArgs e)
        {
            using (loading)
            {
                var coefficient = (int)binarizationInput.Value;

                for (var i = 0; i < _pixels.Count; i++)
                {
                    var oldPixel = _pixels[i];
                    var total = oldPixel.R + oldPixel.G + oldPixel.B;
                    _pixels[i] = total > coefficient ? Pixel.Create(255, 255, 255) : Pixel.Create(0, 0, 0);
                }

                UpdateImage(_pixels); 
            }
        }

        /// <summary>
        /// Переход к оттенкам серого
        /// </summary>
        private void grayscaleButton_Click(object sender, EventArgs e)
        {
            using (loading)
            {
                for (var i = 0; i < _pixels.Count; i++)
                {
                    var oldPixel = _pixels[i];
                    var avg = Normalize((oldPixel.R + oldPixel.G + oldPixel.B) / 3d);
                    _pixels[i] = Pixel.Create(avg, avg, avg);
                }

                UpdateImage(_pixels); 
            }
        }

        /// <summary>
        /// Негатив
        /// </summary>
        private void negativeButton_Click(object sender, EventArgs e)
        {
            using (loading)
            {
                for (var i = 0; i < _pixels.Count; i++)
                {
                    var oldPixel = _pixels[i];
                    _pixels[i] = Pixel.Create((byte)(255 - oldPixel.R), (byte)(255 - oldPixel.G), (byte)(255 - oldPixel.B));
                }

                UpdateImage(_pixels); 
            }
        }

        private void ApplyFilter(double[] filter, int offset = 0, bool redraw = true)
        {
            var width = _bmp.Width;
            var height = _bmp.Height;

            var size = (int)Math.Sqrt(filter.Length);
            var half = (int)Math.Floor(size / 2d);

            var inputData = _pixels;

            var output = new PixelCollection(_pixels.Width, _pixels.Height, _pixels.Count);
            output.AddRange(Enumerable.Range(0, _pixels.Count).Select(x => Pixel.Empty));

            // Go through image pixels
            for (var j = 0; j < _bmp.Height; j++)
            {
                for (var i = 0; i < _bmp.Width; i++)
                {
                    double r = 0, g = 0, b = 0;

                    // Go through filter
                    for (var filterY = 0; filterY < size; filterY++)
                    {
                        for (var filterX = 0; filterX < size; filterX++)
                        {
                            var weight = filter[filterY * size + filterX];

                            // Border crossing check
                            var neighborY = Math.Min(
                              height - 1, Math.Max(0, j + filterY - half)
                            );
                            var neighborX = Math.Min(
                              width - 1, Math.Max(0, i + filterX - half)
                            );

                            // Sum rgba from original image
                            var inputIndex = (neighborY * width + neighborX);
                            r += inputData[inputIndex].R * weight;
                            g += inputData[inputIndex].G * weight;
                            b += inputData[inputIndex].B * weight;
                        }
                    }

                    // Set new rgba
                    var outputIndex = (j * width + i);
                    output[outputIndex] = Pixel.Create(Normalize(r + offset), Normalize(g + offset), Normalize(b + offset));
                }
            }

            if (redraw)
            {
                UpdateImage(output);
            }
            else
            {
                _pixels = output;
            }
        }

        private void MedianAverage(int n)
        {
            var output = new PixelCollection(_pixels.Width, _pixels.Height, _pixels.Count);
            output.AddRange(Enumerable.Range(0, _pixels.Count).Select(x => Pixel.Empty));

            Parallel.For(0, _pixels.Width, i =>
            {
                //Parallel.For(0, _pixels.Height, j =>
                for(var j = 0; j < _pixels.Height; j++)
                {
                    var minX = i - n;
                    var maxX = i + n;
                    var minY = j - n;
                    var maxY = j + n;

                    var pixels = new List<Pixel>();
                    for (int x = minX; x <= maxX; x++)
                    {
                        for (int y = minY; y <= maxY; y++)
                        {
                            if (x < 0 || x >= _pixels.Width || y < 0 || y >= _pixels.Height)
                            {
                                continue;
                            }

                            pixels.Add(_pixels.Get(x, y));
                        }
                    }

                    var average = pixels.OrderBy(x => x.Brightness).Skip(pixels.Count / 2).First();
                    output[j * _pixels.Width + i] = Pixel.From(average);
                }/*);*/
            });

            UpdateImage(output);
        }

        private void aquarelButton_Click(object sender, EventArgs e)
        {
            using (loading)
            {
                // Медианное усреднение
                MedianAverage(5);

                // Повышение резкости
                var k = 2d;
                ApplyFilter(new[]
                {
                    -k/8, -k/8, -k/8,
                    -k/8,  k+1, -k/8,
                    -k/8, -k/8, -k/8
                }); 
            }
        }

        /// <summary>
        /// Случайный шум
        /// </summary>
        private void noiseButton_Click(object sender, EventArgs e)
        {
            using (loading)
            {
                foreach (var pixel in _pixels)
                {
                    if (_rand.NextDouble() > 0.95)
                    {
                        pixel.R = pixel.G = pixel.B = 255;
                    }
                }

                UpdateImage(_pixels);
            }
        }

        /// <summary>
        /// Шум Гаусса
        /// </summary>
        private void gaussNoiseButton_Click(object sender, EventArgs e)
        {
            using (loading)
            {
                var power = 50;
                foreach (var pixel in _pixels)
                {
                    var noise = ((_rand.NextDouble() + _rand.NextDouble() - 1) * power);

                    pixel.R = Normalize(pixel.R + noise); 
                    pixel.G = Normalize(pixel.G + noise); 
                    pixel.B = Normalize(pixel.B + noise); 
                }

                UpdateImage(_pixels);
            }

        }

        /// <summary>
        /// Равномерное шупомодавление
        /// </summary>
        private void uniformButton_Click(object sender, EventArgs e)
        {
            using (loading)
            {
                ApplyFilter(new[]
                {
                    1 / 9d, 1 / 9d, 1 / 9d,
                    1 / 9d, 1 / 9d, 1 / 9d,
                    1 / 9d, 1 / 9d, 1 / 9d,
                });
            }
        }

        /// <summary>
        /// Медианное шумпоподавление
        /// </summary>
        private void medianButton_Click(object sender, EventArgs e)
        {
            using (loading)
            {
                // Медианное усреднение
                MedianAverage(3);
            }
        }

        /// <summary>
        /// Шумоподавление Гаусса
        /// </summary>
        private void gaussAntiNoiseButton_Click(object sender, EventArgs e)
        {
            using (loading)
            {
                ApplyFilter(new[]
                {
                    0.0001, 0.0020, 0.0055, 0.0020, 0.0001,
                    0.0020, 0.0422, 0.1171, 0.0422, 0.0020,
                    0.0055, 0.1171, 0.3248, 0.1171, 0.0055,
                    0.0020, 0.0422, 0.1171, 0.0422, 0.0020,
                    0.0001, 0.0020, 0.0055, 0.0020, 0.0001,
                });
            }
        }


        /// <summary>
        /// Резкость
        /// </summary>
        private void sharpnessButton_Click(object sender, EventArgs e)
        {
            using (loading)
            {
                var k = 2d;
                ApplyFilter(new[]
                {
                    -k/8, -k/8, -k/8,
                    -k/8,  k+1, -k/8,
                    -k/8, -k/8, -k/8
                });
            }
        }

        /// <summary>
        /// Тиснение
        /// </summary>
        private void embossinglButton_Click(object sender, EventArgs e)
        {
            using (loading)
            {
                ApplyFilter(new double[]
                {
                    1, 0, 0,
                    0, 0, 0,
                    0, 0, -1
                }, 128);
            }
        }

        /// <summary>
        /// Оконтуривание по Собелю
        /// </summary>
        private void sobelButton_Click(object sender, EventArgs e)
        {
            using (loading)
            {
                ApplyFilter(new double[]
                {
                    1, 2, 1,
                    0, 0, 0,
                    -1, -2, -1
                }, redraw: false);

                PostProcessing();
            }
        }

        /// <summary>
        /// Оконтуривание по Превиту
        /// </summary>
        private void previtButton_Click(object sender, EventArgs e)
        {
            using (loading)
            {
                ApplyFilter(new double[]
                {
                    1, 1, 1,
                    0, 0, 0,
                    -1, -1, -1
                }, redraw: false);

                PostProcessing();
            }
        }

        /// <summary>
        /// Оконтуривание по Робертсу
        /// </summary>
        private void robertsButton_Click(object sender, EventArgs e)
        {
            using (loading)
            {
                ApplyFilter(new double[]
                {
                    -1, 0,
                     0, 1,
                     //0, -1,
                     //1, 0
                }, redraw: false);

                PostProcessing();
            }
        }

        private void PostProcessing()
        {
            var offset = (int)porog.Value;

            foreach (var pixel in _pixels)
            {
                if (pixel.R <= offset && pixel.G <= offset && pixel.B <= offset)
                {
                    pixel.R = pixel.G = pixel.B = 255;
                }
                else
                {
                    pixel.R = pixel.G = pixel.B = 0;
                }
            }

            UpdateImage(_pixels);
        }

        private byte Normalize(double value)
        {
            if (value > 255) return 255;
            if (value < 0) return 0;
            return (byte)value;
        }
    }


    internal class Loading : IDisposable
    {
        public static ProgressBar progressBar;

        private bool cancel;
        private Timer timer;

        public Loading()
        {
            cancel = false;
            progressBar.Value = progressBar.Minimum;

            timer = new Timer();
            timer.Interval = 100;
            timer.Tick += (s, e) =>
            {
                if (cancel)
                {
                    progressBar.Value = progressBar.Maximum;
                    timer.Enabled = false;
                    timer.Dispose();
                }
                else if (progressBar.Value < progressBar.Maximum * 0.9)
                {
                    progressBar.PerformStep();
                }
            };
            timer.Enabled = true;
        }

        public void Dispose()
        {
            cancel = true;
        }
    }
}
