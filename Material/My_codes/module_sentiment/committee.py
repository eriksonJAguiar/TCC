from sent_classification_module import *
from class_roc import Roc
import collections
from datetime import datetime as dt

if __name__ == '__main__':

	sent = SentClassifiers('dataset-portuguese')

	results = []
	acuracias = []
	logs = []

	nv_acc,nv_ac,nv_p,nv_r,nv_f1,nv_e,_,_ = sent.CMultinomialNV()
	print('Naive')
	print('ac = %f'%nv_acc)
	print('p = %f'%nv_p)
	print('r = %f'%nv_r)
	print('f1 = %f'%nv_f1)
	print('e = %f'%nv_e)
	print('---------------')

	l = 'nv',nv_acc,nv_p,nv_r,nv_f1,nv_e,str(dt.now())
	logs.append(l)

	svm_acc,svm_ac,svm_p,svm_r,svm_f1,svm_e,_,_ = sent.CSuportVectorMachine()
	print('SVM')
	print('ac = %f'%svm_acc)
	print('p = %f'%svm_p)
	print('r = %f'%svm_r)
	print('f1 = %f'%svm_f1)
	print('e = %f'%svm_e)
	print('---------------')

	l = 'svm',svm_acc,svm_p,svm_r,svm_f1,svm_e,str(dt.now())
	logs.append(l)
	
	dt_acc,dt_ac,dt_p,dt_r,dt_f1,dt_e,_,_ = sent.CDecisionTree()
	print('Decisao')
	print('ac = %f'%dt_acc)
	print('p = %f'%dt_p)
	print('r = %f'%dt_r)
	print('f1 = %f'%dt_f1)
	print('e = %f'%dt_e)
	print('---------------')

	l = 'dt',dt_acc,dt_p,dt_r,dt_f1,dt_e,str(dt.now())
	logs.append(l)

	rf_acc,rf_ac,rf_p,rf_r,rf_f1,rf_e,_,_ = sent.CRandomForest()
	print('Forest')
	print('ac = %f'%rf_acc)
	print('p = %f'%rf_p)
	print('r = %f'%rf_r)
	print('f1 = %f'%rf_f1)
	print('e = %f'%rf_e)
	print('---------------')

	l = 'rf',rf_acc,rf_p,rf_r,rf_f1,rf_e,str(dt.now())
	logs.append(l)

	rl_acc,rl_ac,rl_p,rl_r,rl_f1,rl_e,_,_ = sent.CLogistRegression()
	print('Logistic')
	print('ac = %f'%rl_acc)
	print('p = %f'%rl_p)
	print('r = %f'%rl_r)
	print('f1 = %f'%rl_f1)
	print('e = %f'%rl_e)
	print('---------------')

	l = 'rl',rl_acc,rl_p,rl_r,rl_f1,rl_e,str(dt.now())
	logs.append(l)

	sent.write_csv(logs,'logs')

	results.append(nv_ac)
	results.append(svm_ac)
	results.append(dt_ac)
	results.append(rf_ac)
	results.append(rl_ac)

	acuracias.append(nv_acc)
	acuracias.append(svm_acc)
	acuracias.append(dt_acc)
	acuracias.append(rf_acc)
	acuracias.append(rl_acc)

	pesos = sent.calc_weigth(acuracias)

	k = 10


	lines = []

	names = ['naive','svm','tree','forest','logistic','cm']

	ac,cmm_ac,p,r,f1,e,_,_ = sent.committee(k,pesos)

	results.append(cmm_ac)

	print("Comitê")
	print("Acuracia %f"%ac)
	print("Precisao %f"%p)
	print("Recall %f"%r)
	print("F1 Score %f"%f1)
	print("Erro %f"%e)
	print("--------------------------")

	l = 'cm',ac,p,r,f1,e,str(dt.now())
	lines.append(l)

	sent.write_csv(lines,'committee')

	sent.box_plot(results,names,'comparação entre algoritmos')


	

