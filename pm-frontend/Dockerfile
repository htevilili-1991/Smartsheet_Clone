# Use an official node runtime as a parent image
FROM node:22-alpine

# Set work directory
WORKDIR /app

# Install dependencies
COPY package.json ./
COPY package-lock.json ./
RUN npm install

# Copy project
COPY . .

# Expose port
EXPOSE 5173

# Run the app
CMD ["npm", "run", "dev", "--", "--host"]
