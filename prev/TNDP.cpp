#include <iostream>
#include <vector>



class TNDP
{
private:
    int num_of_objectives;
    int num_of_variables;
    std::vector<double> objectives;
    int dominated_solutions;
    int features;
    std::vector<double> objectives;

public:
    bool dominates(const Individual& other);

};

bool Individual::dominates(const Individual & other)
{
    bool and_cond = true;
    bool or_cond = false;
    for (int i = 0; i < 7; i++)
    {
        and_cond = and_cond && this->objectives[i] <= other.objectives[i];
        or_cond = and_cond || this->objectives[i] <= other.objectives[i];
    }
    return and_cond && or_cond;
}