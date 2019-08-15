#include <iostream>

using namespace std;

int main() {
  enum languages { c = 10, cplusplus = 20, java = 30 } myLanguage;

  myLanguage = cplusplus;
  cout << "cplusplus = " << myLanguage << endl;
  return 0;
}