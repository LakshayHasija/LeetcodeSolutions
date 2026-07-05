class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        n = len(board)
        MOD = 10**9 + 7
        dp_score = [[0] * (n + 1) for _ in range(n + 1)]
        dp_paths = [[0] * (n + 1) for _ in range(n + 1)]
        dp_paths[n - 1][n - 1] = 1
        for r in range(n - 1, -1, -1):
            row = board[r]
            dp_score_r = dp_score[r]
            dp_paths_r = dp_paths[r]
            dp_score_next = dp_score[r + 1]
            dp_paths_next = dp_paths[r + 1]

            for c in range(n - 1, -1, -1):
                char = row[c]
                if char == "X" or (r == n - 1 and c == n - 1):
                    continue
                s1, p1 = dp_score_next[c], dp_paths_next[c]
                s2, p2 = dp_score_r[c + 1], dp_paths_r[c + 1]
                s3, p3 = dp_score_next[c + 1], dp_paths_next[c + 1]
                max_s = -1
                paths = 0

                if p1 > 0 and s1 > max_s:
                    max_s, paths = s1, p1
                elif p1 > 0 and s1 == max_s:
                    paths += p1

                if p2 > 0 and s2 > max_s:
                    max_s, paths = s2, p2
                elif p2 > 0 and s2 == max_s:
                    paths += p2

                if p3 > 0 and s3 > max_s:
                    max_s, paths = s3, p3
                elif p3 > 0 and s3 == max_s:
                    paths += p3
                if max_s != -1:
                    dp_score_r[c] = max_s + (int(char) if char != "E" else 0)
                    dp_paths_r[c] = paths % MOD

        return [dp_score[0][0], dp_paths[0][0]]