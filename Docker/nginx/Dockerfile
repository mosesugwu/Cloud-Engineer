FROM nginx:1.27.0-alpine

# Copy the custom nginx config if necessary
COPY nginx.conf /etc/nginx/nginx.conf

# Create the directory where nginx expects files, if not already present
RUN mkdir -p /usr/share/nginx/html

# Copy the site.html into the correct directory
COPY booking.html site.html /usr/share/nginx/html/
 
# Expose port 80
EXPOSE 80

# Command to run nginx in the background
CMD [ "nginx", "-g", "daemon off;" ] 


