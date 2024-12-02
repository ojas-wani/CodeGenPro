package orderedstream;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * A class to maintain an ordered stream.
 */
public class OrderedStream {
    private Map<Integer, String> map;
    private List<String> chunk;

    /**
     * Initializes an object of the OrderedStream class.
     * 
     * @param n the maximum ID key in the stream.
     */
    public OrderedStream(int n) {
        map = new HashMap<>();
        chunk = new ArrayList<>();
        for (int i = 1; i <= n; i++) {
            map.put(i, null);
        }
    }

    /**
     * Inserts a new value into the stream and returns the largest possible chunk of 
     * previously inserted values that appear next in the order.
     * 
     * @param idKey the key of the value to be inserted.
     * @param value the value to be inserted.
     * @return the largest possible chunk of previously inserted values that appear next 
     * in the order.
     */
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