# Stage 1: build con Maven
FROM maven:3-openjdk-17-slim AS build

WORKDIR /app/Figuras
COPY pom.xml .
COPY src ./src
RUN mvn clean package -DskipTests

# Stage 2: runtime
FROM openjdk:17-slim

WORKDIR /app/Figuras
COPY --from=build /app/Figuras/target/sistema-figuras-geometricas-1.0.0-all.jar app.jar
ENTRYPOINT ["java","-jar","app.jar"]
