# 在这import random

def simulate_point(prob):
    """模拟1分的胜负，prob为选手A的得分概率"""
    return random.random() < prob

def simulate_game(prob_a):
    """模拟一局比赛，返回最终比分(score_a, score_b)"""
    score_a, score_b = 0, 0
    serve_count = 0  # 记录当前轮发球次数（每轮2次）
    server = 'A'     # 初始发球方为A

    while True:
        # 模拟1分
        if simulate_point(prob_a):
            score_a += 1
        else:
            score_b += 1
        
        # 切换发球方（每轮2次发球）
        serve_count += 1
        if serve_count % 2 == 0:
            server = 'B' if server == 'A' else 'A'
        
        # 判断比赛结束条件
        # 情况1：一方先到11分且分差≥2
        if (score_a >= 11 or score_b >= 11) and abs(score_a - score_b) >= 2:
            return (score_a, score_b)
        # 情况2：比分到12:10（单局最高）
        if (score_a == 12 and score_b == 10) or (score_a == 10 and score_b == 12):
            return (score_a, score_b)

# 测试：模拟1局比赛（选手A得分概率为0.6）
if __name__ == "__main__":
    final_score = simulate_game(0.6)
    print(f"比赛结束，比分：{final_score[0]}:{final_score[1]}")个文件里编写代码
