package com.example.cg1.models;

import static java.lang.Math.*;

//Аффинная матрица преобразования для трехмерного случая
abstract public class AffineTransformationMatrix3D {

    //вывести матрицу в консоль (тестовый метод)
    private static void printMatrix(double[][] matrix) {
        for (double[] line: matrix
             ) {
            for (double elem: line
                 ) {
                System.out.print(elem + " ");
            }
            System.out.println();
        }
    }

    //получить нулевую матрицу 4x4 (тестовый метод)
    public static double[][] getZeroMatrix()
    {
        return new double[][]{
                {0.0, 0.0, 0.0, 0.0},
                {0.0, 0.0, 0.0, 0.0},
                {0.0, 0.0, 0.0, 0.0},
                {0.0, 0.0, 0.0, 0.0}};
    }

    //получить матрицу перемещения 4x4
    public static double[][] getMovingMatrix(double toX, double toY, double toZ) {
        return new double[][]{
                {1.0, 0.0, 0.0, 0.0},
                {0.0, 1.0, 0.0, 0.0},
                {0.0, 0.0, 1.0, 0.0},
                {toX, toY, toZ, 1.0}};
    }

    //получить матрицу поворота 4x4 вокруг оси X
    public static double[][] getXRotationMatrix(double angle) {
        return new double[][]{
                {1.0, 0.0, 0.0, 0.0},
                {0.0, cos(angle), sin(angle), 0.0},
                {0.0, -sin(angle), cos(angle), 0.0},
                {0.0, 0.0, 0.0, 1.0}};
    }

    //получить матрицу поворота 4x4 вокруг оси Y
    public static double[][] getYRotationMatrix(double angle) {
        return new double[][]{
                {cos(angle), 0.0, -sin(angle), 0.0},
                {0.0, 1.0, 0.0, 0.0},
                {sin(angle), 0.0, cos(angle), 0.0},
                {0.0, 0.0, 0.0, 1.0}};
    }

    //получить матрицу поворота 4x4 вокруг оси Z
    public static double[][] getZRotationMatrix(double angle) {
        return new double[][]{
                {cos(angle), sin(angle), 0.0, 0.0},
                {-sin(angle), cos(angle), 0.0, 0.0},
                {0.0, 0.0, 1.0, 0.0},
                {0.0, 0.0, 0.0, 1.0}};
    }

    //получить матрицу масштабирования 4x4
    public static double[][] getScalingMatrix(double forX, double forY, double forZ) throws Exception {
        if (forX <= 0 || forY <=0 || forZ <= 0) {
            throw new Exception("scale factor cannot be less than zero");
        }
        return new double[][]{
                {forX, 0.0, 0.0, 0.0},
                {0.0, forY, 0.0, 0.0},
                {0.0, 0.0, forZ, 0.0},
                {0.0, 0.0, 0.0, 1.0}};
    }

    //получить матрицу отзеркаливания 4x4
    public static double[][] getReflectionMatrix(int yoz, int zox, int xoy) throws Exception {
        if (abs(yoz) != 1 || abs(zox) != 1 || abs(xoy) != 1) {
            throw new Exception("method parameter is wrong");
        }
        return new double[][]{
                {yoz, 0.0, 0.0, 0.0},
                {0.0, zox, 0.0, 0.0},
                {0.0, 0.0, xoy, 0.0},
                {0.0, 0.0, 0.0, 1.0}};
    }
}
