// Стандартный алгоритм генерации шкалы простых чисел
#include <assert.h>

#include <stdio.h>

static char s[66000];
static unsigned p[66000];

int main() {
    freopen("output.txt","w",stdout);
    freopen("input.txt","r",stdin);

    unsigned sp = 1, i, N, n, np=0;
    while(1) {
	sp++;
	if( sp >= 66000 ) break;
	if( s[sp] ) continue;
	p[np++] = sp;
	for( i=sp*2; i<66000; i+=sp ) s[i] = 1;
    }
    scanf( "%u ", &N );
    assert ( N <= 2000 );
    while(N--) {
	scanf( "%u ", &n );
if (n >4200000000L) printf( "!!! %u \n" ,n);
        assert ( n <= 4200000000L);
	if(n<2) n=2;
	while(1) {
	    for(i=0;i<np&&p[i]*p[i]<=n;i++) if( (n%p[i]) == 0 ) goto next;
	    printf( "%u\n", n );
	    break;
next:;
	    n++;
	}
    }
return 0;
}
