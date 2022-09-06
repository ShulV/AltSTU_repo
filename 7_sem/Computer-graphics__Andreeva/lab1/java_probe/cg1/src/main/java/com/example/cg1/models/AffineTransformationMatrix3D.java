package com.example.cg1.models;

//Аффинная матрица преобразования для трехмерного случая
abstract public class AffineTransformationMatrix3D {

    //получить нулевую матрицу 4x4
    public static double[][] getZeroMatrix()
    {
        double[][] matrix = new double[4][4];
        for (int i = 0; i < 4; i++)
        {
            for (int j = 0; j < 4; j++)
                matrix[i][j] = 0.0F;
        }
        return matrix;
    }

    //получить матрицу перемещения 4x4
    public static double[][] getMovingMatrix(double toX, double toY, double toZ) {
        double[][] matrix = getZeroMatrix();
        matrix[0][0] = 1.0F;
        matrix[1][1] = 1.0F;
        matrix[2][2] = 1.0F;
        matrix[3][0] = toX;
        matrix[3][1] = toY;
        matrix[3][2] = toZ;
        matrix[3][3] = 1.0F;
        return matrix;
    }
}
