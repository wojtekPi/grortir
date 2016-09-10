"""Represents optimization strategy for group in PSO."""
import numpy as np

from grortir.main.pso.group_optimization_strategy import \
    GroupOptimizationStrategy


class CallsGroupOptimizationStrategy(GroupOptimizationStrategy):
    """Represents optimization strategy for group in PSO."""

    def __init__(self, stages_in_group):
        self.stages_in_group = stages_in_group
        self.max_cost = 0
        self.expected_quality = np.inf

    def initialize(self):
        max_cost = 0
        for stage in self.stages_in_group:
            max_cost += stage.max_calls
            if self.expected_quality > stage.maximum_acceptable_quality:
                self.expected_quality = stage.maximum_acceptable_quality
        self.max_cost = max_cost

    def should_continue(self, best_particle):
        return self._is_safe_cost() and not self._is_enough_quality(
            best_particle)

    def _is_safe_cost(self):
        current_cost = 0
        for stage in self.stages_in_group:
            current_cost += stage.get_cost()
        return current_cost < self.max_cost

    def _is_enough_quality(self, best_particle):
        return best_particle.best_quality <= self.expected_quality
