// «адача 1 - нерекурсивное решение
#include <stdio.h>
//#include <string.h>
#include <cstdio>                               
#include <iostream>
#include <vector>

#define MAXN 100000

using namespace std;

const int inf = 1000*1000*1000;
vector <int> res(MAXN, inf);  // массив дл€ хранени€ значений функции


int f(int n) {
   int arg;
   if (n < 2) res[n] = n;
   else         // n >= 2
   if (n % 2 == 0) {    // четный аргумент
       arg = n/2;
       if (res[arg] != inf) 
            res[n] =  1 +  res[arg]; 
       else  res[n] = 1+ f(arg);
   } 
   else {   // нечетный аргумент
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

           //   считаем ответ на задачу:
      int count = 0;
      for (int n = 1; n <= x; n++) {
          int ff= res[n];
          if ((ff > 100) && (ff != inf)) count++;
   } 
   cout << count << endl;
   return 0;
}











