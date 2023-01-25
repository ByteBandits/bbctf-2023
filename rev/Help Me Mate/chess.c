#include <stdbool.h>
#include <stdio.h>

char b[8][8] = {' '};
const int ndirx[] = {2, 1, -1, -2, 2, 1, -1, -2};
const int ndiry[] = {1, 2, 2, 1, -1, -2, -2, -1};

const int kdiry[] = {-1, 0, 1, -1, 1, -1, 0, 1};
const int kdirx[] = {1, 1, 1, 0, 0, -1, -1, -1};

int findKing(int white) {
    for (int i = 0; i < 8; i++) {
        for (int j = 0; j < 8; j++) {
            if (white && b[i][j] == 'K') return i * 8 + j;
            if (!white && b[i][j] == 'k') return i * 8 + j;
        }
    }
    return -1;
}

bool isCheckb(int x, int y) {
    for (int i = 0; i < 8; i++) {
        int nx = x + ndirx[i], ny = y + ndiry[i];
        if (nx < 0 || nx > 7 || ny < 0 || ny > 7) continue;
        if (b[nx][ny] == 'N') return 1;
    }

    for (int i = x - 1, j = y - 1; i >= 0 && j >= 0; i--, j--) {
        if (b[i][j] == 'B') return 1;
        if (b[i][j] != ' ') break;
    }

    for (int i = x + 1, j = y + 1; i < 8 && j < 8; i++, j++) {
        if (b[i][j] == 'B') return 1;
        if (b[i][j] != ' ') break;
    }
    for (int i = x - 1, j = y + 1; i >= 0 && j < 8; i--, j++) {
        if (b[i][j] == 'B') return 1;
        if (b[i][j] != ' ') break;
    }
    for (int i = x + 1, j = y - 1; i < 8 && j >= 0; i++, j--) {
        if (b[i][j] == 'B') return 1;
        if (b[i][j] != ' ') break;
    }

    for (int i = 0; i < 8; i++) {
        int nx = x + kdirx[i], ny = y + kdiry[i];
        if (nx < 0 || nx > 7 || ny < 0 || ny > 7) continue;
        if (b[nx][ny] == 'K') return 1;
    }

    return 0;
}

bool isCheckw(int x, int y) {
    for (int i = 0; i < 8; i++) {
        int nx = x + kdirx[i], ny = y + kdiry[i];
        if (nx < 0 || nx > 7 || ny < 0 || ny > 7) continue;
        if (b[nx][ny] == 'k') return 1;
    }

    if (x + 1 < 8 && y - 1 >= 0 && (b[x + 1][y - 1] == 'p')) return 1;
    if (x + 1 < 8 && y + 1 < 8 && (b[x + 1][y + 1] == 'p')) return 1;

    return 0;
}

bool isLegal(int x1, int y1, int x2, int y2, int white) {
    int p = b[x1][y1];
    int p2 = b[x2][y2];
    if (p == ' ') return 0;
    if ((white && isLower(p)) || (!white && isUpper(p))) return 0;
    if ((isUpper(p) && isUpper(p2)) || (isLower(p) && isLower(p2))) return 0;
    if (x1 == x2 && y1 == y2) return 0;

    if (white) {
    } else {
        if (p == 'k') {
            int dx = abs(x1 - x2), dy = abs(y1 - y2);
            if (dx > 1 || dy > 1) return 0;

            b[x1][y1] = ' ';
            b[x2][y2] = 'k';

            if (isCheckb(x2, y2)) return 0;

        } else if (p == 'p') {
            if (abs(y1 - y2) > 1 || x1 - x2 > 2 || x1 - x2 < 0) return 0;
            // capture
            if (y1 != y2) {
                if (abs(x1 - x2) != 1) return 0;
                if (!(b[x2][y2] == 'N' || b[x2][y2] == 'B')) return 0;

            } else {
                if (b[x2][y2] != ' ') return 0;
                if (x1 - x2 == 2 && (x1 != 6 || b[x1 - 1][y1] != ' ')) return 0;
            }

            b[x1][y1] = ' ';
            b[x2][y2] = 'p';
            int k = findKing(1 - white);
            if (isCheckb(k / 8, k % 8)) return 0;
        }
    }
}

bool isValidSqaure(int x, int y) {
    if (x < 0 || x > 7 || y < 0 || y > 7) return 0;
    return 1;
}

bool isCheckMateb() {
    int k = findKing(0), x = k / 8, y = k % 8, nx, ny;
    if (!isCheckb(x, y)) return 0;

    for (int i = 0; i < 8; i++) {
        nx = x + kdirx[i], ny = y + kdiry[i];
        if (!isValidSqaure(nx, ny) || isLower(b[nx][ny])) continue;
        char prev = b[nx][ny];
        b[nx][ny] = 'k';
        b[x][y] = ' ';

        if (!isCheckb(nx, ny)) {
            b[nx][ny] = prev;
            b[x][y] = 'k';
            return 0;
        }
    }
    return 1;
}

int main() {
    int n, t=10;
    int x1, y1, x2, y2, white = 1;
    while (t--) {
        scanf("%d", &n);
        n %= 4096;
        y2 = n & 7;
        n >>= 3;
        x2 = n & 7;
        n >>= 3;
        y1 = n & 7;
        n >>= 3;
        x1 = n & 7;

        if(!isLegal(x1, y1, x2, y2, white)){
            printf("Wrong number!");
            return 0;
        };

        white = 1 - white;
    }
}