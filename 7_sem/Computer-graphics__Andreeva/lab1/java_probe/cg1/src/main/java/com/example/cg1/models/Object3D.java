package com.example.cg1.models;

import javafx.animation.*;
import javafx.beans.value.WritableValue;
import javafx.geometry.Bounds;
import javafx.scene.canvas.Canvas;
import javafx.util.Duration;

import java.io.*;
import java.text.DecimalFormat;
import java.text.DecimalFormatSymbols;
import java.util.ArrayList;
import java.util.List;
import java.util.Locale;

import static java.lang.Double.parseDouble;

public class Object3D {
    private final List<Line3D> lineList = new ArrayList<>();

    public void addLineToList(Line3D line) {
        lineList.add(line);
    }

    //прочитать строки с данными о координатах из файла
    public void readLinesFromFile(String filePath) {
        try {
            File file = new File(filePath);
            FileReader fr = new FileReader(file);
            BufferedReader reader = new BufferedReader(fr); //буфер для построчного считывания
            String line = reader.readLine(); //считывание 1ой строки
            lineList.clear();
            while (line != null) {
                this.addLineToList(convertFileStringToLine3D(line)); //добавление нового объекта-линии в List
                line = reader.readLine();
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    //записать новые значения координат проволочной фигуры в файл
    public void writeLinesToFile(String filePath) {
        try (FileWriter writer = new FileWriter(filePath, false)) {
            String stringDataLine;
            for (Line3D line3D : lineList
            ) {
                DecimalFormat dF = new DecimalFormat("#################0.00");
                //для "." в double (по дефолту запятая)
                dF.setDecimalFormatSymbols(new DecimalFormatSymbols(Locale.CANADA));
                stringDataLine = String.format("%s,%s,%s;%s,%s,%s\n",
                        dF.format(line3D.getStartPoint().getX()), //X1
                        dF.format(line3D.getStartPoint().getY()), //Y1
                        dF.format(line3D.getStartPoint().getZ()), //Z1
                        dF.format(line3D.getEndPoint().getX()), //X2
                        dF.format(line3D.getEndPoint().getY()), //Y2
                        dF.format(line3D.getEndPoint().getZ())); //Z2

                assert stringDataLine != null;
                System.out.println(stringDataLine);
                writer.write(stringDataLine);
                writer.flush();
            }

        } catch (IOException ex) {
            throw new RuntimeException(ex);
        }
    }

    //создать объект отрезка из данных полученных из строки файла
    private Line3D convertFileStringToLine3D(String string) {
        String[] points = string.split(";");
        String[] startCoords = points[0].split(",");
        String[] endCoords = points[1].split(",");
        CustomPoint3D startPoint = new CustomPoint3D(parseDouble(startCoords[0]),
                parseDouble(startCoords[1]),
                parseDouble(startCoords[2]));
        CustomPoint3D endPoint = new CustomPoint3D(parseDouble(endCoords[0]),
                parseDouble(endCoords[1]),
                parseDouble(endCoords[2]));
        return new Line3D(startPoint, endPoint);
    }

    public List<Line3D> getLineList() {
        return lineList;
    }

    //сделать Аффинное преобразование всех отрезков объекта (их точек)
    public void doAffineTransformation(double[][] affineTransformationMatrix) {
        for (Line3D line : lineList
        ) {
            line.doAffineTransformation(affineTransformationMatrix);
        }
    }

}
