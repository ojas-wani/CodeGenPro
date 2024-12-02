class Solution {
    public boolean isPathCrossing(String path) {
        int x = 0, y = 0;
        boolean[][] visited = new boolean[2001][2001];
        visited[1001][1001] = true;
        for (char c : path.toCharArray()) {
            switch (c) {
                case 'N':
                    y++;
                    break;
                case 'S':
                    y--;
                    break;
                case 'E':
                    x++;
                    break;
                case 'W':
                    x--;
                    break;
            }
            if (x < 0 || x >= 2000 || y < 0 || y >= 2000 || visited[x + 1000][y + 1000]) {
                return true;
            }
            visited[x + 1000][y + 1000] = true;
        }
        return false;
    }
}