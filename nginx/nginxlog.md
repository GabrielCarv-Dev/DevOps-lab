
# Por que usar NGINX
    # EM produção real apps rodam atrás de um reversproxy
    # proxy de requisições HTTP na porta 80 para servições interno ( conteiners da api)
    # API não precisa expor porta diretamente (8000 do fastapi)
    # Possibilidade de load balancer