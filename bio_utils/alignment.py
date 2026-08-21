def needleman_wunsch(seq1, seq2, match=1, mismatch=-1, gap=-1):
    """
    Needleman-Wunsch 全局序列比对（动态规划）
    参数:
        seq1, seq2: str, 待比对序列
        match: int, 匹配得分（默认 +1）
        mismatch: int, 错配罚分（默认 -1）
        gap: int, 空位罚分（默认 -1）
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
    pass