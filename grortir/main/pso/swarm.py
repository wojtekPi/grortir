"""Represents swarm."""
import numpy as np

from grortir.main.pso.particle import Particle


class Swarm(object):
    """Class which represent swarm."""

    def __init__(self, process, stages, number_of_particles):
        self.stages = stages
        self.process = process
        self.number_of_particles = number_of_particles
        self.particles = [Particle(stages, self.process) for i in
                          range(number_of_particles)]
        self.best_particle_quality = np.inf
        self.best_particle = self.particles[0]

    def initialize(self):
        """Initialize all particles in swarm."""
        for particle in self.particles:
            particle.initialize()

    def do_single_iteration(self):
        """Iterate one time."""
        for particle in self.particles:
            particle.update_values()
        self._update_best_particle()
        self._update_velocieties()
        for particle in self.particles:
            particle.move()

    def _update_best_particle(self):
        for particle in self.particles:
            if particle.best_quality < self.best_particle_quality:
                self.best_particle = particle
                self.best_particle_quality = particle.best_quality

    def _update_velocieties(self):
        for particle in self.particles:
            particle.update_velocities(self.best_particle)

    def post_processing(self):
        self.best_particle.current_control_params = self.best_particle.best_positions
        self.best_particle.current_input = self.best_particle.input_vectors_for_best_pos
        for stage in self.stages:
            stage.control_params = self.best_particle.best_positions[stage]
        self.best_particle.update_input_vectors()
        # input vectors for best particle is output (x) vector

