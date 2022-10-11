# Yet Another Parser (for Neurobridge)
#
# Designed to take the plain text files from Ray and clean them up and regularize them.
#
# Specifically: normalize junk whitespace, convert to one sentence per line, regularize
# punctuation, and so on. It should provide both a plain text (1 sentence per line, 1SPL)
# output and also various parsings.
#
# MDT
# 2022.10.06

import io
from pprint import pprint
import nltk

# temp test text

testblock = """Abnormal Frontostriatal Activity During Unexpected Reward Receipt in Depression and Schizophrenia: Relationship to Anhedonia
Alterations in reward processes may underlie motivational and anhedonic symptoms in depression and schizophrenia. However it remains unclear whether these alterations are disorder-specific or shared, and whether they clearly relate to symptom generation or not. We studied brain responses to unexpected rewards during a simulated slot-machine game in 24 patients with depression, 21 patients with schizophrenia, and 21 healthy controls using functional magnetic resonance imaging. We investigated relationships between brain activation, task-related motivation, and questionnaire rated anhedonia. There was reduced activation in the orbitofrontal cortex, ventral striatum, inferior temporal gyrus, and occipital cortex in both depression and schizophrenia in comparison with healthy participants during receipt of unexpected reward. In the medial prefrontal cortex both patient groups showed reduced activation, with activation significantly more abnormal in schizophrenia than depression. Anterior cingulate and medial frontal cortical activation predicted task-related motivation, which in turn predicted anhedonia severity in schizophrenia. Our findings provide evidence for overlapping hypofunction in ventral striatal and orbitofrontal regions in depression and schizophrenia during unexpected reward receipt, and for a relationship between unexpected reward processing in the medial prefrontal cortex and the generation of motivational states.
Introduction
Depression and schizophrenia are associated with deficits in motivation and enjoyment, which have been collectively termed anhedonia by some authors. Clinically it is challenging to distinguish between deficits in pleasure and motivation, even though there are at least partially separable processes that underpin these functions. Some evidence suggests that striatal hypofunction during reward processing is present in schizophrenia and depression, and may contribute to the motivational and hedonic problems experienced by patients, whilst other authors have emphasized the importance of orbitofrontal cortex function in this regard. It remains unknown whether the neurobiological disturbances in reward processing are different in schizophrenia and depression and it is not yet clear which aspects of reward processing are particularly problematic in these conditions, or whether any associated neural deficits are predominantly cortical or subcortical in origin. Insights into any shared pathophysiology underlying abnormalities in motivation and pleasure across different psychiatric diagnoses could lead to improved use of existing treatments, facilitate development of new treatments and, as is postulated by the Research Domain Criteria (RDoC) project, may contribute to improved psychiatric classification in the future.
Recently it has been suggested that in both schizophrenia and depression, the aspects of reward processing that relate to reward receipt may be relatively spared, whereas anticipatory and motivational aspects of reward processing may be more dysfunctional and may be closely linked to negative symptoms/depression. However, the majority of neuroimaging studies that have examined reward receipt in schizophrenia and depression have used tasks where rewards are rather predictable, and can be expected to occur more often than not; several studies using such tasks have found broadly intact neural responses to reward feedback in schizophrenia and depression (eg,). Such tasks are optimized to examine brain responses during the anticipation and receipt of a highly expected reward, rather than unexpected reward responses; several studies have documented robust striatal and cortical deficits in schizophrenia and depression in the anticipation of reward.
This still leaves open the question as to whether response to reward receipt, especially unexpected reward receipt, is normal in these disorders. In this regard it is critical to examine neural responses to unpredicted rewards, which may be more pronounced than those to predicted rewards. This is of particular interest, given that unexpected events evoke prediction errors, which are encoded within the brain at both cortical and subcortical levels. Prediction error signaling has been postulated to relate to many aspects of thought and behavior in health and in psychiatric illness, including learning, motivation, and attention, and abnormal brain prediction error signaling may contribute to psychotic symptoms as well as deficits in motivation and enjoyment.
Initial evidence suggests that the prediction error signaling during, or after, learning may be compromised in both schizophrenia and depression in cortical and subcortical regions (; although see). However, abnormal neural correlates of prediction error associated learning signals may reflect dysfunction of the learning mechanism (eg, failure to update in response to prediction error signals during learning), not necessarily to the prediction error signaling mechanism per se. To fully assess the integrity of neural systems that signal surprising/unexpected rewards, it is critical to employ an experimental scenario with little or no learning component in which reward outcome is unpredictable.
to test whether brain responses to unexpected rewards were broadly intact in schizophrenia and depression,
if brain responses to unexpected rewards are abnormal in schizophrenia and depression, to evaluate if the deficits are confined to cortical, or subcortical regions, and whether there are any shared or differential areas of deficit in the two disorders, and
to examine whether brain responses to unexpected reward receipt are related to motivation and enjoyment in these disorders.
Our aim therefore was to explore brain responses to unexpected reward delivery in both depression and schizophrenia, and their relationship to motivation and enjoyment. We used an fMRI reward processing task involving the receipt of unexpected rewards, but minimal learning, with a sample of patients who all subjectively endorsed at least some degree of anhedonia. Our goals were:
Materials and methods
Participants
The study was approved by the Cambridgeshire 3 National Health Service research ethics committee. Written informed consent was obtained from all participants.
Twenty-one people with DSM-IV schizophrenia, 24 people with DSM-IV major depressive disorder (MDD), and 21 healthy volunteers took part in the study (Table 1). All schizophrenia participants were taking antipsychotic medication; eight were additionally taking antidepressant medication. Thirteen of the 24 depression participants were taking antidepressant medication, of whom four were additionally taking antipsychotic medication; medication is described in Table 1 and in further detail in Supplementary Material. Inclusion criteria were an age between 18 and 65 and adequate proficiency in English. Exclusion criteria were history of neurological disorder, physical illness, dependence on alcohol or recreational drugs, and any contraindication for MRI scanning. A first-degree family history of schizophrenia or bipolar disorder was an additional exclusion criterion in the depression and control groups. All participants with depression or schizophrenia subjectively endorsed a degree of loss of interest or pleasure.
Anhedonia Assessment
To assess anhedonia we used the Snaith Hamilton Pleasure Scale (SHAPS), a validated self-report measure.
fMRI Task Description
The task involved playing a computerized version of a slot-machine game; participants view two reels of a slot-machine/one arm bandit game, where the left hand reel is stationary and the right hand reel spins until it stops (Figure 1). If the two icons in the center of view match, there is a financial reward of 50 pence. Participants win on an average one in six trials, making rewards unexpected in this game. Furthermore, the duration of the spinning of the wheel is variable in this task (delay varies between 2.8 and 6 s), so the precise timing of the outcome is also not predictable. The game consisted of two runs of 60 trials, each run lasting ~20 min, and has been previously described. On 50% of trials, the participant selects the ‘play icon'—the image in the center of the left hand reel—by rotating the reel to the icon of their choice. In the other 50% of trials (pseudorandomised distribution), the computer selects the ‘play icon' on these trials the participant is required to confirm with a button press that he/she has noted the computer choice. After this selection phase the right hand reel starts to spin. The selection phase lasts 5 s, followed by a variable delay stage whilst the second reel spins and comes to a stop, followed by an outcome phase of 4 s where the reward is presented: ‘£0.50 win!' (if the icons on the payline of the two reels match) or ‘No win' (if they do not match). If selection/confirmation did not occur within 5 s, ‘too late' was presented on the screen and the task moved on to the next trial. At the end of each trial, there was a variable inter-trial interval of between 2 and 7 s duration. Participants were told that they would be given any money they won at the end of the experiment.
Task-related pleasure and motivation
Immediately after the scan session the participants answered the questions, ‘When the second picture matched the chosen picture you won money. How much did you like the feeling of winning money?' and, ‘When the second picture matched the chosen picture you won money. Did this make you want to play more?' The answers were marked on a visual analog scale.
fMRI Data Acquisition and Pre-Processing
A Siemens Trio Tim operating at 3T was used to collect imaging data. Gradient-echo T2*-weighted echo planar images depicting BOLD contrast were acquired from 32 noncontiguous oblique axial planes to minimize signal drop-out in ventral regions. TR=2 s; echo time=30 ms; flip angle=78; voxel size=3.14 × 3.14 × 3.75 mm3, matrix size 64 × 64; bandwidth 2232 HZ/Px. A high-resolution T1-weighted three-dimensional MP-RAGE structural image was also acquired for use in spatial normalization of the EPI series. Imaging data was analyzed using FSL software (FMRIB's Software Library, www.fmrib.ox.ac.uk/fsl). See Supplementary Material for pre-processing details.
fMRI Data Analysis
An event-related analysis in FSL software was used to identify neural responses at the time of the unexpected win. We used a single statistical linear regression model with four explanatory variables and their temporal derivatives: (a) anticipation phase (the duration of this event varied between 2.8 and 6 s on different trials); (b) win outcome (4 s duration, 20 events in total); (c) near-miss outcomes (4 s duration, 40 events in total); (d) full-miss outcomes (4 s duration, 60 events in total). A near-miss outcome is where the play icon finishes adjacent to, but not on, the payline; near-miss outcomes have been shown to evoke neural responses different to other misses. Movement parameters from the realignment step were also included in the first-level model.
As our hypotheses concerned brain activation in response to unexpected reward, an ‘unexpected reward receipt' contrast was investigated, formed by the contrast of win outcomes vs full-miss outcomes. This contrast was computed at the single-participant level and the β-parameters for participants from this contrast were carried forward to group analyses. One-way between participants ANOVA was conducted at the whole-brain level to compare between the three groups. The one-way ANOVA only identifies regions in which activation is different between groups, without indicating which groups drive the differences or the directionality of the differences. Therefore, for clusters in which the ANOVA indicated group differences we extracted the mean parameter estimates for each subject for that cluster (using the FSL tool Featquery) and conducted post hoc comparisons across groups. Regression analyses at the whole-brain level in FSL were used to investigate relationships between brain activation and the post-scan subjective ratings of motivation and pleasure.
Imaging comparisons were cluster thresholded using the FSL tool easythresh, using a family-wise error (FWE) correction at p<0.05 (initial cluster threshold z=2).
"""

# Open and read in a "Ray-type" file

# temp
# f = io.StringIO(testblock)

# Clean it

# Sentence parse it

nltk_sentences = nltk.sent_tokenize(testblock)

pprint(nltk_sentences)

print("\n", len(nltk_sentences), "\n")

for no, sent in enumerate(nltk_sentences):
    print(no, sent.replace("\n", " ... "))

# Parse parse it

# save in various formats

# coda
