#include <iostream>

using namespace std;

namespace NS1 {
int number;
void Test() { cout << "NS1:: Test called number = " << number << endl; }
}  // namespace NS1

namespace NS2 {
int number;
void Test() { cout << "NS2:: Test called number = " << number << endl; }
}  // namespace NS2

int main() {
  NS1::number = 10;
  NS1::Test();

  using namespace NS2;
  number = 100;
  Test();
  return 0;
}