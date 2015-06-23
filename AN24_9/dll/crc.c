#include <stdio.h>
#include <string.h>
#define GENERATE_POLYNOMIAL 0x1021/* The CCITT polynomial */

#ifdef BUILD_DLL
#define EXPORT __declspec(dllexport)
#else
#define EXPORT __declspec(dllimport)
#endif

EXPORT unsigned short __cdecl generate_CRC(char *);

static unsigned short crctab[256];/* The CRC lookup table */



/*------------------------------------------------------------------------
* crcupdate ( unsigned short data, --- new data to be added to CRC
* unsigned short *accum --- storage of old/new CRC
* )
*/
void crcupdate ( unsigned short data, unsigned short *accum )
{
	*accum = (*accum << 8) ^ crctab[(*accum >> 8) ^ data];
}



/*------------------------------------------------------------------------
* crchware ( unsigned short data, --- data to be polynomial divided
* unsigned short poly, --- polynomial divisor
* unsigned short accum --- old (preset) CRC value
*/
static unsigned short crchware ( unsigned short data,unsigned short poly,unsigned short accum)
{
	int i;
	data <<= 8; /* Data to high byte */
	for (i=8; i>0; i--)
	{
		if ((data ^ accum) & 0x8000) /* if msb of (data XOR accum) is TRUE */
			accum = (accum << 1) ^ poly; /* shift and subtract poly */
		else accum <<= 1; /* otherwise, transparent shift */
			data <<= 1; /* move up next bit for XOR */
	}
	return accum;
}


/*------------------------------------------------------------------------
* mk_crctbl () --- Creates / fills the crctab table
*/
void mk_crctbl ( void )
{
	int i;
	for (i=0; i<256; ++i)
	{
		/* Fill the table with CRCs of values .... */
		crctab[i] = crchware ( i, GENERATE_POLYNOMIAL, 0 );
	}
}


EXPORT unsigned short generate_CRC(char *message)
{
	unsigned short crc;
	int i;
	
	mk_crctbl(); /* This must be called only once in an application */
	crc = 0; /* Initialize the CRC value with zero */
	for ( i=0; i<strlen(message); ++i )
	{
		crcupdate ( message[i], &crc );		//-----------------output-------------------
	}
	return crc;
}
