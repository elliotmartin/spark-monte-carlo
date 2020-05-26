from pyspark.context import SparkContext


# data: function to generate input data
# function: fn to apply to the data. Should return true or false
# n: number of iterations
def run_sim(data, function, n):
    sc = SparkContext()

    input_data = sc.parallelize([data()] * n)
    transformed_data = input_data.map(lambda x: function(x))
    kvp_data = transformed_data.map(lambda x: (x, 1))
    
    counts = kvp_data.reduceByKey(lambda a, b: a+b)
    counts = counts.collectAsMap()
    
    num_true = counts[True]
    num_false = counts[False]
    
    return num_true/n


