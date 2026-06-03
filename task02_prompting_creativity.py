from textwrap import dedent

task_title = "Task 02: Prompting for Creativity"

system_persona = dedent("""
You are "The Visionary," an eccentric, highly creative startup incubator.
You generate wild, futuristic, yet logically sound business ideas.
""").strip()

few_shot_examples = [
    {
        "input": "A startup for pets.",
        "output": "Bark & Byte: A smart-collar tech company that uses AI to translate dog barks into text messages sent to the owner's phone."
    },
    {
        "input": "A startup for coffee.",
        "output": "Nebula Brews: A cafe chain that uses centrifuge technology to zero-gravity brew coffee beans for a perfectly smooth espresso."
    }
]

target_input = "A startup for fitness."

variant_a_instruction = "Maintain a highly corporate, investor-pitch tone emphasizing ROI."
variant_b_instruction = "Maintain a whimsical, slightly chaotic tone. Make it sound like a mad scientist pitching the idea."

variant_a_result = "AeroFit Analytics: A B2B SaaS platform utilizing biometric wearables to track employee cardiovascular health, reducing corporate insurance premiums by 15%."
variant_b_result = "Kineti-Craze Generators! Behold! We hook up high-resistance kinetic dynamo suits to gym-goers. They sweat, they burn calories, and they power the city grid! It's a win-win for humanity!"

def print_section(title, content):
    print("
" + "=" * 70)
    print(title)
    print("=" * 70)
    print(content)

print_section("Title", task_title)
print_section("System Persona", system_persona)

print("
" + "=" * 70)
print("Few-Shot Examples")
print("=" * 70)
for i, example in enumerate(few_shot_examples, start=1):
    print(f"
Example {i}")
    print(f"Input: {example['input']}")
    print(f"Output: {example['output']}")

print_section("Target Input", target_input)

print("
" + "=" * 70)
print("Variant A: Strict/Corporate Tone")
print("=" * 70)
print(f"Instruction: {variant_a_instruction}")
print(f"Result: {variant_a_result}")

print("
" + "=" * 70)
print("Variant B: Whimsical Tone")
print("=" * 70)
print(f"Instruction: {variant_b_instruction}")
print(f"Result: {variant_b_result}")

print("
" + "=" * 70)
print("Conclusion")
print("=" * 70)
print("The whimsical tone is more creative and engaging, while the corporate tone is more formal but less imaginative.")
