#include <stdint.h>

#include "include_func_helper.h"

int include_func_prog(uint32_t value, int enabled) {
  uint32_t next = value;

  if (enabled) {
    next = bump_by_three(next);
  } else {
    return 0;
  }

  return (int)next;
}
