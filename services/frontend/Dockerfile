# syntax=docker/dockerfile:1.7
FROM node:20.17.0-alpine AS deps
WORKDIR /app
COPY services/frontend/package.json services/frontend/package-lock.json* ./
RUN npm ci --ignore-scripts --no-audit --no-fund

FROM node:20.17.0-alpine AS builder
WORKDIR /app
COPY --from=deps /app/node_modules ./node_modules
COPY services/frontend .
RUN npm run build

FROM node:20.17.0-alpine AS runner
WORKDIR /app
ENV NODE_ENV=production
USER node
COPY --from=builder /app/.next ./.next
COPY --from=builder /app/public ./public
COPY --from=builder /app/package.json ./package.json
COPY --from=deps /app/node_modules ./node_modules
EXPOSE 3000
CMD ["npm", "start"]