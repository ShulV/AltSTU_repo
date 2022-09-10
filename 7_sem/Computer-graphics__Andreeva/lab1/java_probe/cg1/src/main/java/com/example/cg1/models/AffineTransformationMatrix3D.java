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
        matrix[0][0] = 1;
        matrix[1][1] = 1;
        matrix[2][2] = 1;
        matrix[3][0] = toX;
        matrix[3][1] = toY;
        matrix[3][2] = toZ;
        matrix[3][3] = 1;
        return matrix;
    }

    //получить матрицу поворота 4x4 вокруг оси X
    public static double[][] getXRotationMatrix(double angle) {
        double[][] matrix = getZeroMatrix();
        matrix[0][0] = 1;
        matrix[1][1] = Math.cos(angle);
        matrix[1][2] = Math.sin(angle);
        matrix[2][1] = -Math.sin(angle);
        matrix[2][2] = Math.cos(angle);
        matrix[3][3] = 1;
        return matrix;
    }

    //получить матрицу поворота 4x4 вокруг оси Y
    public static double[][] getYRotationMatrix(double angle) {
        double[][] matrix = getZeroMatrix();
        matrix[0][0] = Math.cos(angle);
        matrix[0][2] = -Math.sin(angle);
        matrix[1][1] = 1;
        matrix[2][0] = Math.sin(angle);
        matrix[2][2] = Math.cos(angle);
        matrix[3][3] = 1;
        return matrix;
    }

    //получить матрицу поворота 4x4 вокруг оси Z
    public static double[][] getZRotationMatrix(double angle) {
        double[][] matrix = getZeroMatrix();
        matrix[0][0] = Math.cos(angle);
        matrix[0][1] = Math.sin(angle);
        matrix[1][0] = -Math.sin(angle);
        matrix[1][1] = Math.cos(angle);
        matrix[2][2] = 1;
        matrix[3][3] = 1;
        return matrix;
    }

    //получить матрицу масштабирования 4x4
    public static double[][] getScalingMatrix(double forX, double forY, double forZ) throws Exception {
        if (forX <= 0 || forY <=0 || forZ <= 0) {
            throw new Exception("scale factor cannot be less than zero");
        }
        double[][] matrix = getZeroMatrix();
        matrix[0][0] = forX;
        matrix[1][1] = forY;
        matrix[2][2] = forZ;
        matrix[3][3] = 1;
        return matrix;
    }
}
