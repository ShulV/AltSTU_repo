#define BOOST_TEST_MODULE Transform module name
#include <boost/test/unit_test.hpp>
#include "../core/Matrix.hpp"
#include "../core/MatrixTransform.hpp"


BOOST_AUTO_TEST_SUITE(Transform_Test)


BOOST_AUTO_TEST_CASE(Translate_Test)
{
    Matrix4x4 mat(1.0f);



    BOOST_CHECK_EQUAL(Vector4D(0.5f, 0.5f, 0.5f, 1.0f) *
                      Translate(mat, Vector3D(0.5f, 0.5f, 0.5f)),
                      Vector4D(1.0f, 1.0f, 1.0f, 1.0f));

    BOOST_CHECK_NE(Vector4D(0.5f, 0.5f, 0.5f, 1.0f) *
                      Translate(mat, Vector3D(0.5f, 0.5f, 0.5f)),
                      Vector4D(0.5f, 0.5f, 0.5f, 1.0f));

    BOOST_CHECK_EQUAL(Vector4D(-0.5f, -0.5f, 0.0f, 1.0f) *
                      Translate(mat, Vector3D(0.5f, 0.5f, 0.0f)),
                      Vector4D(0.0f, 0.0f, 0.0f, 1.0f));
}


BOOST_AUTO_TEST_CASE(Scale_Test)
{
    Matrix4x4 mat(1.0f);



    BOOST_CHECK_EQUAL(Vector4D(0.5f, 0.5f, 0.5f, 1.0f) *
                      Scale(mat, Vector3D(2.0f, 2.0f, 2.0f)),
                      Vector4D(1.0f, 1.0f, 1.0f, 1.0f));

    BOOST_CHECK_NE(Vector4D(0.5f, 0.5f, 0.5f, 1.0f) *
                      Scale(mat, Vector3D(0.5f, 0.5f, 0.5f)),
                      Vector4D(0.5f, 0.5f, 0.5f, 1.0f));

    BOOST_CHECK_EQUAL(Vector4D(0.5f, 0.5f, 0.5f, 1.0f) *
                      Scale(mat, Vector3D(0.5f, 0.5f, 0.5f)),
                      Vector4D(0.25f, 0.25f, 0.25f, 1.0f));
}


BOOST_AUTO_TEST_CASE(Rotate_X_Test)
{

    BOOST_CHECK_EQUAL(Vector4D(0.0f, 1.0f, 0.0f, 1.0f) * RotateX(ToRadians(90.0f)),
                      Vector4D(0.0f, 0.0f, 1.0f, 1.0f));

    BOOST_CHECK_EQUAL(Vector4D(0.0f, 1.0f, 0.0f, 1.0f) * RotateX(ToRadians(45.0f)),
                      Vector4D(0.0f, 0.707107f, 0.707107f, 1.0f));


}

BOOST_AUTO_TEST_SUITE_END()
