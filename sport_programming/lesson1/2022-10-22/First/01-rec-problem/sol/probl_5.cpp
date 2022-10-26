// ������ 1 - ������������� �������
#include <stdio.h>
//#include <string.h>
#include <cstdio>                               
#include <iostream>
#include <vector>

#define MAXN 100000

using namespace std;

const int inf = 1000*1000*1000;
vector <int> res(MAXN, inf);  // ������ ��� �������� �������� �������


int f(int n) {
   int arg;
   if (n < 2) res[n] = n;
   else         // n >= 2
   if (n % 2 == 0) {    // ������ ��������
       arg = n/2;
       if (res[arg] != inf) 
            res[n] =  1 +  res[arg]; 
       else  res[n] = 1+ f(arg);
   } 
   else {   // �������� ��������
      arg = 3 * n + 1;
       if ( res[arg] != inf)
              res[n] = res[arg] + 1;
      else res[n] = 1 + f(arg);
   }
   return res[n];
}


int main()  {

   int x;
   cin >> x;

   for (int n =0; n <= x; n++ ) {
      int ff = f(n);
   } 

           //   ������� ����� �� ������:
      int count = 0;
      for (int n = 1; n <= x; n++) {
          int ff= res[n];
          if ((ff > 100) && (ff != inf)) count++;
   } 
   cout << count << endl;
   return 0;
}











