package com.example.cg1.models;


public class Line3D {
    private final CustomPoint3D startPoint;
    private final CustomPoint3D endPoint;

    @Override
    public String toString() {
        return "Line3D{" +
                "startPoint= (" +
                startPoint.getX() + ", " +
                startPoint.getY() + ", " +
                startPoint.getZ() + ")" +
                ", endPoint= (" +
                endPoint.getX() + ", " +
                endPoint.getY() + ", " +
                endPoint.getZ() + ")" +
                "}\n";
    }

    public Line3D(CustomPoint3D startPoint, CustomPoint3D endPoint) {
        this.startPoint = startPoint;
        this.endPoint = endPoint;
    }

    public Line3D(double startX, double startY, double startZ, double endX, double endY, double endZ) {
        this.startPoint = new CustomPoint3D(startX, startY, startZ);
        this.endPoint = new CustomPoint3D(endX, endY, endZ);
    }

    public CustomPoint3D getStartPoint() {
        return startPoint;
    }

    public CustomPoint3D getEndPoint() {
        return endPoint;
    }

    //сделать Аффинное преобразование отрезка (его точек)
    public void doAffineTransformation(double[][] affineTransformationMatrix) {
        getStartPoint().doAffineTransformation(affineTransformationMatrix);
        getEndPoint().doAffineTransformation(affineTransformationMatrix);
    }
}
