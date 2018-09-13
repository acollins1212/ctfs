#include <fcntl.h>
#include <stdio.h>
#include <unistd.h>

char* file_in = "cipher.in";
char* file_out = "cipher.out";

int main(){
	int fd_out = open(file_out, O_RDWR);

	unsigned char buf[1]; 
	int fd_in = open(file_in, O_RDONLY);
	while(read(fd_in, buf, 1) > 0){
		printf("%c", buf[0] | 0x41);
	}
	close(fd_in);
}

