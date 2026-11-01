# Expert System Mini Project Report

## Overview

For this project, I completed a rule-based Laptop Advisor expert system using forward chaining. The program asks the user questions about things such as budget, portability, battery life, gaming, creative work, operating system preference, AI acceleration, screen size, and travel. Based on the user's answers, the system stores facts and applies IF–THEN rules to produce laptop recommendations or specifications.

## Inference Engine

The main reasoning logic is implemented in `engine.py`.

The `can_fire()` function checks whether all antecedents of a rule are already present in the current facts. It also checks that the rule's consequent has not already been added. This prevents the same rule from repeatedly producing the same fact.

The `run()` function performs forward chaining. It checks which rules are able to fire, selects a rule based on priority, adds the rule's consequent to the facts, and records the rule in the trace. The process continues until no more rules can fire.

The `conclusions()` function separates the final facts into recommendations, specifications, and other facts.

## Knowledge Base

The knowledge base is stored in `kb/laptop_rules.json`. The original project included one rule, and I expanded the knowledge base to contain ten rules.

For example, if the user has a high budget, wants portability, and needs long battery life, the system recommends a premium ultrabook.

Other rules provide recommendations or specifications for gaming, creative work, travel, macOS preference, Linux suitability, AI acceleration, and large displays.

## User Input

The `main.py` file collects facts from the user through a series of questions. The answers are converted into facts such as:

- `budget_high`
- `portable`
- `long_battery`
- `gaming`
- `creative_work`
- `pref_os_macos`
- `needs_ai_accel`

These facts are placed into the working memory of the inference engine.

After the facts are collected, the engine runs and prints the recommendations, specifications, and the names of the rules that fired.

## Testing

I created test cases in the `tests` folder to verify that the system produces the expected conclusions.

For example, the facts `budget_high`, `portable`, and `long_battery` correctly produce the recommendation `recommend:premium_ultrabook`.

I also tested the macOS rule and AI acceleration rule. In addition, I included a multi-step forward chaining test where one rule creates a new fact that is then used by another rule.

All of the tests passed successfully.

## Conclusion

This project helped demonstrate how a simple expert system can make decisions using facts, rules, and forward chaining. The inference engine does not contain hardcoded laptop recommendations. Instead, it reads rules from the knowledge base and applies them based on the facts provided by the user. This makes the system easier to expand because additional rules can be added to the knowledge base without changing the main reasoning logic.