#include <stdint.h>

typedef uint32_t u32;

#define MAP_SIZE 4

struct int_map {
  int present[MAP_SIZE];
  u32 values[MAP_SIZE];
};

int map_prog(struct int_map *map, u32 key) {
  if (key >= MAP_SIZE || !map->present[key]) {
    return key >= MAP_SIZE ? -1 : 0;
  }

  map->values[key] += 7;
  return map->values[key];
}
