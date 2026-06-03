# 🎨 Task 02: Prompting for Creativity
![Header](https://github.com/user-attachments/assets/7a5a5895-ed8d-4391-9f82-9f1595a88354
)
![Few-Shot Prompting](https://img.shields.io/badge/Technique-Few_Shot-success?style=for-the-badge)
![Creative Writing](https://img.shields.io/badge/Focus-Creative_Writing-purple?style=for-the-badge)

## 🎯 Objective
To explore how few-shot prompting and tone modifiers influence a model's creative output, specifically in generating unique, out-of-the-box startup ideas.

---

## 🧠 The Few-Shot Prompt Design

**System Persona:** You are "The Visionary," an eccentric, highly creative startup incubator. You generate wild, futuristic, yet logically sound business ideas.

### Few-Shot Examples Provided to the LLM:
* **Input:** A startup for pets.
* **Output:** **Bark & Byte:** A smart-collar tech company that uses AI to translate dog barks into text messages sent to the owner's phone.
* **Input:** A startup for coffee.
* **Output:** **Nebula Brews:** A cafe chain that uses centrifuge technology to zero-gravity brew coffee beans for a perfectly smooth espresso.

**🎯 Target Input:** A startup for fitness.

---

## 🔬 Variant Testing & Comparison

### 👔 Variant A: Strict/Corporate Tone
* **Added Instruction:** "Maintain a highly corporate, investor-pitch tone emphasizing ROI."
* **Result:** **AeroFit Analytics:** A B2B SaaS platform utilizing biometric wearables to track employee cardiovascular health, reducing corporate insurance premiums by 15%.
* **Critique:** High detail, but lacks the requested creative flair. Very dry.

### 🌪️ Variant B: Whimsical Tone (🏆 The Winner)
* **Added Instruction:** "Maintain a whimsical, slightly chaotic tone. Make it sound like a mad scientist pitching the idea."
* **Result:** **Kineti-Craze Generators!** Behold! We hook up high-resistance kinetic dynamo suits to gym-goers. They sweat, they burn calories, and they power the city grid! It's a win-win for humanity!
* **Critique:** The few-shot examples successfully guided the structure, while the whimsical tone instruction completely transformed the delivery, making it highly creative.

---
*Created as part of the SkillCraft Technology Prompt Engineering Internship*
