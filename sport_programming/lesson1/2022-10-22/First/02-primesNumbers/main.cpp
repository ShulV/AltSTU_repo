// ����� �������������� ���������� �� k  ��������� � ������� a
//    a, a+1, a+2, ... , m+k-1
// ����� (a+a+k-1) * k / 2   =  (2*a + k-1)*k/2   =  y
// ������: ����� ���������� ������ a ��� ��������� y
// a*k +  (k-1)*k/2= y  
// 2*a*k + (k-1)*k = 2*y , k>1
// ���� k=2, �� ��� ������ k ���� ���� �������
// k(2a + k -1) = 2y
// ��� ���� k  >2,  ��������� n, ���� ������� 
//    


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

ll y;  // y - �������� �����
int  primeNumbers[MAXPRIMES], nprimes = 0,  primeCount[MAXPRIMES]; 
ll del[4000],k=0;

const ll ONE =  1;
const ll MAXN =  ONE << 31;

void setPrimes()  {  	// setup primes
   primeNumbers[0] = 2;
   primeNumbers[1] = 3;
   nprimes = 2;
   bool isprime;
   for (int i = 5 ; i < (2 << 16) ; i+=2) {
      isprime = true;
      for (int j=0 ; j < nprimes ; j++) 
         if ((i % primeNumbers[j]) == 0) {
            isprime = false;
            break;
      }
      if (isprime) {
         primeNumbers[nprimes++] = i;
         cout << "prime number = " << nprimes  << "   "<< i << endl; 
      }
   }
}



map<ll,int> memory;


ll go() {
   int number;
   cin >> number;
   cin >> y;  
   assert( y <= MAXN);
   memset(del, 0, sizeof(del));
   memset(primeCount, 0, sizeof(primeCount));
   memory.clear(); 
   
   for (int i = 0; i < nprimes; i++) {
      int yy = y;
      while (yy % primeNumbers[i] == 0) {
         primeCount[i]++;  
         yy = yy / primeNumbers[i];
      }
   }
   k = 0;
   int oldk=k, newk=k;
   for (int i = 0 ; (i < nprimes) && (primeNumbers[i] <= y) ; i++) {  
               // i = ����� �������� �����
      if (primeCount[i] == 0) continue;
      int t = primeNumbers[i];
      oldk = k; 
      for (int j = 0; j < primeCount[i]; j++) {
         del[k++] = t;  memory[t] = 1;
         t *= primeNumbers[i];
      }

// ��������� �������� �� ������� �����, ������� �� ����� ����� �� y
      newk = k;
      for (int jj = 0; jj < oldk; jj++)
         for (int ii = oldk; ii < k; ii++) {
            del[newk++] = del[jj]*del[ii];
            memory[del[jj]*del[ii]] = 1;
         }
      k = newk;
   }

// �������� �������� �������� �������:
   for (int i = 0 ; i < newk  ; i++) {  // i = ����� ��������
       ll yy = y / del[i], zz = yy * del[i];
         if ( (zz == y) && (yy > 1) ) {
            if ( memory.find(yy) == memory.end() ) {
                   del[k++]= yy; 
            }
         }
   }

   int count = 0;
// (a + a + n - 1)/2 * n == y
//  n*(2*a + n - 1) == 2y  
// y ������ n
// (2*a + n - 1) == 2*(y/n)
// 2*a == 2*(y/n) -  n + 1
cout << y << endl; 
   for (int i = 0; i < k; i++){
      if (del[i] == y) continue;
      ll n = del[i], b = 2 * (y/n) - n + 1;
//cout << "y = " << y << "   del  = " << n << "   b = " << b << endl;
      ll a = b/2;
      if (a * 2 == b) {count++ ;   cout<< a << endl;}
   }
   if (y % 2 ) count ++;  // �������� ������ ����� ����� ������� � ���������: 9=4+5, 17=8+9, 101 = 50+51,...
   cout<< number << " " << count << endl; 
   return count;
}


#define MAXTEST 1000
int main()  {
    freopen("output.txt","w",stdout);
    freopen("input.txt","r",stdin);
    setPrimes(); return 0;

    int testCount;                 
    cin >> testCount;
    assert( testCount <= MAXTEST);
    for (int i = 0; i < testCount; i++)   {
          go(); 
    }
    return 0;
}

