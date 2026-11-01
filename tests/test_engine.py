import unittest

from kb_loader import load_rules
from engine import ForwardChainingEngine


class TestExpertSystem(unittest.TestCase):

    def test_premium_ultrabook(self):
        rules = load_rules("kb/laptop_rules.json")
        engine = ForwardChainingEngine(rules)

        #Input facts for a user with a high budget, portability, and long battery life
        engine.assert_facts([
            "budget_high",
            "portable",
            "long_battery"
        ])
        
        engine.run()
        results = engine.conclusions()

        #Expected output: The system should recommend a premium ultrabook based on the input facts
        self.assertIn(
            "recommend:premium_ultrabook",
            results["recommendations"]
        )

    def test_ai_acceleration(self):
        rules = load_rules("kb/laptop_rules.json")
        engine = ForwardChainingEngine(rules)

        #Input facts for a user who needs AI acceleration
        engine.assert_facts([
            "needs_ai_accel"
        ])

        engine.run()
        results = engine.conclusions()

        #Expected output: The system should recommend a laptop with a GPU that has tensor cores for AI acceleration
        self.assertIn(
            "spec:gpu_with_tensor_cores",
            results["specs"]
        )

    def test_macos_preference(self):
        rules = load_rules("kb/laptop_rules.json")
        engine = ForwardChainingEngine(rules)

        #Input facts for a user who prefers macOS
        engine.assert_facts([
            "pref_os_macos"
        ])

        engine.run()
        results = engine.conclusions()

        #Expected output: The system should recommend a laptop that runs macOS
        self.assertIn(
            "spec:macos_required",
            results["specs"]
        )
    def test_multi_step_forward_chaining(self):

        from engine import Rule

        rules = [
            Rule(
                antecedents=["gaming"],
                consequent="needs_powerful_gpu",
                name="Gaming Power"
            ),
            Rule(
                antecedents=["needs_powerful_gpu"],
                consequent="recommend:gaming_laptop",
                name="Gaming Recommendation"
            )
        ]

        engine = ForwardChainingEngine(rules)

        #Input facts for a user who is interested in gaming
        engine.assert_facts(["gaming"])
        engine.run()

        results = engine.conclusions()

        #Expected output: The system should recommend a gaming laptop based on the input facts and the rules defined
        self.assertIn(
            "recommend:gaming_laptop",
            results["recommendations"]
        )

if __name__ == "__main__":
    unittest.main()