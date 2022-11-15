#include "Window.h"

#include <cassert>
#include <algorithm>
#include <random>

#include <SDL.h>


Window::Window() :
    m_Width(1280), m_Height(720), m_FrameHeight(m_Height),
    m_Figure1(1, {{150, 150, 150}, {250, 250, 50}, {300, 100, 50}}),
    m_Figure2(2, {{100, 50,  100}, {100, 250, 100}, {250, 250,  100}, {250, 50, 100}}),
    m_Figure3(3, {{200, 200, 125}, {300, 350, 100}, {350, 250,  100}}),
    m_Figure4(4, {{50, 200, 5}, {50, 350, 5}, {150, 320,  120}, {120, 170,  120}}),
    m_Figure5(5, {{25, 50, 10}, {25, 370, 10}, {350, 370, 5}}),
    m_BufferSize(m_Width)
{
    assert(SDL_Init(SDL_INIT_VIDEO) >= 0);

    m_pWindow = SDL_CreateWindow("window",
                                 SDL_WINDOWPOS_CENTERED,
                                 SDL_WINDOWPOS_CENTERED,
                                 m_Width, m_Height, 0);

    assert(m_pWindow != nullptr);

    m_pRenderer = SDL_CreateRenderer(m_pWindow, -1,
                                     SDL_RENDERER_ACCELERATED);

    assert(m_pRenderer != nullptr);



    m_pFrameBuffer  = new int   [m_BufferSize];
    m_pZBuffer      = new float [m_BufferSize];

    m_Groups.resize(m_FrameHeight);

    FigureGroupAppend(m_Figure1);
    FigureGroupAppend(m_Figure2);
    FigureGroupAppend(m_Figure3);
    FigureGroupAppend(m_Figure4);
    FigureGroupAppend(m_Figure5);
}

Window::~Window()
{
    delete [] m_pFrameBuffer;
    delete [] m_pZBuffer;

    SDL_DestroyRenderer(m_pRenderer);
    SDL_DestroyWindow(m_pWindow);

    SDL_Quit();
}

void Window::Show()
{

    SDL_SetRenderDrawColor(m_pRenderer, 250, 250, 250, 255);
    SDL_RenderClear(m_pRenderer);

    SDL_SetRenderDrawColor(m_pRenderer, 0, 0, 0, 255);

    for (int y = m_FrameHeight - 1; y >= 0; --y) {

        memset(m_pZBuffer,      0, sizeof(float)    * m_BufferSize);
        memset(m_pFrameBuffer,  0, sizeof(int)      * m_BufferSize);

        // remove not active figures
        for (auto it = m_Active.begin(); it != m_Active.end();) {

            if ((*it)->GetDy() < 0)
                it = m_Active.erase(it);
            else
                ++it;
        }

        // add active figures in the list
        auto* group = &m_Groups[y];
        for (auto it = group->begin(); it != group->end(); ++it) {
            m_Active.push_back(*it);
        }


        for (auto& figure : m_Active) {
            figure->Activate(y);

            // update frame and z buffers for each edge
            for (const auto& edgepair : figure->ActivePairs()) {

                float z = edgepair.zl;
                for (int x = static_cast<int>(edgepair.xl); x <= edgepair.xr; ++x) {

                    if (z > m_pZBuffer[x]) {
                        m_pFrameBuffer[x] = figure->Number();
                        m_pZBuffer[x] = z;
                    }

                    z -= edgepair.dzx;
                }
            }
        }

        for (int x = 0; x < m_BufferSize; ++x) {
            switch (m_pFrameBuffer[x]) {
            case 0:
                SDL_SetRenderDrawColor(m_pRenderer, 33, 33, 33, 255);
                break;
            case 1:
                SDL_SetRenderDrawColor(m_pRenderer, 255, 0, 0, 255);
                break;
            case 2:
                SDL_SetRenderDrawColor(m_pRenderer, 0, 255, 0, 255);
                break;
            case 3:
                SDL_SetRenderDrawColor(m_pRenderer, 255, 255, 0, 255);
                break;
            case 4:
                SDL_SetRenderDrawColor(m_pRenderer, 255, 0, 255, 255);
                break;
            case 5:
                SDL_SetRenderDrawColor(m_pRenderer, 0, 255, 255, 255);
                break;
            default:
                break;
            };
            SDL_RenderDrawPoint(m_pRenderer, x, m_FrameHeight - y - 1);
        }
        SDL_Delay(15);
        SDL_RenderPresent(m_pRenderer);
        HandleEvents();
    }

    while(true) {
        HandleEvents();
    }
}

void Window::HandleEvents()
{
    SDL_Event event;

    while (SDL_PollEvent(&event))
    {
        switch (event.type)
        {
        case SDL_QUIT:
            exit(0);
            break;

        default:
            break;
        }
    }
}

void Window::FigureGroupAppend(Figure &figure)
{
    int maxY = figure.MaxY();
    m_Groups[maxY].push_back(&figure);
}
