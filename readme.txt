Create a sample Flask application

Dockerize it (write Dockerfile)

Build the Docker image

Run the Docker container

Access the Flask app inside the container

I'll explain everything in detail. Let's begin:

Step 1: Create a Sample Flask Application
1.1 Install Flask (locally)
If you don't have Flask installed, install it:

bash
Copy
Edit
pip install Flask
1.2 Create a Project Directory
Create a folder for your project:

bash
Copy
Edit
mkdir flask_docker_app
cd flask_docker_app
1.3 Create the Flask App
Inside flask_docker_app/, create a file called app.py:

python
Copy
Edit
# app.py

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Flask inside Docker!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
Important:

host='0.0.0.0' tells Flask to accept connections from outside the container.

1.4 Create requirements.txt
This tells Docker which Python libraries to install.

bash
Copy
Edit
echo "Flask" > requirements.txt
Step 2: Create a Dockerfile
In the same folder, create a file called Dockerfile (no extension):

Dockerfile
Copy
Edit
# Use an official lightweight Python image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file first (for efficient docker caching)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port that Flask will run on
EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"]
Step 3: Build the Docker Image
From inside the flask_docker_app folder, run:

bash
Copy
Edit
docker build -t flask-docker-app .
-t flask-docker-app tags (names) the image.

. means the Dockerfile is in the current directory.

✅ If successful, you'll see a message like:

php-template
Copy
Edit
Successfully built <image_id>
Successfully tagged flask-docker-app:latest
Step 4: Run the Docker Container
Now, run the container:

bash
Copy
Edit
docker run -d -p 5000:5000 --name flask-container flask-docker-app
Explanation:

-d → run in detached (background) mode

-p 5000:5000 → map container's port 5000 to host's port 5000

--name flask-container → name your container

flask-docker-app → the image to run

✅ After this, Flask should be running inside the Docker container!

Step 5: Access the Flask Application
Open your browser and visit:

text
Copy
Edit
http://localhost:5000
You should see:

Hello from Flask inside Docker!

🎉 Congrats! Your Flask app is running inside a Docker container!

Extra Useful Commands
Command	What it does
docker ps	--->  List running containers
docker stop flask-container	---> Stop the container
docker start flask-container	---> Start it again
docker logs flask-container	---> See the logs from the container
docker images	---> List images
docker rm flask-container	---> Remove a stopped container
docker rmi flask-docker-app	---> Remove the image