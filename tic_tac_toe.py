class Solution(object):
    def tictactoe(self, moves):
        """
        :type moves: List[List[int]]
        :rtype: str
        """
        def check(self,final):
            for i in range(len(final)):
                if final[i][0] == final[i][1] == final[i][2] == 'X':
                    return 'A'
                if final[i][0] == final[i][1] == final[i][2] == 'O':
                    return 'B'
                if final[0][i] == final[1][i] == final[2][i] == 'X':
                    return 'A'
                if final[0][i] == final[1][i] == final[2][i] == 'O':
                    return 'B'
            if final[0][0] == final[1][1] == final[2][2] == 'X':
                return 'A'
            if final[0][0] == final[1][1] == final[2][2] == 'O':
                return 'B'
            if final[2][0] == final[1][1] == final[0][2] == 'X':
                return 'A'
            if final[2][0] == final[1][1] == final[0][2] == 'O':
                return 'B'
        
        final = [[0,0,0],[0,0,0],[0,0,0]]
        for i in range(len(moves)):
            a = moves[i][0]
            b = moves[i][1]
            if i%2==0:
                final[a][b] = 'X'
            elif i%2==1:
                final[a][b] = 'O'

        #print(check(self,final))
        a = check(self,final)
        if a==None and len(moves)==9:
            return "Draw"
        elif a==None and len(moves)<9:
            return "Pending"
        return a
moves =  [[0,0],[2,0],[1,1],[2,1],[2,2]]
s = Solution()
print(s.tictactoe(moves))
