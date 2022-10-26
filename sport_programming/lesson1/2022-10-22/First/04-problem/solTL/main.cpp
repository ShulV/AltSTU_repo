// сумма арифметической прогрессии из k  элементов с началом a
//    a, a+1, a+2, ... , m+k-1
// равна (a+a+k-1) * k / 2   =  (2*a + k-1)*k/2   =  y
// ЗАДАЧА: найти количество разеых a для заданного y
// a*k +  (k-1)*k/2= y  
// 2*a*k + (k-1)*k = 2*y , k>1      (1)
// перебираем k от 2 до  sqrt (y) +1
// находим a = (2*y - (k-1)*k ) / (2*k) 
// если (1) выполняется, то res++   


#include <math.h>
#include <assert.h>
#include <cstdio>                               
#include <cstring>
#include <algorithm>
#include <map>
#include <iostream>
#define MAXPRIMES 20000

using namespace std;

typedef long long int ll;

ll y;  // y - исходное число


#define MAXTEST 1000


void go() {
   int number;
   cin >> number;
   cin >> y;  

   int res = 0, nn = sqrt ((double) y * 2) + 10;
 
   for (int k = 2; k <= nn; k++){
      ll a  =  (2*y - (k-1)*k ) / (2*k) ;
      if (a <= 0) continue;
      if ( (a + a + k - 1) * k == y*2 ) res++ ;   
   }
   cout<< number << " " << res << endl; 
}


int main()  {
    freopen("output.txt","w",stdout);
    freopen("input.txt","r",stdin);

    int testCount;                 
    cin >> testCount;
    assert( testCount <= MAXTEST);
    for (int i = 0; i < testCount; i++)   {
          go(); 
    }
    return 0;
}

