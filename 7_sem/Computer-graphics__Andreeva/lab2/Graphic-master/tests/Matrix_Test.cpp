#define BOOST_TEST_MODULE Matrix module name
#include <boost/test/unit_test.hpp>
#include "../core/Matrix.hpp"
#include "../core/MatrixTransform.hpp"


BOOST_AUTO_TEST_SUITE(Matrix_Test)


BOOST_AUTO_TEST_CASE(Multiply_Test)
{
    Matrix4x4 mat(2.0);


    BOOST_CHECK_EQUAL(Matrix4x4(1.f) * mat, Matrix4x4(2.f));

    Matrix4x4 left(1.f);
    Matrix4x4 right(1.f);
    Matrix4x4 result(1.f);

    left[3][0] = 0.5f;
    left[3][1] = 0.5f;
    left[3][2] = 0.5f;

    right[0][1] = 0.5f;
    right[1][0] = 0.5f;
    right[1][2] = 0.5f;
    right[2][1] = 0.5f;

    result[0][1] = 0.5f;
    result[1][0] = 0.5f;
    result[1][2] = 0.5f;
    result[2][1] = 0.5f;

    result[3][0] = 0.75f;
    result[3][1] = 1.0f;
    result[3][2] = 0.75f;

    BOOST_CHECK_EQUAL(left * right, result);

}


BOOST_AUTO_TEST_CASE(Multiplying_To_Vector_Test)
{
    Matrix4x4 mat(1.f);
    Vector4D vec(0.5f, 0.5f, 0.0f, 1.f);

    mat[3][0] = 0.5f;
    mat[3][1] = 0.3f;

    BOOST_CHECK_EQUAL(vec * mat, Vector4D(1.f, 0.8f, 0.0f, 1.0f));
}


BOOST_AUTO_TEST_SUITE_END()
