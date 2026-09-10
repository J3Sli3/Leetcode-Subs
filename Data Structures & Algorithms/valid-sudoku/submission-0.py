class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            appearedr = set()
            for val in board[i]:
                if val == '.':
                    continue
                if val in appearedr:
                    return False
                appearedr.add(val)

            appearedc = set()
            for r in range(9):
                val = board[r][i]
                if val == '.':
                    continue
                if val in appearedc:
                    return False
                appearedc.add(val)

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                appeareds = set()
                for r in range(i, i+3):
                    for c in range(j, j+3):
                        val = board[r][c]
                        if val =='.':
                            continue
                        if val in appeareds:
                            return False
                        appeareds.add(val)       
        return True


            
                


        