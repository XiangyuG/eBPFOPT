#include <stdint.h>

typedef uint32_t u32;

#define MAP_SIZE 4

struct int_map {
  int present[MAP_SIZE];
  u32 values[MAP_SIZE];
};

int map_prog(struct int_map *map, u32 key) {
  if (key >= MAP_SIZE) {
    return -1;
  }

  if (!map->present[key]) {
    return 0;
  }

  u32 old_value = map->values[key];
  u32 new_value = old_value + 7;
  map->values[key] = new_value;

  return map->values[key];
}
