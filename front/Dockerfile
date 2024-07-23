FROM node:18.20-bookworm AS builder

WORKDIR /app

COPY . .

RUN npm install

# Build the Next.js application
RUN npm run build

# Stage 2: Serve the application
FROM node:18.20-bookworm as production

WORKDIR /app

COPY --from=builder /app/package*.json ./
COPY --from=builder /app/.next ./.next
COPY --from=builder /app/public ./public
COPY --from=builder /app/node_modules ./node_modules

RUN npm install -g serve

EXPOSE 3000

CMD ["serve", "-s", "build", "-l", "3000"]
