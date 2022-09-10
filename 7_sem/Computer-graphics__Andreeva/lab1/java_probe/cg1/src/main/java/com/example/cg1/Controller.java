package com.example.cg1;

import com.example.cg1.models.AffineTransformationMatrix3D;
import com.example.cg1.models.Line3D;
import com.example.cg1.models.Object3D;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.geometry.Point3D;
import javafx.scene.canvas.Canvas;
import javafx.scene.canvas.GraphicsContext;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.effect.BlendMode;
import javafx.scene.paint.Color;
import javafx.scene.shape.Line;

import java.io.*;
import java.net.URISyntaxException;
import java.net.URL;
import java.util.ArrayList;
import java.util.List;

import static java.lang.Double.parseDouble;

public class Controller {
    @FXML
    private Canvas canvasPlot;

    private final Object3D object3D = new Object3D(); //проволочная фигура
    private GraphicsContext gc;

    public Controller() throws URISyntaxException {
        object3D.readLinesFromFile(""); //TODO заменить абсолютный путь
    }

    //FMXL конструктор
    @FXML
    public void initialize() {
        gc = canvasPlot.getGraphicsContext2D();
        gc.translate(canvasPlot.getWidth() / 2, canvasPlot.getHeight() / 2);

    }
    //нарисовать линию
    private void drawLine(GraphicsContext gc, double xStart, double yStart, double xEnd, double yEnd) {
        gc.setLineWidth(1.0);
        gc.setStroke(Color.BLUE);

//        //отражение координат, т.к. направления осей координат на canvas в java нестандартное
//        yStart *= -1;
//        yEnd *= -1;

        gc.strokeLine(xStart, yStart, xEnd, yEnd);

    }

    //нарисовать линию
    private void drawLine(GraphicsContext gc, Line3D line) {
        gc.setLineWidth(1.0);
        gc.setStroke(Color.BLUE);
        double xStart = line.getStartPoint().getX();
        double yStart = line.getStartPoint().getY();
        double xEnd = line.getEndPoint().getX();
        double yEnd = line.getEndPoint().getY();

//        //отражение координат, т.к. направления осей координат на canvas в java нестандартное
//        yStart *= -1;
//        yEnd *= -1;

        gc.strokeLine(xStart, yStart, xEnd, yEnd);
    }

    //очистить холст
    public void clearCanvas(GraphicsContext gc) {

        gc.clearRect(-canvasPlot.getWidth() / 2,
                -canvasPlot.getHeight() / 2,
                canvasPlot.getWidth(),
                canvasPlot.getHeight());
    }

    //отрисовать оси координат
    public void drawAxes(GraphicsContext gc) {
        gc.setLineWidth(2.0);
        gc.setStroke(Color.GREEN);

        gc.strokeLine(0, 0, 500, 0);// Ox
        gc.strokeLine(0, 0, 0, -500);// Oy
        gc.strokeLine(0, 0, -500, 500);// Oz

    }

    //отрисовать все элементы (очистка, оси, фигура)
    public void drawAll() {
        clearCanvas(gc);
        drawAxes(gc);
        drawFigure(gc);
    }

    //отрисовать проволочную фигуру
    public void drawFigure(GraphicsContext gc) {
        for (Line3D line: object3D.getLineList()
             ) {
            //проецирование
//            a = edge.Item1.X - float.Parse((edge.Item1.Z * 0.5 * Math.Cos(Math.PI / 4)).ToString());
//            b = -edge.Item1.Y + float.Parse((edge.Item1.Z * 0.5 * Math.Cos(Math.PI / 4)).ToString());
//            c = edge.Item2.X - float.Parse((edge.Item2.Z * 0.5 * Math.Cos(Math.PI / 4)).ToString());
//            d = -edge.Item2.Y + float.Parse((edge.Item2.Z * 0.5 * Math.Cos(Math.PI / 4)).ToString());
            double startX = line.getStartPoint().getX() - line.getStartPoint().getZ() * 0.5 * Math.cos(Math.PI / 4);
            double startY = -line.getStartPoint().getY() + line.getStartPoint().getZ() * 0.5 * Math.cos(Math.PI / 4);
            double endX = line.getEndPoint().getX() - line.getEndPoint().getZ() * 0.5 * Math.cos(Math.PI / 4);
            double endY = -line.getEndPoint().getY() + line.getEndPoint().getZ() * 0.5 * Math.cos(Math.PI / 4);

            
            drawLine(gc, startX, startY, endX, endY);
        }
    }

    //обработчик кнопки смещения по oX (увеличение)
    public void onBtnMovingIncreaseXClick(ActionEvent actionEvent) throws URISyntaxException {
        object3D.doAffineTransformation(AffineTransformationMatrix3D.getMovingMatrix(10.0, 0.0, 0.0));
        drawAll();
    }

    //обработчик кнопки смещения по oX (уменьшение)
    public void onBtnMovingReduceXClick(ActionEvent actionEvent) throws URISyntaxException {
        object3D.doAffineTransformation(AffineTransformationMatrix3D.getMovingMatrix(-10.0, 0.0, 0.0));
        drawAll();
    }

    //обработчик кнопки смещения по oY (увеличение)
    public void onBtnMovingIncreaseYClick(ActionEvent actionEvent) throws URISyntaxException {
        object3D.doAffineTransformation(AffineTransformationMatrix3D.getMovingMatrix(0.0, 10.0, 0.0));
        drawAll();
    }

    //обработчик кнопки смещения по oY (уменьшение)
    public void onBtnMovingReduceYClick(ActionEvent actionEvent) throws URISyntaxException {
        object3D.doAffineTransformation(AffineTransformationMatrix3D.getMovingMatrix(0.0, -10.0, 0.0));
        drawAll();
    }

    //обработчик кнопки смещения по oZ (увеличение)
    public void onBtnMovingIncreaseZClick(ActionEvent actionEvent) throws URISyntaxException {
        object3D.doAffineTransformation(AffineTransformationMatrix3D.getMovingMatrix(0.0, 0.0, 10.0));
        drawAll();
    }

    //обработчик кнопки смещения по oZ (уменьшение)
    public void onBtnMovingReduceZClick(ActionEvent actionEvent) throws URISyntaxException {
        object3D.doAffineTransformation(AffineTransformationMatrix3D.getMovingMatrix(0.0, 0.0, -10.0));
        drawAll();
    }

    //обработчик кнопки поворота вокруг oX (увеличение)
    public void onBtnRotationIncreaseXClick(ActionEvent actionEvent) {
        object3D.doAffineTransformation(AffineTransformationMatrix3D.getXRotationMatrix(Math.toRadians(10)));
        drawAll();
    }

    //обработчик кнопки поворота вокруг oX (уменьшение)
    public void onBtnRotationReduceXClick(ActionEvent actionEvent) {
        object3D.doAffineTransformation(AffineTransformationMatrix3D.getXRotationMatrix(Math.toRadians(-10)));
        drawAll();
    }

    //обработчик кнопки поворота вокруг oY (увеличение)
    public void onBtnRotationIncreaseYClick(ActionEvent actionEvent) {
        object3D.doAffineTransformation(AffineTransformationMatrix3D.getYRotationMatrix(Math.toRadians(10)));
        drawAll();
    }

    //обработчик кнопки поворота вокруг oY (уменьшение)
    public void onBtnRotationReduceYClick(ActionEvent actionEvent) {
        object3D.doAffineTransformation(AffineTransformationMatrix3D.getYRotationMatrix(Math.toRadians(-10)));
        drawAll();
    }

    //обработчик кнопки поворота вокруг oZ (увеличение)
    public void onBtnRotationIncreaseZClick(ActionEvent actionEvent) {
        object3D.doAffineTransformation(AffineTransformationMatrix3D.getZRotationMatrix(Math.toRadians(10)));
        drawAll();
    }

    //обработчик кнопки поворота вокруг oZ (уменьшение)
    public void onBtnRotationReduceZClick(ActionEvent actionEvent) {
        object3D.doAffineTransformation(AffineTransformationMatrix3D.getZRotationMatrix(Math.toRadians(-10)));
        drawAll();
    }

    //обработчик кнопки масштабирования относительно oX (увеличение в 1.5 раза)
    public void onBtnScalingIncreaseXClick(ActionEvent actionEvent) throws Exception {
        object3D.doAffineTransformation(AffineTransformationMatrix3D.getScalingMatrix(
                (double) 3/2, 1, 1));
        drawAll();
    }

    //обработчик кнопки масштабирования относительно oX (уменьшение в 1.5 раза)
    public void onBtnScalingReduceXClick(ActionEvent actionEvent) throws Exception {
        object3D.doAffineTransformation(AffineTransformationMatrix3D.getScalingMatrix(
                (double) 2/3, 1, 1));
        drawAll();
    }

    //обработчик кнопки масштабирования относительно oY (увеличение в 1.5 раза)
    public void onBtnScalingIncreaseYClick(ActionEvent actionEvent) throws Exception {
        object3D.doAffineTransformation(AffineTransformationMatrix3D.getScalingMatrix(
                1, (double) 3/2, 1));
        drawAll();
    }

    //обработчик кнопки масштабирования относительно oY (уменьшение в 1.5 раза)
    public void onBtnScalingReduceYClick(ActionEvent actionEvent) throws Exception {
        object3D.doAffineTransformation(AffineTransformationMatrix3D.getScalingMatrix(
                1, (double) 2/3, 1));
        drawAll();
    }

    //обработчик кнопки масштабирования относительно oZ (увеличение в 1.5 раза)
    public void onBtnScalingIncreaseZClick(ActionEvent actionEvent) throws Exception {
        object3D.doAffineTransformation(AffineTransformationMatrix3D.getScalingMatrix(
                1, 1, (double) 3/2));
        drawAll();
    }

    //обработчик кнопки масштабирования относительно oZ (уменьшение в 1.5 раза)
    public void onBtnScalingReduceZClick(ActionEvent actionEvent) throws Exception {
        object3D.doAffineTransformation(AffineTransformationMatrix3D.getScalingMatrix(
                1, 1, (double) 2/3));
        drawAll();
    }

}