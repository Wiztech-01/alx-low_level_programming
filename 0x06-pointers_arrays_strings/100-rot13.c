#include "main.h"

/**
 * rot13 - encodes a string using rot13
 * @s; pointer to string params
 * Return: encoded string
 */

char *rot13(char *s)
{
	int i;
	
	char rot13[] = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
        char datarot[] = "nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM";
        char *ptr = s;
       
	while (*s)
	{
	         for (i = 0; i < 52; i++)
		 {
		        if (*s == rot13[i])
			{
		                *s =  datarot[i];
				break;
			}
		 }
		 s++
	}
        return (ptr);
}	
