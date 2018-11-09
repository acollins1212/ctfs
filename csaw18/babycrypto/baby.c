#include <fcntl.h>
#include <stdio.h>
#include <unistd.h>

char* file_in = "unicode.txt";

int main(){
//	int fd_out = open(file_out, O_RDWR);

	unsigned char buf[1]; 
	int fd_in = open(file_in, O_RDONLY);
	while(read(fd_in, buf, 1) > 0){
		printf("%c", buf[0] ^ 0x59454554); //yeet in hex
	}
	close(fd_in);
}

