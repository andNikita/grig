#pragma once

class Packet{
public:
	Packet (double arrivalTime, double serviceTime);
	double GetArrivalTime() const;
	double GetServiceTime() const;

private:
	double m_arrivalTime;
	double m_serviceTime;
};
