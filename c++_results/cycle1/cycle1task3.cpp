#include <iostream>
#include <string>
#include <algorithm>

int isNotAlphaNum(char c)
{
        return !std::isalnum(c);
}

int main(int argc, char* argv[])
{
    std::string s1;
    std::cin >> s1;

        std::replace_if(s1.begin(), s1.end(), isNotAlphaNum, '?');
        std::replace_if(s1.begin(), s1.end(), isalpha, '-');
        std::replace_if(s1.begin(), s1.end(), isdigit, '*');
        std::cout << s1;
}
