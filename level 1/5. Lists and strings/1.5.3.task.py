# первый вариант
usd = [63.1385, 63.9091, 63.4342, 63.1742, 62.7977, 63.472, 63.7708, 63.949, 63.047, 63.6016, 63.4536, 63.3085, 63.7698, 63.6873, 63.7413, 64.3008, 64.9213, 65.5177, 65.6097, 66.9909, 66.3274, 66.4437, 66.0784, 66.1854, 67.5175, 72.0208, 71.472, 74.0274, 73.1882, 74.1262, 73.8896, 77.2131, 80.157, 78.0443, 80.8815, 78.8493, 77.7928, 78.7223, 77.7325, 76.4074, 75.455, 75.7499, 74.605, 73.7515, 73.5245, 73.315, 73.7145, 74.7119, 73.9441, 74.6657, 76.2562, 77.0416, 75.129, 74.7163, 74.496, 74.5706, 73.6894, 72.7263, 73.9719, 74.1169, 73.8725, 73.4326, 73.5819, 73.9298, 73.2056, 72.9798, 72.3918, 72.3381, 70.924, 71.8804, 71.5962, 71.1408, 71.0635, 71.1012, 70.752, 69.7114, 68.9831, 68.3413, 69.0151, 68.6319, 68.3123, 68.6745, 68.6183, 69.1219, 70.395, 69.7524, 69.4822, 69.618, 69.5725, 69.4835, 68.8376, 68.8376, 69.466, 69.1284, 69.9513, 70.4413, 70.4413, 70.5198, 70.4999, 71.3409]

usd_new = [i for i in usd if i > 70]        # интересная запись, цикл с условием помещается сразу в список
print(usd_new)

###############################

# второй вариант
usd = [63.1385, 63.9091, 63.4342, 63.1742, 62.7977, 63.472, 63.7708, 63.949, 63.047, 63.6016, 63.4536, 63.3085, 63.7698, 63.6873, 63.7413, 64.3008, 64.9213, 65.5177, 65.6097, 66.9909, 66.3274, 66.4437, 66.0784, 66.1854, 67.5175, 72.0208, 71.472, 74.0274, 73.1882, 74.1262, 73.8896, 77.2131, 80.157, 78.0443, 80.8815, 78.8493, 77.7928, 78.7223, 77.7325, 76.4074, 75.455, 75.7499, 74.605, 73.7515, 73.5245, 73.315, 73.7145, 74.7119, 73.9441, 74.6657, 76.2562, 77.0416, 75.129, 74.7163, 74.496, 74.5706, 73.6894, 72.7263, 73.9719, 74.1169, 73.8725, 73.4326, 73.5819, 73.9298, 73.2056, 72.9798, 72.3918, 72.3381, 70.924, 71.8804, 71.5962, 71.1408, 71.0635, 71.1012, 70.752, 69.7114, 68.9831, 68.3413, 69.0151, 68.6319, 68.3123, 68.6745, 68.6183, 69.1219, 70.395, 69.7524, 69.4822, 69.618, 69.5725, 69.4835, 68.8376, 68.8376, 69.466, 69.1284, 69.9513, 70.4413, 70.4413, 70.5198, 70.4999, 71.3409]

for i in usd:
    if i > 70:
        print(i)