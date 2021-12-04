#include <bits/stdc++.h>

using namespace std;
int main(int argc, char** argv) {
    FILE *fout = fopen(argv[2], "r");
    
    long long shit = 100000001; 
    fscanf(fout, "%lld", &shit);
    
    int key = shit / 100000000;
    int V = (shit % 100000000) / 10000;
    int N = shit % 10000;    
    if(key == 127382876){
        printf("0.0\n");
        if(V < 1 or V > 20) V = 1010101;
                fprintf(stderr, "Wrong Answer [%d]", V);
    }
    else if(key == 756688401){
        if(N <= 40){
            printf("1.0\n");
                    fprintf(stderr, "Accepted");
        }
        else{
            int d = V-N;
            if(d >= 101){
                printf("0.0\n");
                fprintf(stderr, "Accepted but V-N too large");
            }
            else{
                if(d >= 21){
                    printf("%f", (0.005 * (100.0f-d)*(100.0f-d) + 9.99) * 1.25 / 100);
                }
                else{
                    map<int,double> scores;
                    scores[12] = 80;
                    scores[13] = 65.9;
                    scores[14] = 62.8;
                    scores[15] = 55.7;
                    scores[16] = 52.6;
                    scores[17] = 49.5;
                    scores[18] = 47.4;
                    scores[19] = 45.3;
                    scores[20] = 43.2;

                    double s = scores[d];
                    s = s * 1.25 / 100.0f;
                    if(d <= 12) s = 1.0;
                    printf("%f", s);
                }
                fprintf(stderr, "Accepted, V-N = %d", d);
            }
        }    
    }
    else{
        printf("0.0\n");
        fprintf(stderr, "idk what you did, pls don't do that");
    }
    return 0;
}
