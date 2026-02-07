
import numpy as np

def cosine_similarity(v1, v2):
	# Implement your code here
	vec1=np.array(v1)
	vec2=np.array(v2)

	#checking shape
	if vec1.shape!=vec2.shape or vec1.size==0:
		return -1.0
	
	v1_norm=np.linalg.norm(v1)
	v2_norm=np.linalg.norm(v2)

	if v1_norm==0 or v2_norm==0:
		return -1.0
	
	return np.dot(vec1,vec2)/(v1_norm*v2_norm)
