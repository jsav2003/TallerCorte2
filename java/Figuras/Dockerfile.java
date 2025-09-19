# Stage 1: build con Maven
FROM maven:3-openjdk-17-slim AS build

WORKDIR /app
COPY pom.xml .
COPY src ./src
RUN mvn clean package -DskipTests

# Stage 2: runtime
FROM openjdk:17-slim

WORKDIR /app
COPY --from=build /app/target/sistema-figuras-geometricas-1.0.0-all.jar app.jar
ENTRYPOINT ["java","-cp","app.jar","org.example.Main"]
