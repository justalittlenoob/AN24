#include <stdlib.h>
EXPORT void __cdecl get_crc(char *);
static unsigned short crctab[256];/* The CRC lookup table */
#define GENERATE_POLYNOMIAL 0x1021/* The CCITT polynomial */
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
static unsigned short crchware ( unsigned short data,
unsigned short poly,
unsigned short accum )
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

EXPORT void __cdecl int get_crc (char *message )
{
unsigned short crc;
int i;
//char message[18];
//scanf("%s",&message);
//char *message = "\x10\x02H\x10\x03";
mk_crctbl(); /* This must be called only once in an application */
crc = 0; /* Initialize the CRC value with zero */
for ( i=0; i<strlen(message); ++i )
{
crcupdate ( message[i], &crc );
}
printf ( "Message=<%s>, CRC=%04x\n", message, crc );
}

