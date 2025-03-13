import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Définition du backlog avec une estimation optimiste, moyenne et pessimiste
backlog = [
    (3, 5, 8),
    (5, 8, 13),
    (1, 2, 3),
    (8, 13, 21),
    (3, 5, 8),
    (5, 8, 13),
    (1, 2, 3),
    (8, 13, 21)
] * 9  # Simule un backlog de 72 tickets

num_simulations = 10000
sprint_velocity = (29, 33, 37)  # Fourchette de vélocité en story points
sprint_length = 2  # Durée du sprint en semaines

# Fonction de simulation
def monte_carlo_simulation(backlog, sprint_velocity, num_simulations):
    completion_times = []
    
    for _ in range(num_simulations):
        # Générer une estimation aléatoire pour chaque ticket
        estimated_backlog = [np.random.randint(low, high+1) for low, _, high in backlog]
        total_story_points = sum(estimated_backlog)
        
        # Générer une vélocité aléatoire
        velocity = np.random.randint(sprint_velocity[0], sprint_velocity[2]+1)
        
        # Calcul du nombre de sprints nécessaires
        num_sprints = total_story_points / velocity
        completion_times.append(num_sprints)
    
    return completion_times

# Exécuter la simulation
results = monte_carlo_simulation(backlog, sprint_velocity, num_simulations)

# Tracer la distribution des résultats
plt.figure(figsize=(10, 6))
sns.histplot(results, bins=30, kde=True)
plt.axvline(np.percentile(results, 50), color='red', linestyle='dashed', label='50% chance')
plt.axvline(np.percentile(results, 80), color='blue', linestyle='dashed', label='80% chance')
plt.axvline(np.percentile(results, 95), color='green', linestyle='dashed', label='95% chance')
plt.xlabel('Nombre de sprints pour compléter le backlog')
plt.ylabel('Fréquence')
plt.legend()
plt.title('Simulation de Monte Carlo - Estimation du Backlog')
plt.show()
