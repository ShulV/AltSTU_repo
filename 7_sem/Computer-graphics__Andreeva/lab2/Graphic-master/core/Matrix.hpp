#pragma once

#ifndef MATRIX_H
#define MATRIX_H

#include "Vector3D.hpp"
#include "Vector4D.hpp"

#include <iostream>

class Matrix4x4
{
    using RowType = Vector4D;
    using ColumnType = Vector4D;

    RowType data[4];

public:

    Matrix4x4() {
    }

    Matrix4x4(float v) {
        data[0].x = v;
        data[1].y = v;
        data[2].z = v;
        data[3].w = v;
    }

    Matrix4x4(const Matrix4x4& other)
    {
        data[0] = other.data[0];
        data[1] = other.data[1];
        data[2] = other.data[2];
        data[3] = other.data[3];
    }


    Matrix4x4 operator* (const Matrix4x4& other) const
    {
        Matrix4x4 result;

        for (size_t i = 0; i < 4; ++i)
        {
            for (size_t j = 0; j < 4; ++j)
            {
                float a = 0;
                for (size_t k = 0; k < 4; ++k)
                {
                    a += data[i][k] * other[k][j];
                }

                result[i][j] = a;
            }
        }



        return result;
    }

    ColumnType operator* (const ColumnType& v) const
    {
        float x, y, z, w;

        x = data[0].x * v.x + data[0].y * v.y + data[0].z * v.z + data[0].w * v.w;
        y = data[1].x * v.x + data[1].y * v.y + data[1].z * v.z + data[1].w * v.w;
        z = data[2].x * v.x + data[2].y * v.y + data[2].z * v.z + data[2].w * v.w;
        w = data[3].x * v.x + data[3].y * v.y + data[3].z * v.z + data[3].w * v.w;

        return ColumnType(x, y, z, w);
    }

    RowType& operator [] (size_t i)
    {
        return data[i];
    }

    const RowType& operator [] (size_t i) const
    {
        return data[i];
    }

    bool operator== (const Matrix4x4& other) const
    {
        return  data[0] == other[0] &&
                data[1] == other[1] &&
                data[2] == other[2] &&
                data[3] == other[3];
    }

    friend std::ostream& operator << (std::ostream& out, const Matrix4x4& m)
    {
        for (int i = 0; i < 4; i++)
        {
            for (int j = 0; j < 4; ++j)
            {
                out << m[i][j] << " ";
            }
        }
        return out;
    }
};

#endif // MATRIX_H
