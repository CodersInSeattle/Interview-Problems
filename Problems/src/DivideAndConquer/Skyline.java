import java.util.*;

/**
 Leetcode: 218. The Skyline Problem

 */
public class Skyline {
    public List<int[]> getSkyline(int[][] buildings) {
        final Map<Integer, List<int[]>> map = flatten(buildings);
        final Queue<int[]> heap = new PriorityQueue<>((a, b) -> ((Integer)b[2]).compareTo(a[2]));
        final List<int[]> ans = new ArrayList<>();
        
        for (Integer pos : new TreeSet<Integer>(map.keySet())) {
            List<int[]> list = map.get(pos);
            heap.addAll(list);

            while (!heap.isEmpty() && heap.peek()[1] <= pos) {
                heap.poll(); // remove finished building
            }
            int h = heap.isEmpty() ? 0 : heap.peek()[2];
            if (ans.size() > 0) {
                int lastArr[] = ans.get(ans.size() - 1);
                if (lastArr[1] == h) {
                    continue;
                } 
            }
            ans.add(new int[]{pos, h});
        }
        return ans;
    }
    private Map<Integer, List<int[]>> flatten(int buildings[][]) {
        Map<Integer, List<int[]>> map = new HashMap<>();
        
        for (int[] building : buildings) {
            List<int[]> list = map.getOrDefault(building[0], new ArrayList<int[]>());
            list.add(building);
            map.put(building[0], list);
            map.put(building[1], map.getOrDefault(building[1], new ArrayList<int[]>()));
        }
        return map;
    }
}
