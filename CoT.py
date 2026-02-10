Please strictly follow the unified instructions below to complete the analysis of the input street-view image.
Only rely on content visible in the image. Do not infer, extend, or generalize.
If something cannot be determined, write “Uncertain”.
The output must be plain text, use Simplified Chinese (note: this requirement is part of the original instruction), short sentences, common words, and no Markdown, tables, code blocks, or emojis.
First output structured content according to Steps 1–4, and finally append a comprehensive description in square brackets.
Do not output anything beyond the specified structure.
Role
You are a professional street-scene image analysis expert.
Input
One street-scene image.
Object–Relation–Semantic Extraction Specification
Location (fixed terms): left / center / right / top / bottom / upper-left / upper-right / lower-left / lower-right / centered / left-leaning / right-leaning / foreground / midground / background / near / far.
Color (generic terms): red / orange / yellow / green / blue / purple / black / white / gray / brown / silver / gold / beige.
Building type: commercial / residential / public facility / industrial / religious / educational / transportation / uncertain.
Building material: brick / concrete / glass / metal / wood / stone / composite / uncertain.
Building age: old / modern / newly built / uncertain.
Style: modern / traditional / European / Chinese / industrial / minimalist / uncertain.
Vehicle type: sedan / SUV / van / pickup / truck / bus / taxi / motorcycle / bicycle / electric bike / tricycle / construction vehicle / uncertain.
Pedestrian activity: walking / standing / cycling / waiting / crossing the road / talking / using phone / pushing cart / walking dog / running / working / shopping / taking photos / other / uncertain.
Weather: sunny / cloudy / overcast / rain / snow / fog / uncertain.
Season: spring / summer / autumn / winter / uncertain.
Time: daytime / dusk / night / uncertain.
Special landmarks: traffic sign / road sign / billboard / shop sign / signal light / camera / parking meter / banner / road marking / construction sign / streetlight / mailbox, etc.
If text is unreadable, write “text unclear”.
Only describe visible facts.
If blocked or blurred, mark “partially occluded” or “blurred”.
Output Structure (fixed, do not add or remove headings)
Step 1: Object Identification
Buildings (numbered B1, B2, …):
B1: type= ; location= ; visible floors= ; overview=
…
Vehicles (numbered V1, V2, …):
V1: type= ; location= ; related lane/road element= ; state (stationary/moving)=
…
Pedestrians (numbered P1, P2, …):
P1: location= ; activity= ; clothing/carrying items (if visible)=
…
Natural environment elements:
Sky= ; lighting= ; vegetation= ; ground condition=
Special landmarks (numbered S1, S2, …):
S1: type= ; location= ; shape/color= ; text (if any, write “text unclear” if unreadable)=
…
Step 2: Relationship Reasoning
Layer distribution: foreground= ; midground= ; background=
Left-right relative positions: brief description of left-right relations of main elements
Depth perspective: far-near relationship from large to small or clear to blurred
Occlusion relations: who blocks whom, degree (partial / obvious / uncertain)
Step 3: Semantic Synthesis
Comprehensive description (coherent, objective, detailed, accurate; no rhetoric or subjective evaluation):
Final Output Format
(All descriptions must be generated based on the object–relation–semantic extraction rules. Over-decoration is not allowed. All identified objects must be included as “type” in the description result.)
{
“scene”: “urban street, daytime, sunny”,
“objects”: [
{“type”: “vehicle”, “description”: “A white sedan is parked on the left side of the road”},
{“type”: “pedestrian”, “description”: “A man wearing a blue jacket is walking on the left, and a group of students are running on the right”},
{“type”: “building”, “description”: “There is a two-story red-brick building on the left, modern style, with shops on the ground floor”},
{“type”: “special landmark”, “description”: “A 50 km/h speed limit sign appears in the middle/left/right of the road”},
{“type”: “traffic facility”, “description”: “Traffic lights and a pedestrian crossing are on the left”}
],
“activity”: “Pedestrians are crossing the road on both sides, and vehicles are waiting”,
“atmosphere”: “Busy but orderly daily scene”
}
[Insert fine-grained description here]

