#include <iostream>
#include <memory>
#include "packet-generator.h"
#include "simulator.h"

int main(int argc, char** argv){

	if(argc < 5){
		std::cout << "Usage: ./scenario seed lambda mu q_size simTime" << std::endl;
		return -1;
	}

	int seed = atoi(argv[1]);
	double lambda = atof(argv[2]);
	double mu = atof(argv[3]);
	//if q_size < 0 then q_size = inf
	int q_size = atoi(argv[4]);
	time_t simTime = atof(argv[5]);

	std::exponential_distribution<double>::param_type params1(lambda);
	std::exponential_distribution<double>::param_type params2(mu);
	//std::uniform_int_distribution<>::param_type params2(1, 1);
	//PacketGenerator<std::exponential_distribution<double>, std::uniform_int_distribution<>> packetGen(params1, params2);
	PacketGenerator<std::exponential_distribution<double>, std::exponential_distribution<double>> packetGen(params1, params2);

	std::shared_ptr<Server> server(new Server(q_size));
	packetGen.SetServer(server);  

	Simulator sim;
	sim.SetStop(simTime);
	sim.SetSeed(seed);

	packetGen.Start();
	sim.Run();
}
