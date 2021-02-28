#pragma once

#include "queue.h"
#include <memory>

class Server{
public:
	Server(int q_size);
	void AddPacket(std::shared_ptr<Packet> packet);
	void GetQueueSize(int size) const;

private:
	Queue m_queue;
};
