# ChatGPT Troubleshooting Guide

Quick reference for fixing common problems when ChatGPT doesn't follow the outline.

---

## PROBLEM #1: Made Big Scene Too Small

**Symptom:** 
- Catastrophic event happens privately with few witnesses
- Major crisis resolved quickly in a few paragraphs
- No lasting consequences

**Example:**
> "Caelen tried the technique in the quiet orchard. The strain wobbled briefly. Rachel helped correct it. They talked about being careful."

**Why This Happens:**
ChatGPT defaults to intimate character moments and avoids writing large action scenes.

**Fix Prompt:**
```
REVISION NEEDED - SCALE IS WRONG

This scene should be CATASTROPHIC and PUBLIC, not small and private.

REQUIREMENTS:
- Location: Main square or high-traffic area (NOT quiet orchard)
- Witnesses: Dozens of residents, Council observers, delegation
- Threat level: Multiple buildings at risk, lives endangered
- Duration: Sustained crisis over 800-1200 words, not quick resolution
- Rachel's intervention: Requires FULL abilities, visible time dilation
- Consequences: Injury, property damage, political fallout
- Community impact: Everyone talking about it afterwards

REWRITE the scene with these scale requirements.
```

---

## PROBLEM #2: Used Plot Beat From Wrong Chapter

**Symptom:**
- Chapter 17 includes content that should be in Chapter 35
- Angel realm reveals appearing in Act II instead of Act IV
- Major reveals happening before proper setup

**Example:**
> "Rachel saw her mother step through into the structured realm. Geometric architecture rose around Theryn, angular and precise..."

**Why This Happens:**
ChatGPT sees thematic connection and uses cool ideas immediately instead of saving them.

**Fix Prompt:**
```
STOP - WRONG PLOT BEAT

This chapter includes content reserved for Chapter [X].

RESERVED FOR LATER:
- Direct angel realm visions (Chapter 41-42)
- Theryn crossing details (Act IV)
- Seal aperture opening (Chapter 41)
- Meeting father figure (Chapter 43)

THIS CHAPTER SHOULD HAVE:
- [Paste correct outline section]

REMOVE all content about [specific thing] and replace with [correct content].
```

---

## PROBLEM #3: Resolved Tension Too Quickly

**Symptom:**
- Council makes quick decision
- Community reaches consensus easily
- Questions get clear answers
- Conflict wraps up neatly

**Example:**
> "The Council deliberated and agreed Rachel was an asset. They granted her full autonomy. Everyone felt reassured."

**Why This Happens:**
ChatGPT likes resolution and closure; avoids sustained uncertainty.

**Fix Prompt:**
```
REVISION NEEDED - TENSION RESOLVED TOO QUICKLY

Act II should BUILD pressure, not release it.

PROBLEMS:
- Council decision too clear/fast
- Community consensus unrealistic
- Uncertainty eliminated instead of deepened
- No new complications emerged

REQUIREMENTS FOR REWRITE:
- Council DIVIDED - some want control, others want study, others uncertain
- Decision creates NEW problems, not solutions
- Community remains fractured - different factions emerge
- More questions raised than answered
- End with INCREASED uncertainty, not decreased

REWRITE with sustained tension.
```

---

## PROBLEM #4: Power Progression Wrong

**Symptom:**
- Rachel has abilities she shouldn't have yet
- Jumps in capability instead of incremental growth
- Explains mechanisms she doesn't understand yet

**Example:**
> "Rachel understood now - the seal recognized her angel heritage. She could open passages at will, moving between realms..."

**Why This Happens:**
ChatGPT extrapolates from hints in the outline and jumps ahead.

**Fix Prompt:**
```
POWER PROGRESSION ERROR

Rachel has abilities/understanding she shouldn't have yet.

BY CHAPTER [X], RACHEL SHOULD HAVE:
- [List abilities from outline progression]
- [Specific capability levels]

BY CHAPTER [X], RACHEL SHOULD NOT HAVE:
- Seal aperture control (Chapter 41)
- Complete understanding (Act IV)
- Realm-crossing ability (Chapter 42)
- [Other advanced abilities]

CURRENT CAPABILITY:
- [Specify exact level for this chapter]
- [Include: range, warmth location, control level]

REWRITE showing ONLY these abilities.
```

---

## PROBLEM #5: Character Acting Out of Character

**Symptom:**
- Sivara being warm instead of measured
- Arathen being distant instead of protective
- Rachel being confident instead of uncertain
- Maelin being cold instead of practical-loving

**Example:**
> "Sivara hugged Rachel warmly. 'You're perfect as you are,' she said with a bright smile."

**Why This Happens:**
ChatGPT defaults to generic supportive characters; loses specific voices.

**Fix Prompt:**
```
CHARACTER VOICE CORRECTION

[Character name] is acting out of character.

ESTABLISHED TRAITS:
Sivara: Measured, analytical, protective through structure not warmth
Arathen: Steadying presence, protective without smothering, quiet strength
Rachel: Uncertain, capable but doubting, guilty about endangering others
Maelin: Practical care, sharp edges, love through action not words

WRONG MOMENTS:
- [Specific dialogue/action that's OOC]

REWRITE with correct character voice:
- Sivara should: [Specify tone - analytical, measured, etc.]
- Show care through: [Structure, teaching, standing up for her]
- NOT through: [Overt warmth, reassurance, softness]
```

---

## PROBLEM #6: Skipped Important Beats

**Symptom:**
- Outline specifies 4-5 scenes but chapter only has 2
- Important character reactions missing
- Setup for next chapter not present

**Example:**
Chapter 21 outline says:
- Young walker asks to train
- Rachel struggles to explain
- Sivara allows observation
- Walker takes notes
- Small attempt with mixed results
- Building tension about bigger attempt

But chapter only includes:
- Young walker asks
- Rachel says no
- End

**Fix Prompt:**
```
INCOMPLETE CHAPTER - MISSING BEATS

The outline specifies multiple scenes/beats this chapter must include.
Current draft only includes [X] of [Y] required beats.

OUTLINE REQUIREMENTS:
[Paste full list]

MISSING FROM DRAFT:
1. [Specific scene/beat]
2. [Specific scene/beat]
3. [Specific scene/beat]

PLEASE EXPAND the chapter to include ALL required beats.
Each beat should have 300-500 words of development.
```

---

## PROBLEM #7: Wrong Tone/Pacing

**Symptom:**
- Slow contemplative chapter when it should be urgent
- Fast action when it should be character development
- Light tone when it should be tense

**Example:**
Major crisis chapter but ChatGPT wrote:
> "Rachel calmly approached the fracture. She corrected it easily. Everyone went home for dinner."

**Fix Prompt:**
```
TONE/PACING CORRECTION

This chapter's tone is wrong for its purpose.

CURRENT TONE: [Calm/light/rushed/contemplative]
REQUIRED TONE: [Urgent/tense/intimate/desperate]

CURRENT PACING: [Too slow/too fast]
REQUIRED PACING: [Building tension/sustained pressure/rapid escalation]

SPECIFIC ADJUSTMENTS NEEDED:
- Increase urgency: [How - shorter sentences, time pressure, etc.]
- Deepen emotion: [Which emotions - fear, guilt, determination]
- Adjust rhythm: [Faster/slower, more/less description]

REWRITE matching the required tone and pacing.
```

---

## PROBLEM #8: Unclear About Chapter's Purpose

**Symptom:**
- Chapter wanders without clear focus
- Multiple competing threads, none developed
- Doesn't set up next chapter properly
- Doesn't build on previous chapter

**Fix Prompt:**
```
CHAPTER PURPOSE CLARIFICATION

This chapter lacks clear focus. Let me specify its role:

CHAPTER [X] PRIMARY PURPOSE:
[One clear sentence - e.g., "Establish that Caelen is planning to attempt imitation"]

CHAPTER [X] SECONDARY PURPOSES:
1. [Support goal - e.g., "Show Rachel can't explain her technique"]
2. [Support goal - e.g., "Position pieces for Chapter X+1 crisis"]

MUST CONNECT TO:
- Previous chapter: [What Chapter X-1 established]
- Next chapter: [What Chapter X+1 needs set up]

CHAPTER [X] SHOULD END WITH:
[Specific hook or tension point]

REWRITE focused clearly on these purposes.
```

---

## QUICK DIAGNOSTIC CHECKLIST

When you receive a chapter from ChatGPT, check:

❓ **Scale:** Is public/catastrophic actually public/catastrophic?
→ If NO: Use Problem #1 fix

❓ **Plot Beats:** Does it use content reserved for later chapters?
→ If YES: Use Problem #2 fix

❓ **Tension:** Does it resolve conflict or build it?
→ If RESOLVE: Use Problem #3 fix

❓ **Powers:** Are Rachel's abilities at correct progression level?
→ If NO: Use Problem #4 fix

❓ **Characters:** Do they sound like themselves?
→ If NO: Use Problem #5 fix

❓ **Completeness:** Are all outline beats included?
→ If NO: Use Problem #6 fix

❓ **Tone:** Does pacing/emotion match chapter's purpose?
→ If NO: Use Problem #7 fix

❓ **Focus:** Does chapter have clear purpose and connections?
→ If NO: Use Problem #8 fix

---

## NUCLEAR OPTION: START OVER

If ChatGPT is really not getting it, try this:

```
Let's start fresh on Chapter [X].

FORGET previous attempts. 

Read ONLY this outline section:
[Paste outline]

This chapter is:
- Position in arc: [Setup/building/climax]
- Scale: [Intimate/public/catastrophic]
- Primary beat: [One clear goal]
- Must NOT include: [List reserved items]

Write 2,500-3,500 words focused ONLY on what I've specified above.

Do not extrapolate. Do not compress. Do not jump ahead.

If you're uncertain about anything, ASK before writing.

Ready?
```

---

## PREVENTION IS BETTER THAN CURE

**Best Practices:**

1. ✅ **Start each chapter with verification checklist**
   - Forces ChatGPT to think before writing

2. ✅ **Paste outline section explicitly**
   - Don't rely on ChatGPT remembering

3. ✅ **List "Do Not Include" items**
   - Explicitly prevents jumping ahead

4. ✅ **Specify scale in concrete terms**
   - "50+ witnesses, three buildings threatened" not "big crisis"

5. ✅ **Give word count targets for scenes**
   - "Crisis sequence should be 800-1000 words" prevents rushing

6. ✅ **End each chapter request with: "If uncertain about anything, ask first"**
   - Encourages clarification over guessing

7. ✅ **Review first 500 words before letting it continue**
   - Catch problems early

---

## RED FLAGS THAT MEAN "STOP IMMEDIATELY"

If you see any of these in the draft, STOP and revise:

🚨 "Rachel saw her mother cross into the structured realm..."
🚨 "The seal opened, revealing..."
🚨 "The Council decided unanimously..."
🚨 "Caelen tried the technique and it worked..."
🚨 "Rachel understood the seal was..."
🚨 "The small crisis was quickly resolved..."
🚨 "Everyone agreed she was safe..."
🚨 "The collapse threatened a single building..."
🚨 "Time seemed to slow" (when time dilation shouldn't be visible yet)
🚨 "Rachel's father appeared..."

Any of these = wrong chapter content.

---

## REMEMBER

ChatGPT wants to:
- ✗ Be helpful and give you cool content now
- ✗ Resolve tension for satisfying reading
- ✗ Show off world-building and revelations
- ✗ Keep scenes intimate and character-focused

You need it to:
- ✓ Follow the outline's pacing strictly
- ✓ Build tension sustainably
- ✓ Save reveals for designated chapters
- ✓ Match each scene's required scale

**Your prompts must explicitly fight ChatGPT's helpful instincts.**

Be more specific than feels necessary. It works.

