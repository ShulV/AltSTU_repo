#ifndef FIGURE_H
#define FIGURE_H

#include <vector>
#include <list>

struct Point3D {
    int x, y, z;
};


struct SDL_Renderer;

struct Edge
{
    Point3D p1;
    Point3D p2;
};

struct EdgePair
{
    Edge* left;
    Edge* right;

    float xl;
    float dxl;
    int dyl;

    float xr;
    float dxr;
    int dyr;

    float zl;
    float dzx;
    float dzy;
};

class Figure
{
public:
    Figure();
    Figure(int number, const std::vector<Point3D>& points);
    ~Figure();

    int MaxY() const;

    void Activate(int y);


    int Number() const;

    int GetDy() const;

    const std::list<EdgePair> &ActivePairs() const;

private:

    int         m_Number;
    int         dy;
    int         a, b, c, d;
    int         m_MaxY;

    Point3D*    m_pPoints;
    size_t      m_NumPoints;

    Edge*       m_pEdges;
    size_t      m_NumEdges;

    std::list<EdgePair>     m_ActivePairs;
    std::list<Edge>         m_ActiveEdges;




    void Init();


    inline float InterspectPoint(const Edge &edge, int y) const
    {
        // l(y-y0)/m + x0
        return (edge.p2.x - edge.p1.x) * (y - edge.p1.y) /
                static_cast<float>(edge.p2.y - edge.p1.y) +  edge.p1.x;
    }

};

#endif // FIGURE_H
