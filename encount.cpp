#include <iostream>
#include <string>
using namespace std;

int main() {
    string s;
    int count = 0;
    while(true) {
        cin >>s;
        if(cin.eof())
            break;
        if(s[0] != '(') {
            count++;
        }
    }
    cout << count << "words" << endl;
}