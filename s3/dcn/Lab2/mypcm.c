// general purpose standard C lib
#include <stdio.h>
#include <stdlib.h> // includes malloc(),free()
#include <math.h>
//Add any necessary headers here

// user-defined header files
#include "mypcm.h" // do not modify this file

// put your function prototypes for additional helper functions below:
int NUMBER_OF_SAMPLES = 0;

// implementation
float analog_signal_generator(asignal signal, int t)
{
  if (t > signal.duration) return 0;
  return (signal.A) * sin(signal.omega * t + signal.sigma);
}
void sampler(float *samples, int interval, asignal signal)
{
  NUMBER_OF_SAMPLES = (signal.duration / interval) + 1;
  for (int i = 0; i < NUMBER_OF_SAMPLES; i++) {
    samples[i] = analog_signal_generator(signal, interval * i);
  }
}
void quantizer1(float *samples, int *pcmpulses, int levels)
{
  quantizer(samples, pcmpulses, levels, 1);
}
void quantizer(float *samples, int *pcmpulses, int levels, float A)
{
  for (int i = 0; i < NUMBER_OF_SAMPLES; i++) {
    pcmpulses[i] = floor((samples[i] + A) * levels / (2 * A));
  }
}
void encoder(int *pcmpulses, int *dsignal, int encoderbits)
{
  for (int i = 0; i < NUMBER_OF_SAMPLES; i++) {
    int pcmValue = pcmpulses[i];

    for (int bit_i = encoderbits - 1; bit_i >= 0; bit_i--) {
      dsignal[(i + 1)*encoderbits - bit_i - 1] = (pcmValue >> bit_i) & 1;
    }
  }
}
