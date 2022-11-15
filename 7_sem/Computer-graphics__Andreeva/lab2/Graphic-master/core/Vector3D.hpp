#pragma once
#ifndef VECTOR_H
#define VECTOR_H

#include <cmath>
#include <cassert>

struct Vector3D
{
    Vector3D() noexcept :
        x(0), y(0), z(0) {}

    Vector3D(float x, float y, float z) noexcept :
        x(x), y(y), z(z) {}

    float Length() const noexcept
    {
        return std::sqrt ( x*x + y*y + z*z);
    }


    Vector3D Normalize() const noexcept
    {
        float length = Length();
        return Vector3D(x / length, y / length, z / length);
    }

    bool operator == (const Vector3D& other)
    {
        return  other.x == x &&
                other.y == y &&
                other.z == z;
    }

    bool operator != (const Vector3D& other)
    {
        return ! (*this == other);
    }

    Vector3D& operator = (const Vector3D& other)
    {
        x = other.x;
        y = other.y;
        z = other.z;

        return *this;
    }

    float& operator[](size_t i)
    {
        assert(i < 3);

        switch(i)
        {
        case 0:
            return x;
        case 1:
            return y;
        case 2:
            return z;
        }
    }


    const float& operator[](size_t i) const
    {
        assert(i < 3);

        switch(i)
        {
        case 0:
            return x;
        case 1:
            return y;
        case 2:
            return z;
        }
    }

    Vector3D operator + (const Vector3D& other)
    {
        return Vector3D(x + other.x, y + other.y, z + other.z);
    }

    Vector3D operator - (const Vector3D& other)
    {
        return Vector3D(x - other.x, y - other.y, z - other.z);
    }

    Vector3D operator * (float a)
    {
        return Vector3D(x * a, y * a, z * a);
    }

    Vector3D operator / (float a)
    {
        return Vector3D(x / a, y / a, z / a);
    }


    Vector3D& operator += (const Vector3D& other)
    {
        x += other.x;  y += other.y;  z += other.z;
        return *this;;
    }

    Vector3D& operator -= (const Vector3D& other)
    {
        x -= other.x;  y -= other.y;  z -= other.z;
        return *this;
    }

    Vector3D& operator *= (float a)
    {
        x *= a;  y *= a;  z *= a;
        return *this;
    }

    Vector3D& operator /= (float a)
    {
        x /= a;  y /= a;  z /= a;
        return *this;
    }

    float x, y, z;
};

#endif // VECTOR_H
