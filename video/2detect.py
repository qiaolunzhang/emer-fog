from imageai.Prediction import ImagePrediction
import os
import time

execution_path = os.getcwd()

prediction = ImagePrediction()
prediction.setModelTypeAsResNet()
prediction.setModelPath(os.path.join(execution_path, "resnet50_weights_tf_dim_ordering_tf_kernels.h5"))
prediction.loadModel()
time_used = 0

for i in range(5):
    time_start = time.time()
    predictions, probabilities = prediction.predictImage(os.path.join(execution_path+"/image/", "frame" +str(i*500) +".jpg"), result_count=5 )
    for eachPrediction, eachProbability in zip(predictions, probabilities):
        print(eachPrediction , " : " , eachProbability)
    if (i):
        time_used = time_used + time.time() - time_start
    print(time_used)

time_start = time.time()
predictions, probabilities = prediction.predictImage(os.path.join(execution_path+"/image/", "frame0.jpg"), result_count=5 )
for eachPrediction, eachProbability in zip(predictions, probabilities):
    print(eachPrediction , " : " , eachProbability)
time_used = time_used + time.time() - time_start
#print("The time used is %s", (time.time() - time_start))
print("The total time used is %s", time_used)
print("The time used is %s", (time_used/5))
