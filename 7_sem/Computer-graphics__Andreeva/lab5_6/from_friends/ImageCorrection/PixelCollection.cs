using System.Collections.Generic;

namespace ImageCorrection
{
    public class PixelCollection : List<Pixel>
    {
        public int Width { get; }
        public int Height { get; }

        public PixelCollection(int width, int height, int capacity = 0)
            : base(capacity)
        {
            Width = width;
            Height = height;
        }

        public Pixel Get(int i, int j) => this[Width * j + i];
    }
}
