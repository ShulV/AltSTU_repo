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

    private final Object3D object3D = new Object3D();

    public Controller() throws URISyntaxException {
        object3D.readLinesFromFile(""); //TODO заменить абсолютный путь
    }

    private void drawLine(Line3D line) {
        GraphicsContext gc = canvasPlot.getGraphicsContext2D();
        gc.setLineWidth(1.0);
        gc.setStroke(Color.BLUE);
        double xStart = line.getStartPoint().getX();
        double yStart = line.getStartPoint().getY();
        double xEnd = line.getEndPoint().getX();
        double yEnd = line.getEndPoint().getY();
        gc.strokeLine(xStart, yStart, xEnd, yEnd);
    }
    public void clearCanvas() {
        GraphicsContext gc = canvasPlot.getGraphicsContext2D();
        gc.clearRect(0, 0, canvasPlot.getWidth(), canvasPlot.getHeight());
    }

    public void drawFigure() {
        for (Line3D line: object3D.getLineList()
             ) {
            drawLine(line);
        }
    }
    public void onBtnIncreaseXClick(ActionEvent actionEvent) throws URISyntaxException {
        object3D.doAffineTransformation(AffineTransformationMatrix3D.getMovingMatrix(10.0, 0.0, 0.0));
        clearCanvas();
        drawFigure();
    }

    public void onBtnReduceXClick(ActionEvent actionEvent) throws URISyntaxException {
        object3D.doAffineTransformation(AffineTransformationMatrix3D.getMovingMatrix(-10.0, 0.0, 0.0));
        clearCanvas();
        drawFigure();
    }

    public void onBtnIncreaseYClick(ActionEvent actionEvent) throws URISyntaxException {
        object3D.doAffineTransformation(AffineTransformationMatrix3D.getMovingMatrix(0.0, 10.0, 0.0));
        clearCanvas();
        drawFigure();
    }

    public void onBtnReduceYClick(ActionEvent actionEvent) throws URISyntaxException {
        object3D.doAffineTransformation(AffineTransformationMatrix3D.getMovingMatrix(0.0, -10.0, 0.0));
        clearCanvas();
        drawFigure();
    }

    public void onBtnIncreaseZClick(ActionEvent actionEvent) throws URISyntaxException {
        object3D.doAffineTransformation(AffineTransformationMatrix3D.getMovingMatrix(0.0, 00.0, -10.0));
        clearCanvas();
        drawFigure();
    }

    public void onBtnReduceZClick(ActionEvent actionEvent) throws URISyntaxException {
        object3D.doAffineTransformation(AffineTransformationMatrix3D.getMovingMatrix(0.0, 0.0, -10.0));
        clearCanvas();
        drawFigure();
    }
}