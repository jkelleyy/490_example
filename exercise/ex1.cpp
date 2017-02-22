/* Example Code for problem 1 in c++
 */

#include <iostream>

using namespace std;

int main(){
    int val = 1;
    while(cin){
        int x;
        cin >> x;
        if(cin.eof()){
            break;
        }
        val *= x;
    }
    cout << val;
}
