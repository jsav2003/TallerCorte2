FROM openjdk:17-slim
WORKDIR /app
COPY Figuras/ ./
RUN javac -cp . -d classes src/main/java/org/example/*.java
CMD ["java", "-cp", "classes", "org.example.Main"] 
