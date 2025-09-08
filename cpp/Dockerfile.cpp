FROM gcc:12
WORKDIR /app
COPY Figuras/Figuras/ ./
RUN g++ -o figuras \
    Main.cpp \
    Circulo.cpp \
    Cuadrado.cpp \
    Cubo.cpp \
    Esfera.cpp \
    Figura.cpp \
    Gestionar.cpp
CMD ["./figuras"] 
