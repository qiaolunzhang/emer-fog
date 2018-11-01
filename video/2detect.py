from imageai.Prediction import ImagePrediction
import os
import time

execution_path = os.getcwd()

prediction = ImagePrediction()
prediction.setModelTypeAsResNet()
prediction.setModelPath(os.path.join(execution_path, "resnet50_weights_tf_dim_ordering_tf_kernels.h5"))
prediction.loadModel()

time_start = time.time()
predictions, probabilities = prediction.predictImage(os.path.join(execution_path+"/image/", "frame0.jpg"), result_count=5 )
for eachPrediction, eachProbability in zip(predictions, probabilities):
    print(eachPrediction , " : " , eachProbability)
print("The time used is %s", (time.time() - time_start))
