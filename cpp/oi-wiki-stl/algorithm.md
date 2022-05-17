有起止点的（用迭代器）：`sort, reverse, unique`
除了起止点还有其它参数`find, shuffle`（后者需要`std::mt19937 rng(std::random_device{}());`然后把`rng`作为第三个参数）
特殊：`nth_element`：除了起止点还有一个`pivot`地位的东西，即三个迭代器参数