#pragma once

#ifndef VECTOR4D_H
#define VECTOR4D_H

#include <iostream>
#include <cmath>
#include "Vector3D.hpp"
struct Vector4D
{
    static constexpr float eps = 0.0001f;

    Vector4D() noexcept :
        x(0), y(0), z(0), w(0) {}

    Vector4D(float x, float y, float z, float w) noexcept :
        x(x), y(y), z(z), w(w) {}

    Vector4D(const Vector3D& v, float w) noexcept :
        x(v.x), y(v.y), z(v.z), w(w) {}


    Vector4D(const Vector4D& v) noexcept :
        x(v.x), y(v.y), z(v.z), w(v.w) {}

    size_t Size() const { return 4; }


    float Length() const noexcept
    {
        return std::sqrt ( x*x + y*y + z*z);
    }


    Vector4D Normalize() const noexcept
    {
        float length = Length();
        return Vector4D(x / length, y / length, z / length, w / length);
    }

    bool operator == (const Vector4D& other) const
    {
        return  std::abs(other.x - x) < eps &&
                std::abs(other.y - y) < eps &&
                std::abs(other.z - z) < eps &&
                std::abs(other.w - w) < eps;
    }

    bool operator != (const Vector4D& other)
    {
        return ! (*this == other);
    }

    Vector4D& operator = (const Vector4D& other)
    {
        x = other.x;
        y = other.y;
        z = other.z;
        w = other.w;

        return *this;
    }

    float& operator[](size_t i)
    {
        assert(i < 4);

        switch(i)
        {
        case 0:
            return x;
        case 1:
            return y;
        case 2:
            return z;
        case 3:
            return w;
        }
    }

    const float& operator[](size_t i) const
    {
        assert(i < 4);

        switch(i)
        {
        case 0:
            return x;
        case 1:
            return y;
        case 2:
            return z;
        case 3:
            return w;
        }
    }

    Vector4D operator + (const Vector4D& other)
    {
        return Vector4D(x + other.x, y + other.y, z + other.z, w + other.w);
    }

    Vector4D operator - (const Vector4D& other)
    {
        return Vector4D(x - other.x, y - other.y, z - other.z, w - other.w);
    }

    Vector4D operator * (float a)
    {
        return Vector4D(x * a, y * a, z * a, w * a);
    }

    Vector4D operator / (float a)
    {
        return Vector4D(x / a, y / a, z / a, w / a);
    }


    Vector4D& operator += (const Vector4D& other)
    {
        x += other.x;  y += other.y;  z += other.z; w += other.w;
        return *this;
    }

    Vector4D& operator -= (const Vector4D& other)
    {
        x -= other.x;  y -= other.y;  z -= other.z; w -= other.w;
        return *this;
    }

    Vector4D& operator *= (float a)
    {
        x *= a;  y *= a;  z *= a; w *= a;
        return *this;
    }

    Vector4D& operator /= (float a)
    {
        x /= a;  y /= a;  z /= a; w /= a;
        return *this;
    }


    Vector3D ToVector3D() const noexcept
    {
        return Vector3D(x, y, z);
    }

    friend std::ostream& operator<< (std::ostream& out, const Vector4D& vec)
    {
        out << vec.x << " " << vec.y << " " << vec.z << " " << vec.w << std::endl;
        return out;
    }

    float x, y, z, w;
};


#endif // VECTOR4D_H
