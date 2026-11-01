from kb_loader import load_rules
from engine import ForwardChainingEngine

KB_PATH = "kb/laptop_rules.json"

def collect_initial_facts():
    facts = []
    # TODO: Ask more questions to collect facts for reasoning

    budget = input("what is your budget? (low/medium/high): ").lower()
    if budget == "high":
        facts.append("budget_high")
    elif budget == "medium":
        facts.append("budget_medium")
    else:
        facts.append("budget_low")


    if input("Is portability important? (y/n): ").lower().startswith("y"):
        facts.append("portable")
    if input("Do you need long battery life? (y/n): ").lower().startswith("y"):
        facts.append("long_battery")
    if input("Do you need the laptop for gaming? (y/n): ").lower().startswith("y"):
        facts.append("gaming")
    if input("Do you do creative work? (y/n): ").lower().startswith("y"):
        facts.append("creative_work")
    if input("Is the laptop mainly for work? (y/n): ").lower().startswith("y"):
        facts.append("office_only")
    os = input("What operating system do you prefer? (Windows/macOS/Linux): ").lower()
    if os == "windows":
        facts.append("pref_os_windows")
    elif os == "macos":
        facts.append("pref_os_macos")
    elif os == "linux":
        facts.append("pref_os_linux")

    if input("Do you need AI acceleration? (y/n): ").lower().startswith("y"):
        facts.append("needs_ai_accel")
    if input("Do you prefer a large screen? (y/n): ").lower().startswith("y"):
        facts.append("large_screen")
    if input("Do you travel often? (y/n): ").lower().startswith("y"):
        facts.append("travel_often")
    return facts

def main():
    # TODO: Load rules, create engine, assert facts, and run inference
    rules = load_rules(KB_PATH)
    engine = ForwardChainingEngine(rules)
    initial_facts = collect_initial_facts()
    engine.assert_facts(initial_facts)  
    engine.run()
    results = engine.conclusions()

    print("\nRecommendations:")
    for recommendation in results["recommendations"]:
        print(recommendation)

    print("\nSpecifications:")        
    for spec in results["specs"]:
        print(spec) 

    print("Rules fired:")
    for item in engine.trace:
        print(item["rule"]) 

if __name__ == "__main__":
    main()
