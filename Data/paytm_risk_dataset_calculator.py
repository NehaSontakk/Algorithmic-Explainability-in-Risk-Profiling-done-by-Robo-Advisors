import pandas as pd
w_11=1
w_21=0.83
w_22=0.83
w_31=0.65
w_32=0.65
w_41=0.5
w_51=0.8
w_52=0.8
w_61=0.7
w_62=0.65

x_11 = [0.2]
## Add X_11 = [0.5] and [1]
x_21 = [1,0.8,0.4,0.6,0.1]
x_22 = [0.2,0.4,0.6,0.8,1]
x_31 = [1,0.8,0.6,0.4,0.2]
x_32 = [0.1,0.3,0.6,0.9,1]
x_41 = [0.4,0.6,0.5,0.4,0.8]
x_51 = [0.65,0.6,0.4,0.5,1]
x_52 = [0.5,0.8,0.65,0.6,0.7]
x_61 = [1,0.9,0.5,0.2,0.1]
x_62 = [0.2,0.3,0.5,0.9,1]

list_of_values = []
for i in range(len(x_11)):
	for j in range(len(x_21)):
		for k in range(len(x_22)):
			for l in range(len(x_31)):
				for m in range(len(x_32)):
					for n in range(len(x_41)):
						for o in range(len(x_51)):
							for p in range(len(x_52)):
								for q in range(len(x_61)):
									for r in range(len(x_62)):
										list_of_values.append([w_11,x_11[i],w_21,x_21[j],w_22,x_22[k],w_31,x_31[l],w_32,x_32[m],w_41,x_41[n],w_51,x_51[o],w_52,x_52[p],w_61,x_61[q],w_62,x_62[r],w_11*x_11[i]+ w_21*x_21[j] + w_22*x_22[k]*x_11[i] + w_31*x_31[l]*x_11[i]*x_21[j] + w_32*x_32[m] + w_41*x_41[n]*x_11[i]*x_21[j]*x_52[o] + w_51*x_51[o]*x_11[i]*x_21[j]*x_52[p] + w_52*x_52[p]*x_51[o]*x_11[i]*x_21[j] + w_61*x_61[q]*x_11[i]*x_21[j]+w_62*x_62[r]*x_11[i]*x_21[j]*x_32[m]*x_52[p]])


df = pd.DataFrame(list_of_values,columns=["w_11","x_11","w_21","x_21","w_22","x_22","w_31","x_31","w_32","x_32","w_41","x_41","w_51","x_51","w_52","x_52","w_61","x_61","w_62","x_62","output"])
df.to_csv('risk_permutations_14_oct_2019.csv', index=False)





