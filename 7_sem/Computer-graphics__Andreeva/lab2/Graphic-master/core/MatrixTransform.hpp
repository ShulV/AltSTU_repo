#pragma once

#ifndef MATRIXTRANSFORM_H
#define MATRIXTRANSFORM_H

#include "Matrix.hpp"

#include <cmath>

constexpr float pi = 3.14159265359f;

Vector4D operator* (const Vector4D& v, const Matrix4x4& mat)
{

    Vector4D res;

    for (size_t i = 0; i < v.Size(); ++i)
    {
        float a = 0;
        for (size_t j = 0; j < v.Size(); ++j)
        {
            a+= v[j] * mat[j][i];
        }

        res[i] = a;
    }

    return res;
}


float ToRadians(float angle)
{
    return angle * pi / 180.f;
}

Matrix4x4 Translate (const Matrix4x4& mat, const Vector3D& vec)
{
    Matrix4x4 m(1.f);

    m[3] = Vector4D(vec, 1.0f);

    return m * mat;
}

Matrix4x4 Scale (const Matrix4x4& mat, const Vector3D& vec)
{
    Matrix4x4 m(1.f);

    m[0][0] = vec.x;
    m[1][1] = vec.y;
    m[2][2] = vec.z;

    return m * mat;
}


Matrix4x4 RotateX(float angle)
{

    float sin = std::sin(angle);
    float cos = std::cos(angle);

    Matrix4x4 m(1.0f);
    m[1][1] = cos;
    m[1][2] = sin;
    m[2][1] = -sin;
    m[2][2] = cos;

    return m;
}

Matrix4x4 RotateY(float angle)
{

    float sin = std::sin(angle);
    float cos = std::cos(angle);

    Matrix4x4 m(1.0f);
    m[0][0] =  cos;
    m[0][2] = -sin;
    m[2][0] =  sin;
    m[2][2] =  cos;

    return m;
}

Matrix4x4 RotateZ(float angle)
{

    float sin = std::sin(angle);
    float cos = std::cos(angle);

    Matrix4x4 m(1.0f);
    m[0][0] = cos;
    m[0][1] = sin;
    m[1][0] = -sin;
    m[1][1] = cos;

    return m;
}

Matrix4x4 ProjectionX()
{
    Matrix4x4 mat(1.0f);
    mat[0][0] = 0.0f;
    return mat;
}

Matrix4x4 ProjectionY()
{
    Matrix4x4 mat(1.0f);
    mat[1][1] = 0.0f;
    return mat;
}

Matrix4x4 ProjectionZ()
{
    Matrix4x4 mat(1.0f);
    mat[2][2] = 0.0f;
    return mat;
}

Matrix4x4 ObliqueProjection(float a, float b)
{
    Matrix4x4 mat(1.0f);
    mat[2][0] = a;
    mat[2][1] = b;
    return mat;
}

Matrix4x4 Perspective(float fovy, float aspect, float zNear, float zFar)
{

     const float tanHalfFovy = tan(fovy / 2.0);

    Matrix4x4 Result(0.0f);
    Result[0][0] = 1.0f / (aspect * tanHalfFovy);
    Result[1][1] = 1.0f / (tanHalfFovy);
    Result[2][2] = zFar / (zFar - zNear);
    Result[3][2] = 1.0f;
    Result[2][3] = -(zFar * zNear) / (zFar - zNear);
    return Result;
}


#endif // MATRIXTRANSFORM_H
