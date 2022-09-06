package com.example.cg1.models;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.net.URISyntaxException;
import java.util.ArrayList;
import java.util.List;

import static java.lang.Double.parseDouble;

public class Object3D {
    private final List<Line3D> lineList = new ArrayList<>();
    public void addLineToList(Line3D line) {
        lineList.add(line);
    }

    //прочитать строки с данными о координатах из файла
    public void readLinesFromFile(String filePath) throws URISyntaxException {
        try {
            //TODO написать относительный путь
            File file = new File("C:\\Users\\Victor\\IntellijIdeaProjects\\cg1\\src\\main\\resources\\com\\example\\cg1\\lines.txt");
            FileReader fr = new FileReader(file);
            BufferedReader reader = new BufferedReader(fr); //буфер для построчного считывания
            String line = reader.readLine(); //считывание 1ой строки
            while (line != null) {
                this.addLineToList(convertFileStringToLine3D(line)); //добавление нового объекта-линии в List
                line = reader.readLine();
            }
        } catch (IOException e) {
            e.printStackTrace();
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
        for (Line3D line: lineList
             ) {
            line.doAffineTransformation(affineTransformationMatrix);
        }
    }
}
