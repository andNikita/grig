#include "server.h"

Server::Server(int q_size = -1){
	m_queue.SetMaxSize(q_size);
}

void Server::AddPacket (std::shared_ptr<Packet> p){
		m_queue.AddPacket(p);
}
