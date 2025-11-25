/*
Servidor TCP (ECHO) — Exemplo Didático em C
Camada de Transporte — Redes de Computadores / ADS
DIATINF — IFRN

Objetivo:
    Demonstrar como implementar um servidor TCP em C usando sockets.
    Este servidor recebe mensagens de um cliente e devolve o mesmo
    conteúdo (ECHO).

Conceitos reforçados:
    - criação de socket (SOCK_STREAM)
    - bind() para associar IP/porta
    - listen() para modo passivo
    - accept() para aceitar clientes
    - recv() e send() para comunicação
    - fechamento correto da conexão

Compilação:
    $ gcc tcp_echo_server.c -o tcp_echo_server

Execução:
    $ ./tcp_echo_server

Teste:
    $ telnet 127.0.0.1 5000
    ou
    $ nc 127.0.0.1 5000
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>

#define PORTA 5000
#define TAM_BUFFER 1024

int main() {
    int servidor, cliente;
    struct sockaddr_in endereco_servidor, endereco_cliente;
    socklen_t tamanho_cliente;
    char buffer[TAM_BUFFER];
    int bytes_lidos;

    // 1. Criar socket TCP
    servidor = socket(AF_INET, SOCK_STREAM, 0);
    if (servidor < 0) {
        perror("Erro ao criar socket");
        exit(1);
    }

    printf("[*] Socket criado com sucesso.\n");

    // 2. Preparar estrutura do servidor
    endereco_servidor.sin_family = AF_INET;
    endereco_servidor.sin_addr.s_addr = INADDR_ANY;
    endereco_servidor.sin_port = htons(PORTA);

    // 3. Associar (bind)
    if (bind(servidor, (struct sockaddr*)&endereco_servidor, sizeof(endereco_servidor)) < 0) {
        perror("Erro no bind");
        exit(1);
    }

    printf("[*] Bind realizado em 0.0.0.0:%d\n", PORTA);

    // 4. Colocar socket em modo de escuta
    if (listen(servidor, 5) < 0) {
        perror("Erro no listen");
        exit(1);
    }

    printf("[*] Servidor TCP aguardando conexões...\n");

    // Loop principal de atendimento
    while (1) {
        tamanho_cliente = sizeof(endereco_cliente);

        // 5. Aceitar cliente
        cliente = accept(servidor, (struct sockaddr*)&endereco_cliente, &tamanho_cliente);
        if (cliente < 0) {
            perror("Erro no accept");
            continue;
        }

        printf("[+] Cliente conectado de %s:%d\n",
               inet_ntoa(endereco_cliente.sin_addr),
               ntohs(endereco_cliente.sin_port));

        // 6. Comunicação com cliente
        while ((bytes_lidos = recv(cliente, buffer, TAM_BUFFER, 0)) > 0) {
            buffer[bytes_lidos] = '\0';
            printf("[Recebido]: %s\n", buffer);

            // Enviar de volta (ECHO)
            send(cliente, buffer, bytes_lidos, 0);
        }

        printf("[-] Cliente desconectado.\n");
        close(cliente);
    }

    close(servidor);
    return 0;
}
