import math

class Population():
    def __init__(self, init_pop, r):
        self.current_population = init_pop
        self.growth_rate = r

    def oneYearPopUpdate( self, growth_rate_error):
        actual_growth_rate = self.growth_rate + growth_rate_error
        self.current_population = self.current_population * math.exp(actual_growth_rate/100)

    def predictPopulation(self, num_years):
        population_predict = self.current_population * math.exp((self.growth_rate/100)*num_years)
        return population_predict

    def predictNumYears(self, new_population):
        num_years = math.log(new_population/self.current_population)/(self.growth_rate/100)
        return num_years

    def doublingTime(self):
        double_population = 2 * self.current_population
        time_double = self.predictNumYears(double_population)
        return time_double

Earth_Human = Population(7594000000, 1.1)

t_20billion = Earth_Human.predictNumYears(20_000_000_000)
print("The population will get to 20 billion after",t_20billion,"years\n")

predicted_population = Earth_Human.predictPopulation(10)
print("The predicted population after 10 years will be",predicted_population,"\n")

growth_rate_errors = [0.01, -0.025, 0.03, 0.016, -0.04, 0.02, 0.01, -0.02, 0.012, -0.017]
for error in growth_rate_errors:
    Earth_Human.oneYearPopUpdate(error)
print("The actual population after 10 years will be",Earth_Human.current_population,"\n")

difference = predicted_population - Earth_Human.current_population
print("The difference between the predicted population and the actual population after 10 years is", difference,"\n")

double_time = Earth_Human.doublingTime()
print("The population will double after",double_time,"years\n")

