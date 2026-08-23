def needleman_wunsch(seq1, seq2, match=1, mismatch=-1, gap=-2):
    """
    Needleman-Wunsch 全局序列比对（动态规划）
    参数:
        seq1, seq2: str, 待比对序列
        match: int, 匹配得分（默认 +1）
        mismatch: int, 错配罚分（默认 -1）
        gap: int, 空位罚分（默认 -2）
    返回:
        (score, aligned_seq1, aligned_seq2)
    算法要点:
        1. 构建得分矩阵 F，维度 (len(seq1)+1) x (len(seq2)+1)
        2. 初始化第一行和第一列为 gap 的累加
        3. 递推公式:
            F(i,j) = max(
                F(i-1,j-1) + score(seq1[i-1], seq2[j-1]),
                F(i-1,j) + gap,
                F(i,j-1) + gap
            )
        4. 从右下角回溯，记录比对路径，拼接对齐后的序列
    提示:
        回溯时记录每一步的方向，便于构建字符串。
    """
    seq1 = seq1.upper()
    seq2 = seq2.upper()

    def score(mat, num1, num2):
        if seq2[num1 - 1] == seq1[num2 - 1]:
            diag = mat[num1 - 1][num2 - 1] + match
        else:
            diag = mat[num1 - 1][num2 - 1] + mismatch
        left = mat[num1 - 1][num2] +gap
        up = mat[num1][num2 - 1] + gap
        return max(diag, up, left)

    def score_recall(mat, n1, n2):
        if seq1[n1 - 1] == seq2[n2 - 1]:
            return 0
        else:
            if mat[n2][n1] == mat[n2 - 1][n1 -1] + mismatch:
                return 0
            elif mat[n2][n1] == mat[n2 - 1][n1] + gap:
                return 1
            else:
                return -1
    matrix = [[0 for i in range(len(seq1) + 1)] for j in range(len(seq2) + 1)]
    for column in range(len(seq2) + 1):
        matrix[column][0] = gap * column
    for row in range(len(seq1) + 1):
        matrix[0][row] = gap * row
    for row in range(1, len(seq2) + 1):
        for column in range(1, len(seq1) + 1):
            matrix[row][column] = score(matrix, row, column)

    #开始回溯
    # 由于字符串不可变，所以将其放进列表
    seq1_list = []
    seq2_list = []
    recall_column = len(seq1)
    recall_row = len(seq2)
    while recall_column > 0 or recall_row > 0:
        if recall_row == 0:
            # 只能向左（seq1 插入gap）
            seq1_list.append(seq1[recall_column - 1])
            seq2_list.append("-")
            recall_column -= 1
        elif recall_column == 0:
            # 只能向上（seq2 插入gap）
            seq1_list.append("-")
            seq2_list.append(seq2[recall_row - 1])
            recall_row -= 1
        else:
            direction = score_recall(matrix, recall_column, recall_row)
            if direction == 0:
                seq1_list.append(seq1[recall_column - 1])
                seq2_list.append(seq2[recall_row - 1])
                recall_column -= 1
                recall_row -= 1
            elif direction == 1:
                seq1_list.append("-")
                seq2_list.append(seq2[recall_row - 1])
                recall_row -= 1
            else:  # direction == -1
                seq1_list.append(seq1[recall_column - 1])
                seq2_list.append("-")
                recall_column -= 1

    score = matrix[-1][-1]
    return score,''.join(reversed(seq1_list)), ''.join(reversed(seq2_list))

print(needleman_wunsch('GT', 'GAT'))



