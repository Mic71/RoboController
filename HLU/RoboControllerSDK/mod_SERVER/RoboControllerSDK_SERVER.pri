message(Added SERVER module)

QT += network serialport

CONFIG += rcserver

SOURCES += \
        $$ROBOCONTROLLERSDKPATH/mod_SERVER/src/qrobotserver.cpp

INCLUDEPATH += \
        $$ROBOCONTROLLERSDKPATH/mod_SERVER/include/

HEADERS += \
        $$ROBOCONTROLLERSDKPATH/mod_SERVER/include/qrobotserver.h
