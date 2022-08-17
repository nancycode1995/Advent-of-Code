#!/usr/bin/env python3

from functools import reduce, cache
from numpy import uint16
from abc import ABC, abstractmethod

from solution import SolutionBase

def make_thunk(string, nodes):
    node = NodeSignal.compile(string, nodes)
    if node:
        return lambda: node
    else: return lambda: nodes[string]

class Node(ABC):
    @property
    @abstractmethod
    def value(self):
        """Calculate the signal at this node."""
        ...

    @classmethod
    @abstractmethod
    def compile(cls, string, nodes: dict):
        """Attempt to compile this node from a string designator."""
        ...

class NodeSignal(Node):
    def __init__(self, value):
        self._value = value

    @property
    @cache
    def value(self):
        return self._value

    @classmethod
    def compile(cls, string, nodes: dict):
        try:
            return cls(uint16(string))
        except ValueError:
            pass

class NodeOperation(Node):
    def __init__(self, function, *inputs):
        self.function = function
        self.inputs = inputs

    @property
    @cache
    def value(self):
        return self.function(*(node().value for node in self.inputs))

class NodeWire(NodeOperation):
    def __init__(self, wire_input):
        super().__init__(lambda x: x, wire_input)

    @classmethod
    def compile(cls, string, nodes: dict):
        return cls(lambda: nodes[string.strip()])

class NodeNot(NodeOperation):
    def __init__(self, wire_input):
        super().__init__(lambda x: ~x, wire_input)

    @classmethod
    def compile(cls, string, nodes: dict):
        try:
            opcode, operand = string.split()
            assert(opcode == "NOT")
            return cls(make_thunk(operand, nodes))
        except (AssertionError, ValueError):
            pass

class NodeLeftShift(NodeOperation):
    def __init__(self, wire_input, amount):
        super().__init__(lambda x: x << amount, wire_input)

    @classmethod
    def compile(cls, string, nodes: dict):
        try:
            wire, opcode, amount = string.split()
            assert(opcode == "LSHIFT")
            return cls(make_thunk(wire, nodes), int(amount))
        except (AssertionError, ValueError):
            pass

class NodeRightShift(NodeOperation):
    def __init__(self, wire_input, amount):
        super().__init__(lambda x: x >> amount, wire_input)

    @classmethod
    def compile(cls, string, nodes: dict):
        try:
            wire, opcode, amount = string.split()
            assert(opcode == "RSHIFT")
            return cls(make_thunk(wire, nodes), int(amount))
        except (AssertionError, ValueError):
            pass

class NodeAnd(NodeOperation):
    def __init__(self, *inputs):
        def function(*inputs):
            return reduce(lambda a, b: a & b, inputs)
        super().__init__(function, *inputs)

    @classmethod
    def compile(cls, string, nodes: dict):
        try:
            a, opcode, b = string.split()
            assert(opcode == "AND")
            return cls(make_thunk(a, nodes), make_thunk(b, nodes))
        except (AssertionError, ValueError):
            pass

class NodeOr(NodeOperation):
    def __init__(self, *inputs):
        def function(*inputs):
            return reduce(lambda a, b: a | b, inputs)
        super().__init__(function, *inputs)

    @classmethod
    def compile(cls, string, nodes: dict):
        try:
            a, opcode, b = string.split()
            assert(opcode == "OR")
            return cls(make_thunk(a, nodes), make_thunk(b, nodes))
        except (AssertionError, ValueError):
            pass

class Circuit:
    def __init__(self, nodes: dict):
        self.nodes = nodes

    @classmethod
    def compile(cls, string):
        """Compile a circuit from the assembly string."""

        nodes = {}

        for line in string.split("\n"):
            left, right = line.split("->")
            for node_type in NodeSignal, NodeNot, NodeAnd, NodeOr, NodeLeftShift, NodeRightShift, NodeWire:
                node = node_type.compile(left, nodes)
                if node:
                    nodes[right.strip()] = node
                    break

        return cls(nodes)

class Solution(SolutionBase):
    def part_one(self):
        circuit = Circuit.compile(self.input)
        #for name, node in sorted(circuit.nodes.items()):
        #    print(f"{name}: {node.value}")
        return circuit.nodes["a"].value

    def part_two(self):
        circuit = Circuit.compile(self.input)
        value = circuit.nodes["a"].value
        circuit = Circuit.compile(self.input) # invalidate cache
        circuit.nodes["b"] = NodeSignal(value)
        return circuit.nodes["a"].value

solution = Solution.instantiate(7)

if __name__ == "__main__":
    solution.run()
