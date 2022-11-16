using System;
using System.Collections.Generic;
using System.Drawing;
using System.Drawing.Imaging;
using System.Linq;
using System.Runtime.InteropServices;
using System.Text;
using System.Threading.Tasks;

namespace ImageCorrection
{
    public static class BitmapExtensions
    {
        private const int pixelSize = 4;

        public static PixelCollection GetPixels(this Bitmap bmp)
        {
            BitmapData sourceData = bmp.LockBits(new Rectangle(Point.Empty, bmp.Size), ImageLockMode.ReadOnly, PixelFormat.Format32bppArgb);

            byte[] pixelBuffer = new byte[sourceData.Stride * sourceData.Height];

            Marshal.Copy(sourceData.Scan0, pixelBuffer, 0, pixelBuffer.Length);

            bmp.UnlockBits(sourceData);

            var result = new PixelCollection(bmp.Width, bmp.Height, pixelBuffer.Length / pixelSize);

            for (int i = 0; i < pixelBuffer.Length; i += pixelSize)
            {
                result.Add(Pixel.Create(pixelBuffer[i + 2], pixelBuffer[i + 1], pixelBuffer[i], pixelBuffer[i + 3]));
            }

            return result;
        }

        public static Bitmap Create(this PixelCollection pixels)
        {
            var bmp = new Bitmap(pixels.Width, pixels.Height);

            BitmapData bData = bmp.LockBits(new Rectangle(Point.Empty, bmp.Size), ImageLockMode.ReadWrite, PixelFormat.Format32bppArgb);

            int size = bData.Stride * bData.Height;

            byte[] data = new byte[size];

            //Marshal.Copy(bData.Scan0, data, 0, size);

            var i = 0;
            foreach (var pixel in pixels)
            {
                data[i + 2] = pixel.R;
                data[i + 1] = pixel.G;
                data[i] = pixel.B;
                data[i + 3] = pixel.A;
                i += pixelSize;
            }

            Marshal.Copy(data, 0, bData.Scan0, data.Length);

            bmp.UnlockBits(bData);

            return bmp;
        }
    }
}
