#ifndef WINDOW_H
#define WINDOW_H

#include <string>
#include <vector>
#include <list>

#include "figure.h"

struct SDL_Window;
struct SDL_Renderer;


class Window
{
public:
    Window();
    ~Window();

    void Show();
private:
    SDL_Window*     m_pWindow;
    SDL_Renderer*   m_pRenderer;

    int             m_Width;
    int             m_Height;
    bool            m_IsVisible;

    int             m_FrameHeight;

    Figure          m_Figure1;
    Figure          m_Figure2;
    Figure          m_Figure3;
    Figure          m_Figure4;
    Figure          m_Figure5;

    int             m_BufferSize;
    int*            m_pFrameBuffer;
    float*          m_pZBuffer;


    std::vector<std::list<Figure*>>   m_Groups;
    std::list<Figure*> m_Active;

    void HandleEvents();

    void FigureGroupAppend(Figure& figure);
};

#endif // WINDOW_H
