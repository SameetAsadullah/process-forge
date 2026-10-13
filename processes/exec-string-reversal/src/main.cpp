#include <iostream>
#include <unistd.h>
#include <sys/wait.h>
#include <stdlib.h>
using namespace std;

int main () {
	pid_t pID;
	int status;

	pID = fork ();

	if (pID > 0) {
		cout << "Parent Process Starts:" << endl;
		cout << "	My PID= " << getpid() << ", My Child's PID= " << pID << endl << endl;
		wait (&status);
		cout << endl << "Parent Process Finished" << endl;
		cout << status << endl;
	}

	else if (pID == 0) {
		cout << "Child Process Starts:" << endl;
		cout << "	My PID= " << getpid() << ", My PPID= " << getppid() << endl;
		execlp ("./reverse-string" , "reverse-string" , "Sameet" , NULL); //or dont pass first argument and reverse arr[0]
		cout << "Exec Failed" << endl;	
	}

	else {
		cout << "Fork Failed" << endl;
	}
	

	return 0;
}
