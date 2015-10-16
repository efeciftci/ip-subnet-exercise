*/
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 */

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(int argc, char** argv)
{
	int count, correctAnswers = 0;
	int ip[4], subnet[4];
	int tmpsubnet[13][2] = { { 0, 0 }, { 128, 0 }, { 192, 0 }, { 224, 0 }, { 240, 0 }, { 248, 0 }, { 252, 0 }, { 254, 0 }, { 255, 0 }, { 255, 128 }, { 255, 192 }, { 255, 224 }, { 255, 240 } };
	int tmpsubnet2[13][2] = { { 255, 255 }, { 127, 255 }, { 63, 255 }, { 31, 255 }, { 15, 255 }, { 7, 255 }, { 3, 255 }, { 1, 255 }, { 0, 255 }, { 0, 127 }, { 0, 63 }, { 0, 31 }, { 0, 15 } };
	int usrNetwork[4], usrBcast[4], ansNetwork[4], ansBcast[4];
	int flag, tmp;
	srand(time(0));

	/* we want subnet masks to be in range of 255.255.0.0 and 255.255.255.240 for simplicity */
	subnet[0] = 255;
	subnet[1] = 255;

	for (count = 0; count < 4; count++)
	{
		flag = 0;
		/* generate a new ip address and its subnet mask */
		ip[0] = rand() % 255;
		ip[1] = rand() % 255;
		ip[2] = rand() % 255;
		ip[3] = rand() % 255;
		tmp = rand() % 13;
		subnet[2] = tmpsubnet[tmp][0];
		subnet[3] = tmpsubnet[tmp][1];

		/* show ip and subnet to the user */
		printf("IP address : %d.%d.%d.%d\n", ip[0], ip[1], ip[2], ip[3]);
		printf("Subnet mask: %d.%d.%d.%d\n", subnet[0], subnet[1], subnet[2], subnet[3]);

		/* ask network and bcast addresses to the user */
		printf("Network address: ");
		scanf("%d.%d.%d.%d", &usrNetwork[0], &usrNetwork[1], &usrNetwork[2], &usrNetwork[3]);
		printf("Broadcast address: ");
		scanf("%d.%d.%d.%d", &usrBcast[0], &usrBcast[1], &usrBcast[2], &usrBcast[3]);

		/* is network correct? */
		ansNetwork[0] = ip[0] & subnet[0];
		ansNetwork[1] = ip[1] & subnet[1];
		ansNetwork[2] = ip[2] & subnet[2];
		ansNetwork[3] = ip[3] & subnet[3];
		if ((usrNetwork[0] == ansNetwork[0]) && (usrNetwork[1] == ansNetwork[1]) && (usrNetwork[2] == ansNetwork[2]) && (usrNetwork[3] == ansNetwork[3]))
		{
			correctAnswers++;
			flag++;
		}
		else
			printf("Network address is incorrect! The answer is %d.%d.%d.%d\n", ansNetwork[0], ansNetwork[1], ansNetwork[2], ansNetwork[3]);

		/* is bcast correct? */
		ansBcast[0] = ip[0];
		ansBcast[1] = ip[1];
		ansBcast[2] = ip[2] | tmpsubnet2[tmp][0];
		ansBcast[3] = ip[3] | tmpsubnet2[tmp][1];
		if ((usrBcast[0] == ansBcast[0]) && (usrBcast[1] == ansBcast[1]) && (usrBcast[2] == ansBcast[2]) && (usrBcast[3] == ansBcast[3]))
		{
			correctAnswers++;
			flag++;
		}
		else
			printf("Broadcast address is incorrect! The answer is %d.%d.%d.%d\n", ip[0], ip[1], ip[2] | tmpsubnet2[tmp][0], ip[3] | tmpsubnet2[tmp][1]);

		if (flag == 2)
			printf("Good job!\n");
		printf("\n");
	}

	printf("Your score: %.1f\n", correctAnswers / 8.0 * 100);
	return 0;
}
