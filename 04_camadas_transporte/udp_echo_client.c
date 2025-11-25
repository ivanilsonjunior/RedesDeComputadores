/*
Cliente UDP (ECHO) — Exemplo Didático em C
Camada de Transporte — Redes de Computadores / ADS
DIATINF — IFRN

Objetivo:
    Demonstrar a implementação de um cliente UDP.
    O cliente envia uma mensagem ao servidor e tenta receber a resposta (ECHO).

Conceitos reforçados:
    - uso de socket UDP (SOCK_DGRAM)
    - comunicação sem conexão
    - sendto() e recvfrom()
    - possibilidade de perda de pacotes

Compilação:
    $ gcc udp_echo_client.c -o udp_echo_client

Execução:
    $ ./udp_echo_client

Requer:
    Servidor UDP em execução:
    $ ./udp_echo_server
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
    struct sockaddr_in servidor;
    char mensagem[TAM_BUFFER];
    char resposta[TAM_BUFFER];
    socklen_t tamanho = sizeof(servidor);
    int bytes_recebidos;

    // 1. Criar socket UDP
    sock = socket(AF_INET, SOCK_DGRAM, 0);
    if (sock < 0) {
        perror("Erro ao criar socket");
        exit(1);
    }

    printf("[*] Cliente UDP iniciado.\n");

    // 2. Configurar endereço do servidor
    servidor.sin_family = AF_INET;
    servidor.sin_port = htons(PORTA);
    servidor.sin_addr.s_addr = inet_addr("127.0.0.1");

    // 3. Loop de envio/recebimento
    while (1) {
        printf("Digite uma mensagem (ou 'sair'): ");
        fgets(mensagem, TAM_BUFFER, stdin);

        // Remover \n
        mensagem[strcspn(mensagem, "\n")] = 0;

        if (strcmp(mensagem, "sair") == 0)
            break;

        // 4. Enviar datagrama
        sendto(sock, mensagem, strlen(mensagem), 0,
               (struct sockaddr*)&servidor, tamanho);

        // 5. Tentar receber resposta
        bytes_recebidos = recvfrom(sock, resposta, TAM_BUFFER, 0,
                                   (struct sockaddr*)&servidor, &tamanho);

        if (bytes_recebidos < 0) {
            perror("Erro ao receber resposta (pode ter sido perdido)");
            continue;
        }

        resposta[bytes_recebidos] = '\0';

        printf("[ECHO] %s\n\n", resposta);
    }

    close(sock);
    printf("[*] Cliente UDP encerrado.\n");

    return 0;
}
