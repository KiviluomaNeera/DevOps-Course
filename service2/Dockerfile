# Use Node.js base image
FROM node:18

# Set working directory
WORKDIR /app

# Copy the app code to the container
COPY . .

# Install dependencies
RUN npm install express

# Expose port 3000
EXPOSE 3000

# Run the application
CMD ["node", "app.js"]
