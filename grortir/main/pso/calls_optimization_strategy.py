"""Represents optimization strategy for PSO."""
from grortir.main.pso.calls_group_optimization_strategy import \
    CallsGroupOptimizationStrategy
from grortir.main.pso.optimization_strategy import OptimizationStrategy


class CallsOptimizationStrategy(OptimizationStrategy):
    """Represents optimization strategy Calls stages for PSO."""

    def getGroupOptimizationStrategy(self,stages_in_group):
        return CallsGroupOptimizationStrategy(stages_in_group)

