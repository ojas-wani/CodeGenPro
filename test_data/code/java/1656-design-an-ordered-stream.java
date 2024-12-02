import java.util.*;

class OrderedStream {
    private Map<Integer, String> map;
    private List<String> chunk;

    public OrderedStream(int n) {
        map = new HashMap<>();
        chunk = new ArrayList<>();
        for (int i = 1; i <= n; i++) {
            map.put(i, null);
        }
    }

    public List<String> insert(int idKey, String value) {
        if (idKey > map.size()) {
            return chunk;
        }
        if (map.get(idKey) == null) {
            map.put(idKey, value);
            while (chunk.size() < idKey && map.containsKey(idKey)) {
                chunk.add(map.remove(idKey));
            }
        }
        return chunk;
    }
}