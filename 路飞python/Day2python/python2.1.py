def activity_selection(activities):
    """
    使用贪心算法解决活动选择问题。

    参数:
        activities (list of tuples): 活动列表，其中每个元素都是一个二元组(start, end)，
                                     表示活动的开始时间和结束时间。

    返回:
        selected_activities (list of tuples): 可以参与的最大活动集合。
    """
    # 根据活动的结束时间对活动进行排序
    sorted_activities = sorted(activities, key=lambda x: x[1])

    # 初始化结果集，添加第一个活动
    selected_activities = [sorted_activities[0]]

    # 记录上一个被选中的活动的结束时间
    last_end_time = sorted_activities[0][1]

    # 遍历剩余活动
    for start, end in sorted_activities[1:]:
        # 如果当前活动的开始时间大于等于最后一个选定活动的结束时间，则可以参加该活动
        if start >= last_end_time:
            selected_activities.append((start, end))
            last_end_time = end  # 更新最后结束时间

    return selected_activities


# 示例数据
activities = [(1, 2), (3, 4), (0, 6), (5, 7), (8, 9), (5, 9)]
selected = activity_selection(activities)
print("Selected activities:", selected)
