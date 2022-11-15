#include <SDL.h>
#include <algorithm>
#include "figure.h"
#include <cmath>


Figure::Figure() {}

Figure::Figure(int number, const std::vector<Point3D> &points) :
    m_Number(number),
    m_pPoints(nullptr), m_NumPoints(0),
    m_pEdges(nullptr), m_NumEdges(0)
{
    m_NumPoints = points.size();
    m_pPoints = new Point3D[m_NumPoints];
    memcpy(m_pPoints, points.data(), sizeof (Point3D) * m_NumPoints);

    Init();
}

Figure::~Figure()
{
    delete m_pPoints;
    delete m_pEdges;
}


int Figure::MaxY() const
{
    return m_MaxY;
}

void Figure::Activate(int y)
{
    std::list<Edge*> activeEdges;

    for (int i = 0; i < m_NumEdges; ++i) {

        Edge& edge = m_pEdges[i];

        // add edges that are not parallel to the axis x
        if ((edge.p1.y == y && edge.p2.y < y) ||
            (edge.p2.y == y && edge.p1.y < y) )
            activeEdges.push_back(&edge);
    }


    // update active pairs
    for (auto iter = m_ActivePairs.begin(); iter != m_ActivePairs.end();) {



        auto& edgePair = *iter;
        --edgePair.dyl;
        --edgePair.dyr;

        edgePair.xl -= edgePair.dxl;
        edgePair.xr -= edgePair.dxr;

        if (edgePair.dyl <= 0) {
            auto point = edgePair.left->p1.y < edgePair.left->p2.y?
                         edgePair.left->p1 : edgePair.left->p2;

            edgePair.left = nullptr;

            // find new left edge
            for (auto it = activeEdges.begin(); it != activeEdges.end(); ++it) {

                Edge* edge = *it;

                if ((point.x == edge->p1.x && point.y == edge->p1.y) ||
                    (point.x == edge->p2.x && point.y == edge->p2.y)) {

                    edgePair.left = edge;

                    edgePair.dyl = std::abs(edge->p1.y - edge->p2.y);
                    edgePair.xl  = InterspectPoint(*edge, y);
                    edgePair.dxl = InterspectPoint(*edge, y + 1) - edgePair.xl;

                    it = activeEdges.erase(it);
                    break;
                }
            }

        }

        if (edgePair.dyr <= 0) {

            auto point = edgePair.right->p1.y < edgePair.right->p2.y?
                         edgePair.right->p1 : edgePair.right->p2;

            edgePair.right = nullptr;

            // find new right edge
            for (auto it = activeEdges.begin(); it != activeEdges.end(); ++it) {

                Edge* edge = *it;

                if ((point.x == edge->p1.x && point.y == edge->p1.y) ||
                    (point.x == edge->p2.x && point.y == edge->p2.y)) {

                    edgePair.right = edge;

                    edgePair.dyr = std::abs(edge->p1.y - edge->p2.y);
                    edgePair.xr  = InterspectPoint(*edge, y);
                    edgePair.dxr = InterspectPoint(*edge, y + 1) - edgePair.xr;

                    it = activeEdges.erase(it);
                    break;
                }

            }

        }


        if (edgePair.left && edgePair.right) {
            edgePair.zl = static_cast<float>(a * edgePair.xl + b*y + d) / -c;
            ++iter;
        } else {
            iter = m_ActivePairs.erase(iter);
        }
    }


    // add new pairs
    for (auto it = activeEdges.begin(); it != activeEdges.end();) {

        auto left = *it;
        it = activeEdges.erase(it);

        auto right = *it;
        it = activeEdges.erase(it);


        // sort edges by x
        if ((left->p1.y == right->p1.y && left->p1.x > right->p1.x) ||
            (left->p2.y == right->p2.y && left->p2.x > right->p2.x) ||
            (left->p1.y == right->p2.y && left->p1.x > right->p2.x) ||
            (left->p2.y == right->p1.y && left->p2.x > right->p1.x))
            std::swap(left, right);

        EdgePair edgePair;

        edgePair.left = left;
        edgePair.right = right;

        edgePair.dyl = std::abs(left->p1.y - left->p2.y);
        edgePair.xl  = InterspectPoint(*left, y);
        edgePair.dxl = InterspectPoint(*left, y + 1) - edgePair.xl;

        edgePair.dyr = std::abs(right->p1.y - right->p2.y);
        edgePair.xr  = InterspectPoint(*right, y);
        edgePair.dxr = InterspectPoint(*right, y + 1) - edgePair.xr;

        edgePair.zl = left->p1.y > left->p2.y?
                      left->p1.z : left->p2.z;

        edgePair.dzx = static_cast<float>(a) / c;
        edgePair.dzy = static_cast<float>(b) / c;

        m_ActivePairs.emplace_back(edgePair);
    }

}

const std::list<EdgePair> &Figure::ActivePairs() const
{
    return m_ActivePairs;
}

int Figure::Number() const
{
    return m_Number;
}

int Figure::GetDy() const
{
    return dy;
}



void Figure::Init()
{

    m_NumEdges = m_NumPoints;
    m_pEdges = new Edge [m_NumEdges];

    // initialize a list of edges
    for (size_t i = 0; i < m_NumPoints; ++i) {
        Point3D prev;
        Point3D cur = m_pPoints[i];

        if (i != 0) {
            prev = m_pPoints[i - 1];
        } else {
            prev = m_pPoints[m_NumPoints - 1];
        }


        m_pEdges[i] = {cur, prev};

    }

    // initialize the dy
    int minY = INT32_MAX;
    int maxY = INT32_MIN;

    for (size_t i = 0; i < m_NumPoints; ++i) {
        auto point = m_pPoints[i];
        minY = (point.y < minY)? point.y : minY;
        maxY = (point.y > maxY)? point.y : maxY;
    }

    m_MaxY = maxY;
    dy = maxY - minY;

    // initialize coefficients of the equation of a plane
    a = b = c = d = 0;
    for (size_t i = 0; i < m_NumPoints; ++i) {
        Point3D next, cur = m_pPoints[i];

        if (i != m_NumPoints - 1) {
            next = m_pPoints[i + 1];
        } else {
            next = m_pPoints[0];
        }

        a+= (next.y - cur.y)*(cur.z + next.z);
        b+= (next.z - cur.z)*(cur.x + next.x);
        c+= (next.x - cur.x)*(cur.y + next.y);
    }

    for (size_t i = 0 ; i < m_NumPoints; ++i) {
        auto p = m_pPoints[i];
        d += a * p.x + b * p.y + c * p.z;
    }

    d /= -static_cast<int>(m_NumPoints);
}
