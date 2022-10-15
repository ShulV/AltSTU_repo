package com.example.cg1;

import com.example.cg1.models.AffineTransformationMatrix3D;
import com.example.cg1.models.Line3D;
import com.example.cg1.models.Object3D;
import javafx.animation.AnimationTimer;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.canvas.Canvas;
import javafx.scene.canvas.GraphicsContext;
import javafx.scene.paint.Color;
import java.net.URISyntaxException;

import static java.lang.Math.*;

public class Controller {
    @FXML
    private Canvas canvasPlot;

    private final Object3D object3D = new Object3D(); //проволочная фигура
    private GraphicsContext gc;

    public Controller() throws URISyntaxException {
        object3D.readLinesFromFile("lines.txt");
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
            //проецирование (комнатая проекция (45 градусов))
            double startX = line.getStartPoint().getX() - line.getStartPoint().getZ() * 0.5 * Math.cos(Math.PI / 4);
            double startY = -line.getStartPoint().getY() + line.getStartPoint().getZ() * 0.5 * Math.cos(Math.PI / 4);
            double endX = line.getEndPoint().getX() - line.getEndPoint().getZ() * 0.5 * Math.cos(Math.PI / 4);
            double endY = -line.getEndPoint().getY() + line.getEndPoint().getZ() * 0.5 * Math.cos(Math.PI / 4);

            drawLine(gc, startX, startY, endX, endY);
        }
    }

    //обработчик кнопки смещения по oX (увеличение)
    public void onBtnMovingIncreaseXClick(ActionEvent actionEvent) {
        object3D.doAffineTransformation(AffineTransformationMatrix3D.getMovingMatrix(10.0, 0.0, 0.0));
        drawAll();
    }

    //обработчик кнопки смещения по oX (уменьшение)
    public void onBtnMovingReduceXClick(ActionEvent actionEvent) {
        object3D.doAffineTransformation(AffineTransformationMatrix3D.getMovingMatrix(-10.0, 0.0, 0.0));
        drawAll();
    }

    //обработчик кнопки смещения по oY (увеличение)
    public void onBtnMovingIncreaseYClick(ActionEvent actionEvent) {
        object3D.doAffineTransformation(AffineTransformationMatrix3D.getMovingMatrix(0.0, 10.0, 0.0));
        drawAll();
    }

    //обработчик кнопки смещения по oY (уменьшение)
    public void onBtnMovingReduceYClick(ActionEvent actionEvent) {
        object3D.doAffineTransformation(AffineTransformationMatrix3D.getMovingMatrix(0.0, -10.0, 0.0));
        drawAll();
    }

    //обработчик кнопки смещения по oZ (увеличение)
    public void onBtnMovingIncreaseZClick(ActionEvent actionEvent) {
        object3D.doAffineTransformation(AffineTransformationMatrix3D.getMovingMatrix(0.0, 0.0, 10.0));
        drawAll();
    }

    //обработчик кнопки смещения по oZ (уменьшение)
    public void onBtnMovingReduceZClick(ActionEvent actionEvent) {
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

    //обработчик кнопки отзеркаливания относительно YoZ
    public void onBtnReflectionYoZClick(ActionEvent actionEvent) throws Exception {
        object3D.doAffineTransformation(AffineTransformationMatrix3D.getReflectionMatrix(-1, 1, 1));
        drawAll();
    }

    //обработчик кнопки отзеркаливания относительно ZoX
    public void onBtnReflectionZoXClick(ActionEvent actionEvent) throws Exception {
        object3D.doAffineTransformation(AffineTransformationMatrix3D.getReflectionMatrix(1, -1, 1));
        drawAll();
    }

    //обработчик кнопки отзеркаливания относительно XoZ
    public void onBtnReflectionXoYClick(ActionEvent actionEvent) throws Exception {
        object3D.doAffineTransformation(AffineTransformationMatrix3D.getReflectionMatrix(1, 1, -1));
        drawAll();
    }

    //обработчик кнопки сохранения координат фигуры
    public void onBtnSavingFigureClick(ActionEvent actionEvent) throws URISyntaxException {
        object3D.writeLinesToFile("lines.txt");
    }

    public void onBtnLoadingFigureClick(ActionEvent actionEvent) {
        object3D.readLinesFromFile("lines.txt");
        drawAll();
    }

    //TODO можно найти более удачный таймер, в который можно передавать параметры (toX, toY, toZ, timingFunction())...
    public void onBtnFigureTranslatingXAnimationClick(ActionEvent actionEvent) {
        timer = new AnimationTimer(){
            private int counter = 0;
            private double toX = 10.0;
            private int steps = 20; //количество формальных сдвигов

            @Override
            public void handle(long now) {
                counter = translateAnimationProcess(toX, 0.0, 0.0, steps,  counter);
                drawAll();
            }
        };
        timer.start();
    }

    public void onBtnFigureTranslatingYAnimationClick(ActionEvent actionEvent) {
        timer = new AnimationTimer(){
            private int counter = 0;
            private double toY = 10.0;
            private int steps = 20; //количество формальных сдвигов
            @Override
            public void handle(long now) {
                counter = translateAnimationProcess(0.0, toY, 0.0, steps, counter);
                drawAll();
            }
        };
        timer.start();
    }

    //тайминг функция
    private double timingFunction(int num, int steps) {
        // первая половина времени - 10, вторая - плавное уменьшение по гиперболе
        int center = steps/2;
        if (num < center) {
            System.out.println("num=" + num  + " res=10");
            return 10.0;
        } else {
            System.out.println("num =" + num  + " res=" + 5 * ((double)steps / abs(num)));
            return 5 * ((double)steps / num);

        }
    }
    public void onBtnFigureTranslatingZAnimationClick(ActionEvent actionEvent) {
        timer = new AnimationTimer(){
            private int counter = 0;
            private double toZ = 10.0;
            private int steps = 20; //количество формальных сдвигов

            @Override
            public void handle(long now) {
                toZ = timingFunction(counter, steps);
                counter = translateAnimationProcess(0.0, 0.0, toZ, steps, counter);
                drawAll();
            }
        };
        timer.start();

    }



    //условное перемещение фигуры (с проверкой состояния)
    private int translateAnimationProcess(double toX, double toY, double toZ, int steps, int counter) {
        object3D.doAffineTransformation(AffineTransformationMatrix3D.getMovingMatrix(toX, toY, toZ));
        if(counter == steps) {
            timer.stop();
        }
        return ++counter;
    }

    private AnimationTimer timer;
}