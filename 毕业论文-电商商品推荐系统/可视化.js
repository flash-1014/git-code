import React, { useState } from 'react';
import { PieChart, Pie, Cell, CellData, LineChart, Line } from 'd3-vega';
import { cluster } from 'd3/dendrogram';

const userRatingData = [
  { userId: 1, rating: 5 },
  { userId: 2, rating: 4 },
  { userId: 3, rating: 4.5 },
  // 添加更多用户数据
];

const productRatingData = [
  { productId: 'A', ratings: [4, 5, 4] },
  { productId: 'B', ratings: [5, 4.5, 5] },
  // 添加更多商品数据
];
