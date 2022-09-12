package com.example.cg1.models;

import javafx.animation.KeyFrame;
import javafx.animation.KeyValue;
import javafx.animation.Timeline;
import javafx.beans.value.WritableValue;
import javafx.geometry.Bounds;
import javafx.geometry.Point3D;
import javafx.scene.canvas.Canvas;
import javafx.util.Duration;

public class CustomPoint3D {
    private double x;
    private double y;
    private double z;

    public double getX() {
        return x;
    }
    public double getY() {
        return y;
    }
    public double getZ() {
        return z;
    }

    public void setX(double x) {
        this.x = x;
    }

    public void setY(double y) {
        this.y = y;
    }

    public void setZ(double z) {
        this.z = z;
    }

    public CustomPoint3D(double x, double y, double z) {
        this.x = x;
        this.y = y;
        this.z = z;
    }

    public static final int n = 4; //размер матрицы Аффинного преобразования (3D)

    //получить вектор координат точки для Аффинного преобразования (3D)
    private double[] getVectorForAffineTransformation() {
        double[] vector = new double[4];
        vector[0] = getX();
        vector[1] = getY();
        vector[2] = getZ();
        vector[3] = 1.0;
        return vector;
    }

    //сделать Аффинное преобразование точки (3D)
    public void doAffineTransformation(double[][] affineTransformationMatrix) {
        double[] vector = getVectorForAffineTransformation();
        double[] res = new double[n];
        for (int i = 0; i < n; i++)
        {
            res[i] = 0;
            for (int j = 0; j < n; j++)
                res[i] += vector[j] * affineTransformationMatrix[j][i];
        }
        this.x = res[0];
        this.y = res[1];
        this.z = res[2];
    }

}
