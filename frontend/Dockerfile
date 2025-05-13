# Use Node.js as the base image
FROM node:16

# Set the working directory
WORKDIR /app

# Copy the frontend code
COPY . .

# Install dependencies
RUN npm install

# Expose the frontend port
EXPOSE 3000

# Run the application
CMD ["npm", "start"]