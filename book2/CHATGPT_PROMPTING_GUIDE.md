# How to Prompt ChatGPT to Follow the Outline

## THE CORE PROBLEM

ChatGPT tends to:
- ❌ Compress plot beats (make big public scenes into small private ones)
- ❌ Jump ahead to later reveals too early
- ❌ "Spend" major plot points on minor moments
- ❌ Ignore the outline's specific chapter assignments
- ❌ Resolve tension too quickly instead of building it

## THE SOLUTION: STRUCTURED PROMPTING

---

## MASTER PROMPT TEMPLATE (Use this EVERY time)

```
I'm writing Chapter [NUMBER] of Book 2 for my isekai series.

BEFORE YOU WRITE ANYTHING:

1. Read the outline section for Chapter [NUMBER] in the attached scaffolding document
2. Identify what this chapter is SUPPOSED to accomplish according to the outline
3. Check the "Do Not Use Yet" list to make sure you're not using plot elements reserved for later chapters
4. Confirm you understand the difference between THIS chapter's role and similar-seeming plot beats that come later

OUTLINE REQUIREMENTS FOR CHAPTER [NUMBER]:
[Paste the specific section from the outline here]

CRITICAL CONSTRAINTS:
- Do NOT jump ahead to plot beats scheduled for later chapters
- Do NOT make public/catastrophic events into private/small ones
- Do NOT reveal cosmological information reserved for Act IV
- Do NOT resolve major tensions quickly - let them build
- Do NOT compress multiple chapters' worth of content into one

RESERVED FOR LATER (DO NOT USE):
- Angel realm reveals/crossing visions (Act IV, Ch 40-42)
- Major imitator crisis with town-threatening collapse (Ch 21-22, PUBLIC)
- Vex dream inversion climax (Ch 35)
- Seal aperture opening (Ch 41)
- Meeting Rachel's father (Ch 43)
- [Add other specific things from outline]

WHAT THIS CHAPTER SHOULD INCLUDE:
[List 3-5 specific beats from the outline]

WHAT THIS CHAPTER SHOULD NOT INCLUDE:
[List 3-5 things that belong in later chapters]

TONE/SCALE:
[Specify: intimate/public, small/catastrophic, building/climax, etc.]

CHAPTER LENGTH TARGET: 2,500-3,500 words

Now write Chapter [NUMBER] following ONLY what the outline specifies for this chapter.
```

---

## EXAMPLE: PROPER PROMPT FOR CHAPTER 21

```
I'm writing Chapter 21 of Book 2 for my isekai series.

BEFORE YOU WRITE ANYTHING:

1. Read the outline section for Chapters 21-22 in the scaffolding document
2. This is the SETUP chapter for the major imitator crisis
3. Chapter 22 will be the catastrophic failure - don't do that yet
4. This chapter establishes stakes and positioning before the crisis

OUTLINE REQUIREMENTS FOR CHAPTER 21:
From the scaffolding outline:
"Young Imitator Incident (Chapters 21-22) **MAJOR EVENT**

Setup (Chapter 21):
- Young walker inspired by Rachel asks to train with her
- Rachel hesitant but Sivara allows supervised observation
- Walker watches Rachel work, takes notes
- Tries privately to mimic her technique"

CRITICAL CONSTRAINTS:
- This is SETUP only - the catastrophic failure happens in Chapter 22
- Do NOT have the attempt fail yet
- Do NOT make this private and small - position it for public crisis
- Caelen has been watching since Chapter 12 - reference that history
- The delegation observers should still be present or recently departed
- Build tension about imitation without releasing it yet

RESERVED FOR LATER (DO NOT USE IN THIS CHAPTER):
- The catastrophic public failure (that's Chapter 22)
- Time dilation visible to everyone (Chapter 22)
- Town-threatening collapse (Chapter 22)
- Major injury to the young walker (Chapter 22)
- Political fallout and town meeting (Chapters 23-24)

WHAT THIS CHAPTER SHOULD INCLUDE:
1. Caelen (or another young walker) asks Rachel directly about learning her technique
2. Rachel admits she can't explain it, which frustrates him
3. Sivara allows supervised observation (establishing she gave permission)
4. Walker studies Rachel's work intensely, takes detailed notes
5. Maybe attempts something very small and controlled with mixed results
6. End with him planning to try something bigger
7. Sense of inevitability building

WHAT THIS CHAPTER SHOULD NOT INCLUDE:
- The actual catastrophic attempt (next chapter)
- Public crisis (next chapter)
- Anyone getting seriously hurt (next chapter)
- Full political fallout (chapters 23-24)

TONE/SCALE:
- Intimate but with tension building toward public
- Quiet scenes with undercurrent of danger
- End with "calm before storm" feeling
- Reader should sense disaster approaching but not see it yet

CHAPTER LENGTH TARGET: 2,500-3,500 words

Now write Chapter 21 as SETUP ONLY, following exactly what the outline specifies.
```

---

## VERIFICATION CHECKLIST (Give this to ChatGPT)

Before ChatGPT writes anything, have it respond with:

```
OUTLINE VERIFICATION CHECKLIST:

□ I have read the outline section for Chapter [X]
□ I understand this chapter's specific purpose in the overall arc
□ I have identified which plot beats belong HERE vs. later chapters
□ I have checked the "Reserved for Later" list
□ I understand the scale (intimate/public, small/catastrophic)
□ I know what should NOT appear in this chapter
□ I understand this chapter's relationship to surrounding chapters

CHAPTER [X] SHOULD ACCOMPLISH:
1. [List specific beats from outline]
2.
3.

CHAPTER [X] SHOULD NOT INCLUDE:
1. [List reserved plot points]
2.
3.

SCALE: [intimate/public/mixed]
TENSION LEVEL: [building/sustaining/climaxing]
KEY SCENE TYPE: [character moment/action/revelation/etc.]

Proceed? (Wait for your confirmation before writing)
```

---

## SPECIFIC ANTI-PATTERNS TO PREVENT

### Problem: Compressing Big Scenes into Small Ones

**Bad ChatGPT instinct:**
> "Caelen tries Rachel's technique alone in the orchard. Minor compression. Rachel helps him correct it. They talk."

**Your prompt should specify:**
```
SCALE REQUIREMENT:
This is a MAJOR CATASTROPHIC EVENT, not a small private moment.
- Multiple buildings threatened
- Dozens of witnesses present
- Collapse spreading rapidly
- Traditional methods failing publicly
- Life-threatening danger
- Rachel forced to reveal FULL abilities
- Aftermath affects entire community

If your draft can be summarized as "small private correction," you've made it too small.
```

### Problem: Using Later Plot Beats Too Early

**Bad ChatGPT instinct:**
> "Rachel has a vision of her mother crossing into the angel realm. She sees the structured space, the geometric patterns..."

**Your prompt should specify:**
```
COSMOLOGICAL REVEALS - OFF LIMITS:
- Direct views of angel realm (reserved for Chapter 41-42)
- Crossing visions showing the other side (Act IV only)
- Seal aperture opening (Chapter 41)
- Meeting family from angel realm (Chapter 43)
- Understanding seal's full purpose (Act IV)

THIS CHAPTER CAN INCLUDE:
- Hints, distant resonance, unclear sensations
- References to Theryn's past without showing it
- Growing awareness something is watching
- Mystery building, not resolving

If you're explaining cosmology, you've gone too far.
```

### Problem: Resolving Tension Too Fast

**Bad ChatGPT instinct:**
> "The Council observers discuss Rachel's abilities and conclude she's an asset. They recommend continued autonomy. Everyone relaxes."

**Your prompt should specify:**
```
TENSION MANAGEMENT:
This is Act II - pressure should be BUILDING, not resolving.

- Questions should outnumber answers
- New concerns should emerge
- Decisions should create new problems
- Characters should be uncertain
- Multiple forces should want different things
- No clean resolutions until Act IV

If everyone agrees on a path forward, you've resolved too much.
```

---

## CHAPTER-BY-CHAPTER PROMPT FRAGMENTS

### For Power Growth Chapters (15, 16, 18)
```
POWER PROGRESSION NOTE:
Show incremental growth, not sudden jumps:
- Chapter 15: Senses before manifestation (new)
- Chapter 16: Distance correction (70 paces)
- Chapter 18: Seal resonance hints (distant awareness)

This chapter shows [SPECIFIC ABILITY] emerging.
Do NOT show abilities from later chapters.
Do NOT explain the mechanism completely.
Show the growth, show reactions, build mystery.
```

### For Dream Sequence Chapters (17, 33, 35)
```
VEX ENCOUNTER PROGRESSION:
- Phase 1 (Ch 4): Observational, testing edges [COMPLETE]
- Phase 2 (Ch 17): Aggressive, probing relationships [THIS CHAPTER]
- Phase 3 (Ch 33): Direct assault, pre-inversion
- Phase 4 (Ch 35): Full inversion climax [RESERVED]

This is encounter #[X] of 4 total.
Vex should be [more/less] aggressive than last time.
Rachel should show [slightly more/same/much more] ability to resist.
Do NOT do the full inversion yet - that's Chapter 35.
```

### For Creature Encounter Chapters (6-7, 19-20, 31-32)
```
CREATURE ENCOUNTER PROGRESSION:
- First (Ch 6-7): Single entity, basic communication [COMPLETE]
- Second (Ch 19-20): Multiple coordinated, systematic testing [THIS CHAPTER]
- Third (Ch 31-32): More aggressive, "you are called" message

This is encounter #[X] of 3.
Creatures should be more [organized/aggressive/intelligent] than last time.
Show increasing coordination and purpose.
They're gathering data, not attacking randomly.
```

---

## RED FLAGS TO WATCH FOR

If ChatGPT's draft includes any of these, STOP and revise:

### 🚨 RED FLAG: "Rachel sees her mother crossing..."
**Why it's wrong:** Theryn crossing visions reserved for Act IV
**Fix:** Remove the vision, replace with hint/sensation only

### 🚨 RED FLAG: "The small compression was easily corrected..."
**Why it's wrong:** Major crisis beats should be CATASTROPHIC not small
**Fix:** Specify scale explicitly in prompt - "threatens multiple buildings"

### 🚨 RED FLAG: "The Council decides..."
**Why it's wrong:** Resolving political tension too quickly
**Fix:** Councils should deliberate slowly, create new complications

### 🚨 RED FLAG: "Rachel understood the seal was..."
**Why it's wrong:** Cosmological explanations belong in Act IV
**Fix:** Keep understanding vague, mysterious, incomplete

### 🚨 RED FLAG: "Caelen tried and succeeded..."
**Why it's wrong:** Imitation attempts should fail (except minor ones)
**Fix:** Distinguish small attempts from major catastrophic one

---

## PROMPT TEMPLATE FOR REVISIONS

When ChatGPT gets it wrong:

```
This chapter has problems. Let me specify what went wrong:

PROBLEMS IDENTIFIED:
1. [Specific issue - e.g., "Made the crisis too small and private"]
2. [Specific issue - e.g., "Used a plot beat from Chapter 35"]
3. [Specific issue - e.g., "Resolved tension instead of building it"]

WHAT THE OUTLINE ACTUALLY REQUIRES:
[Paste relevant section]

SCALE CORRECTION NEEDED:
[Specify if something needs to be bigger/smaller/more public/more private]

PLOT BEAT CORRECTION NEEDED:
[Specify what needs to be saved for later]

TENSION CORRECTION NEEDED:
[Specify how uncertainty/pressure should build instead of resolve]

Please rewrite Chapter [X] following the outline correctly this time.
```

---

## FINAL CHECKLIST FOR YOU

Before accepting a chapter from ChatGPT, verify:

✅ Does it match the outline's description for this chapter number?
✅ Is the scale appropriate (public vs private, big vs small)?
✅ Does it build tension rather than resolve it?
✅ Are later plot beats still preserved for their proper chapters?
✅ Are cosmological reveals saved for Act IV?
✅ Does it feel like the right pacing position in the act?
✅ Are character reactions realistic and varied?
✅ Does it leave hooks for the next chapter?

If any answer is NO, revise with specific corrections.

---

## SAMPLE OPENING MESSAGE TO CHATGPT

```
I'm working on Book 2 of my isekai series. I have a detailed scaffolding outline that specifies what should happen in each chapter and which plot beats are reserved for later.

I need you to help me write chapters that STRICTLY follow this outline. 

COMMON PROBLEMS TO AVOID:
- Making big public scenes into small private ones
- Using plot beats from later chapters too early
- Resolving tension instead of building it
- Revealing cosmological information before Act IV

I will provide you with:
1. The outline section for the specific chapter
2. A list of what should NOT appear yet
3. Scale and tone specifications
4. Context from previous chapters

For each chapter, please:
1. Read the outline requirements carefully
2. Confirm your understanding before writing
3. Verify you're not using reserved plot beats
4. Write ONLY what the outline specifies for that chapter

Ready? I'll start with Chapter [X].
```

---

## TL;DR - THE ESSENTIAL STRATEGY

1. **Always specify the chapter number explicitly**
2. **Paste the relevant outline section directly into the prompt**
3. **List what should NOT appear yet (reserved for later)**
4. **Specify scale explicitly (public/private, small/catastrophic)**
5. **Make ChatGPT confirm understanding before writing**
6. **Use the verification checklist**
7. **Stop and revise immediately if red flags appear**

The key is **being more specific than you think you need to be**. ChatGPT's instinct is to compress and resolve. Your prompts must fight that instinct explicitly.

