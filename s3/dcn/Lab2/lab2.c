// general purpose standard C lib
#include <stdio.h>
#include <stdlib.h> // stdlib includes malloc() and free()
#include <string.h>

// user-defined header files
#include "mypcm.h"

#define INPUT_LINE_BUFFER_SIZE 1000
#define INPUT_NUMBER_DELIMITER (" ")

// function prototypes
void run(asignal *inputsignal);

int main()
{
  asignal *inputsignal = (asignal *)malloc(sizeof(asignal));
  run(inputsignal);

  // call any other function here

  free(inputsignal);
  return 0;
}

void run(asignal *inputsignal)
{
  char buffer[INPUT_LINE_BUFFER_SIZE];
  fgets(buffer, INPUT_LINE_BUFFER_SIZE, stdin);

  int interval, encoderbits;
  int i = 0;
  char *token = strtok(buffer, INPUT_NUMBER_DELIMITER);

  while (i < 6)
  {
    switch (i)
    {
    case 0:
      inputsignal->A = (float)strtof(token, NULL);
      break;
    case 1:
      inputsignal->omega = (float)strtof(token, NULL);
      break;
    case 2:
      inputsignal->sigma = (float)strtof(token, NULL);
      break;
    case 3:
      inputsignal->duration = (int)strtol(token, NULL, 10);
      break;
    case 4:
      interval = (int)strtol(token, NULL, 10);
      break;
    case 5:
      encoderbits = (int)strtol(token, NULL, 10);
      break;
    }

    token = strtok(NULL, INPUT_NUMBER_DELIMITER);
    i++;
  }
  int numberOfSamples = (inputsignal->duration / interval) + 1;
  int numberOfLevels = 1 << encoderbits;
  float *samples = (float *)malloc(sizeof(float) * numberOfSamples);
  int *pcmpulses = (int *)malloc(sizeof(int) * numberOfSamples);
  int dsignalLength = encoderbits * numberOfSamples;
  int *dsignal = (int *)malloc(sizeof(int) * dsignalLength);

  sampler(samples, interval, *inputsignal);

  quantizer(samples, pcmpulses, numberOfLevels, inputsignal->A);
  free(samples);

  encoder(pcmpulses, dsignal, encoderbits);
  free(pcmpulses);

  for (int i = 0; i < dsignalLength; i++)
  {
    printf("%d", dsignal[i]);
  }
  printf("\n");
  free(dsignal);
}
