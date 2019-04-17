population_size = 50
evaluation_reps = 10
true_copies = int(population_size * 0.05)
mutated_copies = int(population_size * 0.65)
added_randoms = population_size - true_copies - mutated_copies
# abweichung durch anspielzufall ungefähr +/- 2% der normalen fitness (anspiele auf gegner)
# daher ungefähr im bereich 4%
# mal zwei zur sicherheit
# mal evaluation_reps
# daher ahead = 0.02 * 2 * 2 * population_size**2 * evaluation_reps
ahead = int(0.02 * 4 * population_size**2 * evaluation_reps)
generations = 3