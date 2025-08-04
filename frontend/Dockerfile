# Stage 1: Build the Svelte app
FROM node:20 AS builder

WORKDIR /app

# Copy package files and install dependencies
COPY package*.json ./
RUN npm install

# Copy source code and build
COPY . .
RUN npm run build

# Stage 2: Serve using Nginx
FROM nginx:alpine

# Create subfolder for the impersonator app
RUN mkdir -p /usr/share/nginx/html/impersonator

# Copy built assets into that subfolder
COPY --from=builder /app/dist/ /usr/share/nginx/html/impersonator/

# Replace default Nginx config
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Expose port (used by docker-compose)
EXPOSE 80

# Run Nginx in the foreground
CMD ["nginx", "-g", "daemon off;"]
