using System;

namespace ImageCorrection
{
    public class Pixel
    {
        public static Pixel Empty => new Pixel(0, 0, 0, 0);

        public byte R;
        public byte G;
        public byte B;
        public byte A;

        public double Brightness => Math.Round(0.299 * R + 0.5876 * G + 0.114 * G);

        public Pixel(byte r, byte g, byte b, byte a = 255)
        {
            R = r;
            G = g;
            B = b;
            A = a;
        }

        public static Pixel Create(byte r, byte g, byte b, byte a = 255) => new Pixel(r, g, b, a);
        public static Pixel From(Pixel p) => new Pixel(p.R, p.G, p.B, p.A);
    }
}
