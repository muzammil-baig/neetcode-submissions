from collections import defaultdict, OrderedDict

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.min_freq = 0
        
        # 1. Maps key -> (value, frequency)
        self.cache = {}
        
        # 2. Maps frequency -> OrderedDict(key -> True)
        # The OrderedDict maintains the LRU tie-breaker sequence automatically!
        self.freq_map = defaultdict(OrderedDict)

    def _update_frequency(self, key: int, value: int) -> None:
        _, freq = self.cache[key]
        
        # Remove key from its current frequency tier
        del self.freq_map[freq][key]
        
        # If the minimum frequency bucket is empty, increment min_freq
        if freq == self.min_freq and not self.freq_map[freq]:
            self.min_freq += 1
            
        # Update cache data structure and append to the next frequency bucket
        self.cache[key] = (value, freq + 1)
        self.freq_map[freq + 1][key] = True

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        value, _ = self.cache[key]
        self._update_frequency(key, value)
        return value

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        # Scenario A: Key exists, update value and change frequency
        if key in self.cache:
            self._update_frequency(key, value)
            return

        # Scenario B: Cache is full, evict the LFU item
        if len(self.cache) >= self.capacity:
            # popitem(last=False) pops the oldest item in FIFO/LRU order
            evicted_key, _ = self.freq_map[self.min_freq].popitem(last=False)
            del self.cache[evicted_key]

        # Scenario C: Insert a completely new key
        self.cache[key] = (value, 1)
        self.freq_map[1][key] = True
        self.min_freq = 1  # Reset min frequency tier back to 1