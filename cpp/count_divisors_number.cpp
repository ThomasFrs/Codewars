#include <iostream>
#include <cmath>

using namespace std;

int divisors(int number){
  int divisor_count = 0;

  for (int i = 1; i < floor(pow(number, 0.5)) + 1; i++){
    if (number % i == 0){
      if (i == pow(number, 0.5))
        divisor_count++;
      else
        divisor_count += 2;
    }
  }
  return divisor_count;
}

int main(){
  cout << divisors(500000) << endl;
  return 0;
}