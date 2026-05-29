#include <stdint.h>

#include "include_func_helper.h"

int include_func_prog(uint32_t value, int enabled) {
  if (!enabled) {
    return 0;
  }

  uint32_t next = bump_by_three(value);
  return (int)next;
}
