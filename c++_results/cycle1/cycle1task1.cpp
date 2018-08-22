#include<iostream>
#include<algorithm>
#include<string>

using namespace std;
int main() {
    string s;
    cin >> s;
    string q;
    string result;
    q = s.substr(0,1);
    int mylenght = s.length();
    replace( s.begin(), s.end(), 'i', '*'); // replace all 'x' to 'y'
    result = q + s.substr(1,mylenght);

    cout << result;
    return 0;
}
//http://www.cplusplus.com/forum/beginner/33835/
//http://www.cplusplus.com/reference/string/string/replace/
//https://stackoverflow.com/questions/2896600/how-to-replace-all-occurrences-of-a-character-in-string
