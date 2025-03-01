import pandas as pd
from scipy.sparse import csr_matrix
from sklearn.metrics.pairwise import cosine_similarity

# 示例数据集路径
ratings_path = 'ratings.csv'
items_path = 'items.csv'

# 加载数据
data = pd.read_csv(ratings_path, sep=',')
items = pd.read_csv(items_path, sep=',')

# 删除重复行（如果有）
data = data.drop_duplicates()

# 创建用户-物品矩阵
max_user = max(data['user_id']) if not data.empty else 0
max_item = max(data['item_id']) if not data.empty else 0

matrix = csr_matrix((data['rating'], (data['user_id'], data['item_id'])),
                    shape=(max_user + 1, max_item + 1))

# 计算用户之间的余弦相似度
user_similarity = cosine_similarity(matrix.T)


def recommend_products(user_id, matrix, user_similarity, num_recommendations=5):
    # 获取该用户的评分记录
    user_ratings = matrix.getrow(user_id).toarray()

    # 计算相似用户列表（按相似度降序排列）
    similar_users = user_similarity[user_id].argsort()[::-1]

    recommendations = []
    for user in similar_users:
        if user != user_id:  # 忽略自己
            similarity = user_similarity[user_id, user]
            user_ratings_list = matrix.getrow(user).toarray()

            # 计算未评分的商品的加权评分
            for item in range(len(user_ratings_list)):
                if user_ratings[item] == 0 and user_ratings_list[item] > 0:
                    recommendations[item] += similarity * user_ratings_list[item]

    # 排序推荐结果，按加权评分从高到低排序
    recommendations = sorted(recommendations, reverse=True)

    return recommendations[:num_recommendations]


# 示例：为用户推荐商品
user_id = 1  # 替换为你想要推荐的用户的ID
recommendations = recommend_products(user_id, matrix, user_similarity)

# 展示推荐结果
print(f"推荐给用户 {user_id} 的商品：")
for idx, item in enumerate(recommendations):
    print(f"{idx + 1}. 商品 {item}（评分：{matrix[user_id, item] if matrix[user_id, item] > 0 else '未知'}）")

# 可选：可视化相似度矩阵
import seaborn as sns;
import matplotlib.pyplot as plt

plt.figure(figsize=(12, 8))
sns.heatmap(user_similarity, annot=False, cmap='viridis')
plt.title('用户之间的余弦相似度矩阵')
plt.show()


