#include <stdio.h>

#define N 5
#define M 1000  // Representasi untuk "tak hingga"

// Prototipe fungsi
void Tampil(int data[N][N], const char *judul);
void Warshall(int Q[N][N], int P[N][N], int R[N][N]);
void TampilkanRute(int R[N][N], int Beban[N][N], int start, int end);

// Fungsi untuk menampilkan matriks
void Tampil(int data[N][N], const char *judul) {
    printf("%s =\n", judul);
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            if (data[i][j] >= M)
                printf(" M ");
            else
                printf("%2d ", data[i][j]);
        }
        printf("\n");
    }
    printf("\n");
}

// Algoritma Warshall
void Warshall(int Q[N][N], int P[N][N], int R[N][N]) {
    for (int k = 0; k < N; k++)
        for (int i = 0; i < N; i++)
            for (int j = 0; j < N; j++) {
                P[i][j] = P[i][j] | (P[i][k] & P[k][j]);
                if (Q[i][k] + Q[k][j] < Q[i][j]) {
                    Q[i][j] = Q[i][k] + Q[k][j];
                    R[i][j] = R[i][k] != 0 ? R[i][k] : k + 1;
                }
            }
}

// Fungsi untuk menampilkan rute dengan Stack
void TampilkanRute(int R[N][N], int Beban[N][N], int start, int end) {
    int stack[N];
    int top = -1;
    int asal = start;
    int tujuan = end;

    // Isi stack dengan titik-titik perantara
    while (R[asal][tujuan] != 0) {
        stack[++top] = R[asal][tujuan];
        tujuan = R[asal][tujuan] - 1;
    }

    // Tampilkan jalur
    printf("Rute dari %d ke %d: %d", start + 1, end + 1, start + 1);
    while (top >= 0) {
        printf("-%d", stack[top--]);
    }
    printf("-%d\n", end + 1);

    // Tampilkan beban minimal
    printf("Beban minimal: %d\n\n", Beban[start][end]);
}

int main() {
    int Beban[N][N] = {
        { M,  1,  3,  M,  M },
        { M,  M,  1,  M,  5 },
        { 3,  M,  M,  2,  M },
        { M,  M,  M,  M,  1 },
        { M,  M,  M,  M,  M }
    };

    int Jalur[N][N] = {
        { 0, 1, 1, 0, 0 },
        { 0, 0, 1, 0, 1 },
        { 1, 0, 0, 1, 0 },
        { 0, 0, 0, 0, 1 },
        { 0, 0, 0, 0, 0 }
    };

    int Rute[N][N] = { 0 };

    printf("Matriks sebelum Algoritma Warshall:\n");
    Tampil(Beban, "Beban");
    Tampil(Jalur, "Jalur");
    Tampil(Rute, "Rute");

    Warshall(Beban, Jalur, Rute);

    printf("Matriks setelah Algoritma Warshall:\n");
    Tampil(Beban, "Beban (Jarak Terpendek)");
    Tampil(Jalur, "Jalur (Transitive Closure)");
    Tampil(Rute, "Rute (Penelusuran Jalur)");

    // Contoh pemanggilan fungsi TampilkanRute
    TampilkanRute(Rute, Beban, 0, 4);  // Rute 1 ke 5
    TampilkanRute(Rute, Beban, 0, 3);  // Rute 1 ke 4
    TampilkanRute(Rute, Beban, 2, 4);  // Rute 3 ke 5

    return 0;
}
