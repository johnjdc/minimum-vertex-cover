from MVC import min_vertex_cover, read_graph

input_data = read_graph('simple_graph.txt')
output_data = min_vertex_cover(input_data[0], input_data[1])

print output_data

# Output = {2000: [1000, 1001]}, where 2000 is the minimum vertex cover.
