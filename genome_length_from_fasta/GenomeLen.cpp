#include <stdio.h>
#include "iostream"
#include "fstream"
#include <string>
using namespace std;

int main(int argc, char *argv[])
{
	ifstream infile (argv[1]);
	string line;
	long long c = 0;
	if (infile.is_open()) 
	{
		getline (infile, line);
		while(  getline (infile, line))
		{

            //cout<<line<<endl;
            c+= line.length();
		}
	}
	cout << c << endl;
}