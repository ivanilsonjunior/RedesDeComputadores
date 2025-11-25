/*
Servidor UDP (ECHO) — Exemplo Didático em C
Camada de Transporte — Redes de Computadores / ADS
DIATINF — IFRN

Objetivo:
    Demonstrar a implementação de um servidor UDP simples.
    O servidor recebe datagramas de clientes e devolve o mesmo conteúdo.

Conceitos reforçados:
    - uso de socket UDP (SOCK_DGRAM)
    - comunicação sem conexão (connectionless)
    - recvfrom() e sendto()
    - ausência de garantia de entrega

Compilação:
    $ gcc udp_echo_server.c -o udp_echo_server

Execução:
    $ ./udp_echo_server

Teste:
    $ echo "teste" | nc -u 127.0.0.1 6000
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>

#define PORTA 6000
#define TAM_BUFFER 1024

int main() {
    int sock;
    struct sockaddr_in servidor, cliente;
    socklen_t tamanho_cliente;
    char buffer[TAM_BUFFER];
    int bytes_lidos;

    // 1. Criar socket UDP
    sock = socket(AF_INET, SOCK_DGRAM, 0);
    if (sock < 0) {
        perror("Erro ao criar socket");
        exit(1);
    }

    printf("[*] Socket UDP criado com sucesso.\n");

    // Preparar endereço de binding
    servidor.sin_family = AF_INET;
    servidor.sin_port = htons(PORTA);
    servidor.sin_addr.s_addr = INADDR_ANY;

    // 2. Associar socket à porta local
    if (bind(sock, (struct sockaddr*)&servidor, sizeof(servidor)) < 0) {
        perror("Erro no bind");
        exit(1);
    }

    printf("[*] Servidor UDP ouvindo em 0.0.0.0:%d\n", PORTA);

    tamanho_cliente = sizeof(cliente);

    // 3. Loop para receber e enviar datagramas
    while (1) {
        bytes_lidos = recvfrom(
            sock,
            buffer,
            TAM_BUFFER,
            0,
            (struct sockaddr*)&cliente,
            &tamanho_cliente
        );

        if (bytes_lidos < 0) {
            perror("Erro ao receber datagrama");
            continue;
        }

        buffer[bytes_lidos] = '\0';

        printf("[Recebido de %s:%d]: %s\n",
               inet_ntoa(cliente.sin_addr),
               ntohs(cliente.sin_port),
               buffer);

        // Enviar de volta (ECHO)
        sendto(
            sock,
            buffer,
            bytes_lidos,
            0,
            (struct sockaddr*)&cliente,
            tamanho_cliente
        );
    }

    close(sock);
    return 0;
}
