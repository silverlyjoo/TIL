#include <iostream>

using namespace std;

int count = 100;

int Func(void);

int main() {
  Func();
  cout << "main: count = " << count << endl;
  return 0;
};

int Func(void) {
  int number = 10;
  cout << "Func: number = " << number << endl;
  cout << "Func: count = " << count << endl;
  return 0;
}