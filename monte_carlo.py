from pyspark.context import SparkContext


# data: function to generate input data
# function: fn to apply to the data. Should return true or false
# n: number of iterations
def run_sim(data, function, n):
    sc = SparkContext()

    input_data = sc.parallelize([data() for _ in range(n)])
    transformed_data = input_data.map(lambda x: function(x))
    kvp_data = transformed_data.map(lambda x: (x, 1))
    
    counts = kvp_data.reduceByKey(lambda a, b: a+b)
    counts = counts.collectAsMap()
    
    try:
        num_true = counts[True]
    except:
        num_true = 0
    num_false = counts[False]
    
    return num_true/n


