#include "qrobotguiview.h"
#include <QDebug>
#include <QtCore>

#ifndef QT_NO_OPENGL
#include <QGLWidget>
#endif

QRobotGUIView::QRobotGUIView(QWidget *parent) :
    QGraphicsView(parent)
{
#ifndef QT_NO_OPENGL
    mOpenGLActive = true;
    setViewport( new QGLWidget );

    qDebug() << tr("OpenGL Vieport enabled");
#else
    mOpenGLActive = false;
    setViewport( new QWidget );

    qDebug() << tr("OpenGL Vieport disabled");
#endif

    setInteractive( true );

    mScene = new QOpenCVScene();

    setScene( mScene );
}

void QRobotGUIView::setJoypadSize( QSize bgSize, QSize thumbSize )
{
    double maxPos = (bgSize.width()-thumbSize.width()/2)/2;

    mMaxJoypadMove = maxPos;

    mScene->setJoypadSize( bgSize, thumbSize );
}

void QRobotGUIView::mousePressEvent(QMouseEvent *event)
{
    mBnDownPos = event->pos();
    mLastPos = mBnDownPos;

    QPointF posScene = mapToScene( mBnDownPos );

    mScene->buttonDown( posScene );

    qDebug() << Q_FUNC_INFO;
}

void QRobotGUIView::mouseReleaseEvent(QMouseEvent *event)
{
    mScene->buttonUp();

    qDebug() << Q_FUNC_INFO;
}

//void QRobotGUIView::resizeEvent(QResizeEvent * ev)
//{

//}

void QRobotGUIView::mouseMoveEvent(QMouseEvent *event)
{
    mLastPos = event->pos();

    QPointF posScene = mapToScene( mLastPos );
    QPointF centerPosScene = mapToScene( mBnDownPos );

    // >>>>> Let's keep the thumb inside the Joypad area
    double rho = qSqrt( (centerPosScene.x()-posScene.x())*(centerPosScene.x()-posScene.x()) +
            (centerPosScene.y()-posScene.y())*(centerPosScene.y()-posScene.y()) );

    double x = posScene.x()-centerPosScene.x();
    double y = posScene.y()-centerPosScene.y();

    if( rho>mMaxJoypadMove )
    {
        /*double alpha = qAtan2( posScene.y()- centerPosScene.y(), posScene.x()- centerPosScene.x() );
        double x = mMaxJoypadMove*qCos(alpha);
        double y = mMaxJoypadMove*qSin(alpha);*/

        double scale = mMaxJoypadMove/rho;
        x = (posScene.x()-centerPosScene.x())*scale;
        y = (posScene.y()-centerPosScene.y())*scale;

        posScene.setX( centerPosScene.x() + x );
        posScene.setY( centerPosScene.y() + y );
    }
    // <<<<< Let's keep the thumb inside the Joypad area

    mScene->mouseMove( posScene );

    float joyX = (float)x/(float)mMaxJoypadMove*100.0f;
    float joyY = (float)y/(float)mMaxJoypadMove*100.0f;

    emit newJoypadValues(joyX, joyY);
}


