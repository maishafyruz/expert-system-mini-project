from dataclasses import dataclass
from typing import List, Set, Dict, Any

@dataclass
class Rule:
    antecedents: List[str]
    consequent: str
    priority: int = 0
    name: str = ""

class ForwardChainingEngine:
    def __init__(self, rules: List[Rule]):
        self.rules = rules
        self.facts: Set[str] = set()
        self.trace: List[Dict[str, Any]] = []

    def assert_facts(self, initial: List[str]) -> None:
        """Store initial facts into the working memory."""
        self.facts.update(initial)

    def can_fire(self, rule: Rule) -> bool:
        """TODO: Return True if all antecedents are true and consequent not yet known."""
        return all(antecedent in self.facts for antecedent in rule.antecedents) and rule.consequent not in self.facts

    def run(self) -> None:
        """TODO: Implement the forward chaining loop."""
        # while there are rules that can fire:
        #     select one rule (students decide tie-breaking)
        #     add its consequent to facts
        #     record in trace
        while True:
            fireable_rules = [rule for rule in self.rules if self.can_fire(rule)]

            if not fireable_rules:
                break

            rule = max(fireable_rules, key=lambda r: r.priority)

            self.facts.add(rule.consequent)

            self.trace.append({
                "rule": rule.name,
                "antecedents": rule.antecedents,
                "consequent": rule.consequent
            })

    def conclusions(self) -> Dict[str, List[str]]:
        """TODO: Return separated results (recommendations, specs, other facts)."""

        recommendations = []
        specs = []
        other_facts = []

        for fact in self.facts:
            if fact.startswith("recommend:"):
                recommendations.append(fact)
            elif fact.startswith("spec:"):
                specs.append(fact)
            else:
                other_facts.append(fact)

        return {
            "recommendations": recommendations,
            "specs": specs,
            "other_facts": other_facts
        }