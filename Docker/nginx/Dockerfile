# Dockerfile
FROM nginx:1.27.0-alpine

# Copy the custom nginx config
COPY nginx.conf /etc/nginx/nginx.conf

# Create the directory where nginx expects files
RUN mkdir -p /usr/share/nginx/html

# Copy the necessary files into the correct directory
COPY index.php site.html /usr/share/nginx/html/

# Expose port 80
EXPOSE 80

# Command to run nginx in the background
CMD ["nginx", "-g", "daemon off;"]
