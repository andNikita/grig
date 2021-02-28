#include "packet.h"

Packet::Packet(double arrivalTime, double serviceTime){
	m_arrivalTime = arrivalTime;
	m_serviceTime = serviceTime;
}

double Packet::GetArrivalTime() const{
	return m_arrivalTime;
}

double Packet::GetServiceTime() const{
	return m_serviceTime;
}