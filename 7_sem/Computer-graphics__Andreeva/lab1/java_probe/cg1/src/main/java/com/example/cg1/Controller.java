package com.example.cg1;

import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.canvas.Canvas;
import javafx.scene.canvas.GraphicsContext;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.effect.BlendMode;
import javafx.scene.paint.Color;

public class Controller {
    @FXML
    private Label welcomeText;
    @FXML
    private Button btnShow;
    @FXML
    private Canvas canvasPlot;

    public void drawLine(double xStart, double yStart, double xEnd, double yEnd) {
        GraphicsContext gc = canvasPlot.getGraphicsContext2D() ;
        gc.setLineWidth(1.0);
        gc.setFill(Color.GREEN);
        gc.setStroke(Color.BLUE);
        gc.setGlobalBlendMode(BlendMode.SCREEN);
        gc.strokeLine(xStart, yStart, xEnd, yEnd);
    }

    public void onBtnShowClick(ActionEvent actionEvent) {
        System.out.println("click btn show");
        drawLine(50.0, 50.0, 150.0, 150.0);
    }
}