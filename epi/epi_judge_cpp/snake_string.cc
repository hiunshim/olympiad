#include <string>

#include "test_framework/generic_test.h"
using std::string;

string SnakeString(const string& s) {
  // TODO - you fill in here.
  string result;
  for (int i = 1; i < size(s); i += 4) {
      result += s[i];
  }
  for (int i = 0; i < size(s); i += 2) {
      result += s[i];
  }
  for (int i = 3; i < size(s); i += 4) {
      result += s[i];
  }
  return result;
}

int main(int argc, char* argv[]) {
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"s"};
  return GenericTestMain(args, "snake_string.cc", "snake_string.tsv",
                         &SnakeString, DefaultComparator{}, param_names);
}
