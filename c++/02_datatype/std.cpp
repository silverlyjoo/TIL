#include <iostream>

using namespace std;

int main() {
  int number;
  char letter;
  float rnumber;

  cout << "정수 문자 실수 순서로 입력하세요. --> ";
  cin >> number >> letter >> rnumber;
  cout << "당신이 입력한 정수는 " << number << "입니다. " << endl;
  cout << "당신이 입력한 문자는 " << letter << "입니다. " << endl;
  cout << "당신이 입력한 실수는 " << rnumber << "입니다." << endl;

  return 0;
};