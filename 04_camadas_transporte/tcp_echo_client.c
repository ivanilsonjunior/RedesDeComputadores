/*
Cliente TCP (ECHO) — Exemplo Didático em C
Camada de Transporte — Redes de Computadores / ADS
DIATINF — IFRN

Objetivo:
    Demonstrar como implementar um cliente TCP em C usando sockets.
    O cliente se conecta ao servidor, envia mensagens e imprime a
    resposta (ECHO).

Conceitos reforçados:
    - criação de socket (SOCK_STREAM)
    - connect() para estabelecer conexão
    - send() e recv() para comunicação
    - fechamento correto do socket

Compilação:
    $ gcc tcp_echo_client.c -o tcp_echo_client

Execução:
    $ ./tcp_echo_client

Requer:
    O servidor tcp_echo_server.c deve estar rodando.
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>

#define PORTA 5000
#define TAM_BUFFER 1024

int main() {
    int sock;
    struct sockaddr_in servidor;
    char mensagem[TAM_BUFFER];
    char resposta[TAM_BUFFER];
    int bytes_recebidos;

    // 1. Criar socket TCP
    sock = socket(AF_INET, SOCK_STREAM, 0);
    if (sock < 0) {
        perror("Erro ao criar socket");
        exit(1);
    }

    printf("[*] Socket criado com sucesso.\n");

    // 2. Preparar endereço do servidor
    servidor.sin_family = AF_INET;
    servidor.sin_port = htons(PORTA);
    servidor.sin_addr.s_addr = inet_addr("127.0.0.1"); // localhost

    // 3. Conectar ao servidor
    if (connect(sock, (struct sockaddr*)&servidor, sizeof(servidor)) < 0) {
        perror("Erro ao conectar ao servidor");
        exit(1);
    }

    printf("[+] Conectado ao servidor TCP em 127.0.0.1:%d\n\n", PORTA);

    // 4. Loop de comunicação
    while (1) {
        printf("Digite uma mensagem (ou 'sair'): ");
        fgets(mensagem, TAM_BUFFER, stdin);

        // Remover \n
        mensagem[strcspn(mensagem, "\n")] = 0;

        if (strcmp(mensagem, "sair") == 0)
            break;

        // Enviar ao servidor
        send(sock, mensagem, strlen(mensagem), 0);

        // Receber resposta
        bytes_recebidos = recv(sock, resposta, TAM_BUFFER, 0);
        if (bytes_recebidos <= 0) {
            printf("[-] Conexão encerrada pelo servidor.\n");
            break;
        }

        resposta[bytes_recebidos] = '\0';
        printf("[ECHO] %s\n\n", resposta);
    }

    // 5. Fechar conexão
    close(sock);
    printf("[*] Cliente finalizado.\n");

    return 0;
}
