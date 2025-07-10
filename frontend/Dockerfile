# frontend/Dockerfile
# --- Estágio 1: Build ---
FROM node:20-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

# --- Estágio 2: Produção ---
FROM nginx:stable-alpine
# Copia os ficheiros estáticos construídos no estágio anterior
COPY --from=builder /app/dist /usr/share/nginx/html
# Copia a configuração do Nginx
COPY nginx.conf /etc/nginx/conf.d/default.conf
# Expõe a porta 80
EXPOSE 80
# Comando para iniciar o Nginx
CMD ["nginx", "-g", "daemon off;"]
