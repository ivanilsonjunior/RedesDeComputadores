/*
 * Cliente TCP (Camada de Transporte)
 *
 * Objetivo didático:
 *   - Conectar-se a um servidor TCP.
 *   - Enviar mensagens e receber respostas.
 *
 * Compilação:
 *     $ gcc tcp_echo_client.c -o tcp_echo_client
 *
 * Execução:
 *     $ ./tcp_echo_client
 */

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <arpa/inet.h>

#define PORTA 5000
#define BUF 1024

int main() {
    int sock;
    struct sockaddr_in servidor;
    char buffer[BUF];

    sock = socket(AF_INET, SOCK_STREAM, 0);
    if (sock < 0) {
        perror("Erro ao criar socket");
        exit(1);
    }

    servidor.sin_family = AF_INET;
    servidor.sin_port = htons(PORTA);
    servidor.sin_addr.s_addr = inet_addr("127.0.0.1");

    printf("[*] Conectando ao servidor...\n");
    if (connect(sock, (struct sockaddr*)&servidor, sizeof(servidor)) < 0) {
        perror("Erro em connect");
        exit(1);
    }

    printf("[+] Conectado!\n");

    while (1) {
        printf("> ");
        fgets(buffer, BUF, stdin);

        if (strncmp(buffer, "sair", 4) == 0)
            break;

        send(sock, buffer, strlen(buffer), 0);

        int lidos = recv(sock, buffer, BUF - 1, 0);
        buffer[lidos] = '\0';

        printf("[<] Resposta: %s", buffer);
    }

    close(sock);
    return 0;
}
