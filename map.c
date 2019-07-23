// Wednesday 24 Jul, 2019 05:34:01 AM

#include <stdio.h>
#include <string.h>

int main() {
    // Details in python file
    const char *magic =
        "y}@z?{|{HtJpy|TgUhQjPlKqIphynJsHw}}JuGwG}}tLmOhXe[`]b[tzn\\tzl]xvn["
        "xwj_}}zvl[}tlOm]}pn_zqmd{}xsmer{|xmfr}zxmfmxm||phwm||z}|{{gwl}WxCxF|y}"
        "=";

    const int len = strlen(magic);

    int counter = 0;
    for (int i = 0; i < len; ++i) {
        int value = 126 - magic[i];
        for (int j = 0; j < value; ++j, ++counter) {
            if (counter == 64) {
                counter = 0;
                puts("");
            }
            putchar(i & 0x1 ? '*' : ' ');
        }
    }
    puts("");
    return 0;
}
