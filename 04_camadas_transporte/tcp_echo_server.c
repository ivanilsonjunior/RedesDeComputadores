/*
 * Servidor de eco TCP (Camada de Transporte)
 *
 * Objetivo didático:
 *    - Mostrar a criação de um socket TCP em C.
 *    - Demonstrar bind, listen, accept, recv e send.
 *    - A cada mensagem recebida, o servidor devolve a mesma mensagem.
 *
 * Compilação:
 *    $ gcc tcp_echo_server.c -o tcp_echo_server
 *
 * Execução:
 *    $ ./tcp_echo_server
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>         // close
#include <arpa/inet.h>      // struct sockaddr_in, inet_ntoa
#include <netinet/in.h>     // IPPROTO_TCP, INADDR_ANY

#define PORTA   5000
#define BACKLOG 5
#define BUF_TAM 1024

int main(void) {
    int sock_servidor, sock_cliente;
    struct sockaddr_in endereco_servidor;
    struct sockaddr_in endereco_cliente;
    socklen_t tamanho_endereco_cliente;
    char buffer[BUF_TAM];

    // Cria socket TCP (IPv4)
    sock_servidor = socket(AF_INET, SOCK_STREAM, 0);
    if (sock_servidor < 0) {
        perror("Erro ao criar socket");
        exit(EXIT_FAILURE);
    }

    // Permite reuso de porta
    int opt = 1;
    if (setsockopt(sock_servidor, SOL_SOCKET, SO_REUSEADDR, &opt, sizeof(opt)) < 0) {
        perror("Erro em setsockopt");
        close(sock_servidor);
        exit(EXIT_FAILURE);
    }

    // Preenche estrutura de endereço do servidor
    memset(&endereco_servidor, 0, sizeof(endereco_servidor));
    endereco_servidor.sin_family = AF_INET;
    endereco_servidor.sin_addr.s_addr = INADDR_ANY;
    endereco_servidor.sin_port = htons(PORTA);

    // Associa (bind)
    if (bind(sock_servidor, (struct sockaddr *)&endereco_servidor, sizeof(endereco_servidor)) < 0) {
        perror("Erro em bind");
        close(sock_servidor);
        exit(EXIT_FAILURE);
    }

    // Coloca em modo de escuta (listen)
    if (listen(sock_servidor, BACKLOG) < 0) {
        perror("Erro em listen");
        close(sock_servidor);
        exit(EXIT_FAILURE);
    }

    printf("[*] Servidor de eco TCP escutando na porta %d\n", PORTA);

    while (1) {
        printf("[*] Aguardando conexão...\n");
        tamanho_endereco_cliente = sizeof(endereco_cliente);

        // Aceita conexão de um cliente
        sock_cliente = accept(sock_servidor,
                              (struct sockaddr *)&endereco_cliente,
                              &tamanho_endereco_cliente);
        if (sock_cliente < 0) {
            perror("Erro em accept");
            continue;
        }

        printf("[+] Cliente conectado: %s:%d\n",
               inet_ntoa(endereco_cliente.sin_addr),
               ntohs(endereco_cliente.sin_port));

        // Loop de eco
        ssize_t lidos;
        while ((lidos = recv(sock_cliente, buffer, BUF_TAM - 1, 0)) > 0) {
            buffer[lidos] = '\0';  // Garante terminação em string
            printf("[>] Recebido: %s", buffer);

            // Envia de volta (eco)
            if (send(sock_cliente, buffer, lidos, 0) < 0) {
                perror("Erro ao enviar dados");
                break;
            }
        }

        if (lidos == 0) {
            printf("[-] Cliente encerrou a conexão.\n");
        } else if (lidos < 0) {
            perror("Erro em recv");
        }

        close(sock_cliente);
    }

    // Fecha socket do servidor (na prática, nunca chega aqui)
    close(sock_servidor);
    return 0;
}
