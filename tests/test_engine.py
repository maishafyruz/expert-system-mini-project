import unittest

from kb_loader import load_rules
from engine import ForwardChainingEngine


class TestExpertSystem(unittest.TestCase):

    def test_premium_ultrabook(self):
        rules = load_rules("kb/laptop_rules.json")
        engine = ForwardChainingEngine(rules)

        engine.assert_facts([
            "budget_high",
            "portable",
            "long_battery"
        ])

        engine.run()
        results = engine.conclusions()

        self.assertIn(
            "recommend:premium_ultrabook",
            results["recommendations"]
        )

    def test_ai_acceleration(self):
        rules = load_rules("kb/laptop_rules.json")
        engine = ForwardChainingEngine(rules)

        engine.assert_facts([
            "needs_ai_accel"
        ])

        engine.run()
        results = engine.conclusions()

        self.assertIn(
            "spec:gpu_with_tensor_cores",
            results["specs"]
        )

    def test_macos_preference(self):
        rules = load_rules("kb/laptop_rules.json")
        engine = ForwardChainingEngine(rules)

        engine.assert_facts([
            "pref_os_macos"
        ])

        engine.run()
        results = engine.conclusions()

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

        engine.assert_facts(["gaming"])
        engine.run()

        results = engine.conclusions()

        self.assertIn(
            "recommend:gaming_laptop",
            results["recommendations"]
        )

if __name__ == "__main__":
    unittest.main()