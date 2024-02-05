#include <iostream>
#include <map>
#include <random>
#include <cctype>
#include <algorithm>
#include <limits>
using namespace std;



bool isWord(const string& userWord, const string& trueMansWord){
    string preview;

    for (char x : userWord) {
        preview += x;
        preview += ' ';
    }
    cout << preview << endl;

    for(size_t i=0; i< userWord.length(); ++i){
        if(userWord[i] == trueMansWord[i]){
            cout<< "\033[92m" << "▉" << "\033[0m" << " ";
        }
        else if(trueMansWord.find(userWord[i]) != string::npos && userWord[i] != trueMansWord[i]){
            cout<< "\033[93m" << "▉" << "\033[0m" << " ";
        }
        else{
            cout<< "\033[90m" << "▉" << "\033[0m" << " ";
        }
    }
    cout<<"\n";
    if(userWord == trueMansWord){
        return 1;
    }
    else{
        return 0;
    }
}

int main(){
    string words[] = {"which", "there", "their", "about", "would", "these", "other", "words", "could", "write", "first", "water", "after", "where", "right", "think"};
    srand(static_cast<unsigned int>(time(0)));
    
    int size = sizeof(words)/sizeof(words[0]);
    
    string trueMansWord = words[rand() % size];

    cout<<"Take a chance, Child\n"<<"Guess what word I withold";

    map<int, string> message;
    message[0] = "Ok";
    message[1] = "Good";
    message[2] = "Nice";
    message[3] = "Very good";
    message[4] = "Marvellous!";
    message[5] = "Amazing!!";

    int i = 6;

    while(i>0){
        string userWord;
        cout<<"\nEnter Word: ";
        cin>>userWord;
        transform(userWord.begin(), userWord.end(), userWord.begin(), ::tolower);
        if(userWord.length()==5 && all_of(userWord.begin(), userWord.end(), ::isalpha)){
            i--;
            if(isWord(userWord, trueMansWord)){
                cout<<endl<<message[i]<<endl;
                break;
            }
            else{
                continue;
            }
        }
        else{
            cout<<"Do not test me child!\nEnter a valid word now!"<<endl;
        }
    }
    if(i==0){
        cout<<"End of Game, the correct word is: "<< trueMansWord;
    }
    return 0;
}