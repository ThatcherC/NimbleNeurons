#include <iostream>
#include <math.h>
#include <stdlib.h>
#include <time.h>

float alpha = 0.8;
float theta = 0;

//UPDATE LOOPS WITH LEN OF ARRAYS INSTEAD OF CONSTS (EASIER TO CHANGE)

struct neuron{
	const int numweights;
	float weight[5];
	float sum;
	float output;
	float error;
};

int trainingIns[4][2] = {{0,0},{0,1},{1,0},{1,1}};
int inputLayer [2];
neuron hidden [4];
neuron output [2];
int target [4][2] = {{0,0},{0,0},{1,1},{1,1}};\
int o,n,w,i;

//void train(){
	
void setup(){
	srand(time(NULL));
	for(n=0;n<4;n++){				//4=len hidden
		for(w=0;w<5;w++){
			hidden[n].weight[w] = ((float) rand()) / (float) RAND_MAX;
		}
	}
	for(n=0;n<2;n++){
		for(w=0;w<5;w++){
			output[n].weight[w] = ((float) rand()) / (float) RAND_MAX;
		}
	}
}

float activation(float x){
	return 1/(1+(pow(2.7182,0-x)));
}

float dactivation(float x){
	return (activation(x+0.001)-activation(x))/0.001;
}

void forwardProp(int ins[2]){			//perhaps change to array, len
	inputLayer[0] = ins[0];
	inputLayer[1] = ins[1];
	for(n = 0; n < 4;n++){		//n=num hiddens
		for(i=0;i<2;i++){		//i = arrayLen
			hidden[n].sum+=hidden[n].weight[i]*ins[i];
		}
		hidden[n].output = activation(hidden[n].sum-theta);
	}
	for(o = 0;o<2;o++){			//o=num outs
		for(n = 0; n<4;n++){
			output[o].sum+=output[o].weight[n]*hidden[n].output;
		}
		output[o].output=activation(output[o].sum-theta);
	}
}

void calculateError(int targ[2]){
	for(o=0;o<2;o++){
		output[o].error=targ[o]-output[o].output;
	}
	for(n=0;n<4;n++){
		for(o=0;o<2;o++){
			hidden[n].error+=output[o].weight[n]*output[o].error;
		}
	}
}

void updateWeights(){
	for(n=0;n<4;n++){				//4=len hidden
		for(w=0;w<2;w++){			//2 input nodes
			hidden[n].weight[w] += alpha*hidden[n].error*dactivation(hidden[n].sum-theta)*inputLayer[w];
		}
	}
	//std::cout << "toast";
	for(n=0;n<2;n++){
		for(w=0;w<4;w++){			//four hidden neurons
			std::cout << output[n].error << "   " << dactivation(output[n].sum-theta) << "   " << hidden[n].weight[w] << "\n";
			output[n].weight[w] += alpha*output[n].error*dactivation(output[n].sum-theta)*hidden[n].output;
		}
	}
}

int main(){
	std::cout << "Hello, world!\n";
	std::cout << activation(0) << "   " << dactivation(0) << "\n";
	setup();
	forwardProp(trainingIns[1]);
	calculateError(target[0]);
	updateWeights();
	for(n=0;n<4;n++){
		std::cout << "Neuron " << n+5 << " error = " << hidden[n].error << "\n";
		//for(int w=0;w<5;w++){
	//		std::cout << hidden[n].weight[w];
	//	}
	}
	for(int c=0;c<50;c++){
		if(c%4==0){
			std::cout << "Start\n";
		}
		forwardProp(trainingIns[c%4]);
		std::cout << output[0].output << "   " << output[1].output << "\n";
		calculateError(target[c%4]);
		updateWeights();
		//std::cout << "Neuron " << 1 << " error = " << output[0].output << "\n";
	}
	return 0;
}
