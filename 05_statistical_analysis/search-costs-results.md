---
title: "Search Costs Field Experiment"
date: "2025-06-06"
output:
  pdf_document:
    toc: true
    toc_depth: 3
    number_sections: true
    fig_caption: true
    keep_tex: true
    keep_md: true
header-includes:
  - \usepackage{booktabs}
  - \usepackage{longtable}
  - \usepackage{array}
  - \usepackage{multirow}
  - \usepackage{float}
  - \usepackage{pdflscape}
  - \newcommand{\blandscape}{\begin{landscape}}
  - \newcommand{\elandscape}{\end{landscape}}
  - \usepackage{caption}
  - \captionsetup[table]{position=below,skip=10pt}
  - \usepackage{dcolumn}
  - \usepackage{adjustbox}
  - \usepackage{tabularx}
  - \newcolumntype{C}[1]{>{\centering\arraybackslash}p{#1}}
---





\newpage

# Summary Statistics

## Overall Summary Statistics

### Seminar Speaker Demographics

\begin{table}[H]
\caption{Overall Seminar Statistics}
\label{tab:summary_seminars_basic}
\centering
\begin{tabular}{lr}
\toprule
Statistic & Value \\
\midrule
Number of seminars & 1654 \\
Number of unique departments & 528 \\
Total speakers across all seminars & 23069 \\
Mean speakers per seminar & 13.95 \\
SD speakers per seminar & 9.90 \\
Min speakers in a seminar & 1 \\
Max speakers in a seminar & 76 \\
\bottomrule
\end{tabular}
\end{table}

\begin{table}[H]
\caption{Seminar Speaker Demographics (Across All Seminars)}
\label{tab:summary_seminar_demographics}
\centering
\footnotesize
\begin{tabular}{lccccc}
\toprule
Demographic Group & Mean \% & SD \% & Mean Count & SD Count & Pct. Any \\
\midrule
URM & 7.44 & 11.09 & 1.00 & 1.28 & 54.2 \\
Black & 2.23 & 5.96 & 0.32 & 0.68 & 23.3 \\
Hispanic & 5.18 & 9.49 & 0.68 & 1.01 & 42.9 \\
Female & 16.99 & 16.25 & 2.39 & 2.48 & 75.9 \\
\bottomrule
\end{tabular}
\parbox{\linewidth}{\footnotesize Note: N =  1654  seminars. Percentages calculated among speakers with demographic data available. 'Pct. Any' indicates the percentage of seminars that have at least one speaker from that demographic group.}
\end{table}

### Department Faculty Demographics


\begin{table}[H]
\caption{Department Faculty Demographics}
\label{tab:summary_dept_faculty}
\centering
\begin{tabular}{lcc}
\toprule
Statistic & Mean & SD \\
\midrule
Total faculty per department & 34.0 & 18.1 \\
\% URM faculty & 4.09 & 4.40 \\
\% Women faculty & 20.40 & 7.58 \\
\bottomrule
\end{tabular}
\parbox{\linewidth}{\footnotesize Note: N =  528  unique departments. Department faculty demographics based on 2024 coding.}
\end{table}

## Summary Statistics by Discipline

### Seminar Speaker Demographics by Discipline


\begin{table}[H]
\caption{Seminar Statistics by Discipline}
\label{tab:summary_disc_basic}
\centering
\footnotesize
\begin{tabular}{lcccc}
\toprule
Discipline & N Seminars & N Depts & Mean Speakers & SD Speakers \\
\midrule
Chemistry & 270 & 122 & 14.5 & 10.9 \\
Computer Science & 142 & 82 & 13.1 & 10.3 \\
Mathematics & 811 & 134 & 13.2 & 9.1 \\
Mechanical Engineering & 81 & 65 & 13.0 & 10.2 \\
Physics & 350 & 125 & 15.8 & 10.4 \\
\bottomrule
\end{tabular}
\end{table}

\begin{table}[H]
\caption{Seminar Speaker Demographics by Discipline: URM}
\label{tab:summary_disc_urm}
\centering
\footnotesize
\begin{tabular}{lccccc}
\toprule
Discipline & N Seminars & Mean \% & SD \% & Mean Count & Pct. Has Any \\
\midrule
Chemistry & 270 & 8.88 & 10.52 & 1.27 & 64.1 \\
Computer Science & 142 & 4.48 & 8.21 & 0.54 & 36.6 \\
Mathematics & 811 & 7.11 & 10.72 & 0.94 & 50.4 \\
Mechanical Engineering & 81 & 8.20 & 9.17 & 1.12 & 61.7 \\
Physics & 350 & 8.11 & 13.33 & 1.12 & 60.6 \\
\bottomrule
\end{tabular}
\parbox{\linewidth}{\footnotesize Note: Statistics are for seminar speakers. 'Pct. Has Any' indicates percentage of seminars with at least one URM speaker.}
\end{table}

\begin{table}[H]
\caption{Seminar Speaker Demographics by Discipline: Other Groups}
\label{tab:summary_disc_other}
\centering
\footnotesize
\begin{tabular}{lcccccc}
\toprule
 & \multicolumn{2}{c}{Black} & \multicolumn{2}{c}{Hispanic} & \multicolumn{2}{c}{Female} \\
Discipline & Mean \% & Pct. Any & Mean \% & Pct. Any & Mean \% & Pct. Any \\
\midrule
Chemistry & 4.23 & 39.6 & 4.53 & 45.2 & 23.72 & 86.7 \\
Computer Science & 1.55 & 17.6 & 2.93 & 24.6 & 19.20 & 78.2 \\
Mathematics & 1.80 & 19.4 & 5.31 & 41.2 & 14.00 & 70.3 \\
Mechanical Engineering & 2.95 & 28.4 & 5.25 & 46.9 & 19.83 & 76.5 \\
Physics & 1.82 & 20.9 & 6.29 & 51.4 & 17.14 & 79.4 \\
\bottomrule
\end{tabular}
\parbox{\linewidth}{\footnotesize Note: Statistics are for seminar speakers. 'Pct. Any' indicates percentage of seminars with at least one speaker from that group.}
\end{table}

### Department Faculty Demographics by Discipline


\begin{table}[H]
\caption{Department Faculty Demographics by Discipline}
\label{tab:summary_disc_dept_faculty}
\centering
\footnotesize
\begin{tabular}{lccccccc}
\toprule
 & & \multicolumn{2}{c}{Faculty Size} & \multicolumn{2}{c}{\% URM Faculty} & \multicolumn{2}{c}{\% Women Faculty} \\
Discipline & N Depts & Mean & SD & Mean & SD & Mean & SD \\
\midrule
Chemistry & 122 & 28.6 & 11.9 & 4.76 & 4.47 & 24.40 & 7.18 \\
Computer Science & 82 & 43.5 & 25.0 & 2.79 & 3.27 & 20.12 & 7.28 \\
Mathematics & 134 & 33.9 & 16.2 & 3.63 & 3.54 & 19.82 & 7.67 \\
Mechanical Engineering & 65 & 36.4 & 19.1 & 5.57 & 5.48 & 19.70 & 7.61 \\
Physics & 125 & 32.0 & 16.4 & 4.03 & 4.90 & 17.64 & 6.52 \\
\bottomrule
\end{tabular}
\parbox{\linewidth}{\footnotesize Note: Department faculty demographics based on 2024 coding.}
\end{table}

## Summary Statistics by Semester


\begin{table}[H]
\caption{Summary Statistics by Semester}
\label{tab:summary_semester}
\centering
\footnotesize
\begin{tabular}{lccccccc}
\toprule
 & \multicolumn{3}{c}{URM} & \multicolumn{2}{c}{Black} & \multicolumn{2}{c}{Hispanic} \\
Semester (N) & Mean \% & Mean Count & Pct. Any & Mean \% & Pct. Any & Mean \% & Pct. Any \\
\midrule
Fall (1448) & 7.08 & 0.53 & 36.3 & 1.73 & 11.7 & 5.33 & 28.9 \\
Spring (1385) & 7.56 & 0.64 & 41.9 & 2.69 & 18.4 & 4.84 & 29.9 \\
\midrule
 & \multicolumn{3}{c}{Female} & \multicolumn{2}{c}{Total Speakers} & & \\
Semester & Mean \% & Mean Count & Pct. Any & Mean & SD & & \\
\midrule
Fall & 16.16 & 1.27 & 62.0 & 7.75 & 5.50 & & \\
Spring & 17.75 & 1.52 & 64.5 & 8.56 & 6.87 & & \\
\bottomrule
\end{tabular}
\end{table}

\newpage

# Main Effects Analysis

## Main Question 1: URM Speaker Representation

\begin{table}[H]
\caption{Main Question 1: Effect on URM Speaker Representation}
\label{tab:mq1_urm}
\centering
\scriptsize
\begin{tabularx}{\textwidth}{l*{6}{>{\centering\arraybackslash}X}}
\toprule
 & \% URM & \% URM & Count URM & Count URM & Any URM & Any URM \\
 &  (1) & (2) & (3) & (4) & (5) & (6)  \\
\midrule
Treatment  &  0.664$^{}$ & 0.633$^{}$ & 0.087$^{}$ & 0.059$^{}$ & 0.017$^{}$ & 0.008$^{}$  \\
 &  (0.520) & (0.517) & (0.066) & (0.065) & (0.025) & (0.024)  \\
Constant  &  8.446$^{***}$ & 4.001$^{+}$ & 1.163$^{***}$ & 0.248$^{}$ & 0.589$^{***}$ & 0.219$^{+}$  \\
 &  (1.633) & (2.098) & (0.172) & (0.285) & (0.072) & (0.117)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,654 & 1,654 & 1,654 & 1,654 & 1,654 & 1,654  \\
Adjusted $R^2$ &  0.010 & 0.015 & 0.029 & 0.037 & 0.025 & 0.039  \\
\bottomrule
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize \vspace{2pt}Clustered standard errors at department level in parentheses.}}\\
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize $^{+}p<0.1$; $^{*}p<0.05$; $^{**}p<0.01$; $^{***}p<0.001$\vspace{2pt}}}\\
\end{tabularx}
\end{table}

\newpage

## Main Questions 2a-2c: Effects on Speaker Counts

\begin{table}[H]
\caption{Main Questions 2a-2c: Effects on Speaker Counts}
\label{tab:mq2_all}
\centering
\scriptsize
\begin{tabularx}{\textwidth}{l*{6}{>{\centering\arraybackslash}X}}
\toprule
 & \% Count & \% Count & Count Count & Count Count & Any Count & Any Count \\
 &  (1) & (2) & (3) & (4) & (5) & (6)  \\
\midrule
Treatment  &  -0.488$^{}$ & -0.483$^{}$ & 0.087$^{}$ & 0.059$^{}$ & -0.574$^{}$ & -0.542$^{}$  \\
 &  (0.553) & (0.545) & (0.066) & (0.065) & (0.526) & (0.519)  \\
Constant  &  16.744$^{***}$ & 13.098$^{***}$ & 1.163$^{***}$ & 0.248$^{}$ & 15.580$^{***}$ & 12.850$^{***}$  \\
 &  (1.311) & (2.440) & (0.172) & (0.285) & (1.243) & (2.301)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,654 & 1,654 & 1,654 & 1,654 & 1,654 & 1,654  \\
Adjusted $R^2$ &  0.033 & 0.057 & 0.029 & 0.037 & 0.032 & 0.058  \\
\bottomrule
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize \vspace{2pt}Clustered standard errors at department level in parentheses.}}\\
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize $^{+}p<0.1$; $^{*}p<0.05$; $^{**}p<0.01$; $^{***}p<0.001$\vspace{2pt}}}\\
\end{tabularx}
\end{table}

## Seemingly Unrelated Regression (SUR) Analysis


\begin{table}[H]
\caption{SUR Analysis: Testing Substitution Between URM and Non-URM Speakers}
\label{tab:sur_analysis}
\centering
\begin{tabular}{lcc}
\toprule
Outcome & Coefficient & SE \\
\midrule
URM Speakers & 0.0866 & (0.0631) \\
Non-URM Speakers & -0.5742 & (0.4594) \\
\midrule
Sum of Effects & -0.4876 & --- \\
\midrule
\multicolumn{3}{l}{\textit{Wald Test: H0: Treatment effect on URM + Treatment effect on Non-URM = 0}} \\
\bottomrule
\end{tabular}
\parbox{\linewidth}{\footnotesize Note: SUR estimation with simple controls allows for correlation between equation errors. The Wald test examines whether the treatment effect represents a pure substitution (increasing URM speakers while decreasing non-URM speakers by the same amount).}
\end{table}

\newpage

# Demographic Subgroup Analysis

## Black Speakers

\begin{table}[H]
\caption{Effect on Black Speakers}
\label{tab:black}
\centering
\scriptsize
\begin{tabularx}{\textwidth}{l*{6}{>{\centering\arraybackslash}X}}
\toprule
 & \% Black & \% Black & Count Black & Count Black & Any Black & Any Black \\
 &  (1) & (2) & (3) & (4) & (5) & (6)  \\
\midrule
Treatment  &  0.679$^{*}$ & 0.664$^{*}$ & 0.083$^{*}$ & 0.081$^{*}$ & 0.055$^{*}$ & 0.054$^{*}$  \\
 &  (0.309) & (0.294) & (0.039) & (0.038) & (0.023) & (0.022)  \\
Constant  &  2.707$^{***}$ & 0.933$^{}$ & 0.430$^{***}$ & 0.103$^{}$ & 0.289$^{***}$ & 0.051$^{}$  \\
 &  (0.791) & (1.301) & (0.103) & (0.167) & (0.061) & (0.104)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,654 & 1,654 & 1,654 & 1,654 & 1,654 & 1,654  \\
Adjusted $R^2$ &  0.026 & 0.031 & 0.048 & 0.057 & 0.036 & 0.044  \\
\bottomrule
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize \vspace{2pt}Clustered standard errors at department level in parentheses.}}\\
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize $^{+}p<0.1$; $^{*}p<0.05$; $^{**}p<0.01$; $^{***}p<0.001$\vspace{2pt}}}\\
\end{tabularx}
\end{table}

## Hispanic Speakers

\begin{table}[H]
\caption{Effect on Hispanic Speakers}
\label{tab:hispanic}
\centering
\scriptsize
\begin{tabularx}{\textwidth}{l*{6}{>{\centering\arraybackslash}X}}
\toprule
 & \% Hispanic & \% Hispanic & Count Hispanic & Count Hispanic & Any Hispanic & Any Hispanic \\
 &  (1) & (2) & (3) & (4) & (5) & (6)  \\
\midrule
Treatment  &  -0.001$^{}$ & -0.025$^{}$ & 0.004$^{}$ & -0.024$^{}$ & -0.020$^{}$ & -0.032$^{}$  \\
 &  (0.457) & (0.471) & (0.050) & (0.049) & (0.025) & (0.025)  \\
Constant  &  5.526$^{***}$ & 2.851$^{}$ & 0.707$^{***}$ & 0.109$^{}$ & 0.443$^{***}$ & 0.164$^{}$  \\
 &  (1.524) & (1.905) & (0.149) & (0.230) & (0.076) & (0.111)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,654 & 1,654 & 1,654 & 1,654 & 1,654 & 1,654  \\
Adjusted $R^2$ &  0.006 & 0.006 & 0.015 & 0.022 & 0.018 & 0.024  \\
\bottomrule
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize \vspace{2pt}Clustered standard errors at department level in parentheses.}}\\
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize $^{+}p<0.1$; $^{*}p<0.05$; $^{**}p<0.01$; $^{***}p<0.001$\vspace{2pt}}}\\
\end{tabularx}
\end{table}

## Female Speakers

\begin{table}[H]
\caption{Effect on Female Speakers}
\label{tab:female}
\centering
\scriptsize
\begin{tabularx}{\textwidth}{l*{6}{>{\centering\arraybackslash}X}}
\toprule
 & \% Female & \% Female & Count Female & Count Female & Any Female & Any Female \\
 &  (1) & (2) & (3) & (4) & (5) & (6)  \\
\midrule
Treatment  &  0.354$^{}$ & -0.117$^{}$ & -0.061$^{}$ & -0.130$^{}$ & 0.001$^{}$ & -0.003$^{}$  \\
 &  (0.840) & (0.833) & (0.129) & (0.128) & (0.022) & (0.021)  \\
Constant  &  21.904$^{***}$ & 13.802$^{***}$ & 3.602$^{***}$ & 2.169$^{***}$ & 0.870$^{***}$ & 0.682$^{***}$  \\
 &  (2.114) & (4.028) & (0.356) & (0.599) & (0.063) & (0.099)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,654 & 1,654 & 1,654 & 1,654 & 1,654 & 1,654  \\
Adjusted $R^2$ &  0.051 & 0.058 & 0.085 & 0.101 & 0.017 & 0.028  \\
\bottomrule
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize \vspace{2pt}Clustered standard errors at department level in parentheses.}}\\
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize $^{+}p<0.1$; $^{*}p<0.05$; $^{**}p<0.01$; $^{***}p<0.001$\vspace{2pt}}}\\
\end{tabularx}
\end{table}

## URM Female

\begin{table}[H]
\caption{Effect on URM Female Speakers}
\label{tab:urm_female}
\centering
\scriptsize
\begin{tabularx}{\textwidth}{l*{6}{>{\centering\arraybackslash}X}}
\toprule
 & \% URM Female & \% URM Female & Count URM Female & Count URM Female & Any URM Female & Any URM Female \\
 &  (1) & (2) & (3) & (4) & (5) & (6)  \\
\midrule
Treatment  &  0.011$^{}$ & -0.047$^{}$ & 0.022$^{}$ & 0.014$^{}$ & 0.015$^{}$ & 0.008$^{}$  \\
 &  (0.171) & (0.182) & (0.019) & (0.019) & (0.016) & (0.017)  \\
Constant  &  1.815$^{**}$ & -0.072$^{}$ & 0.207$^{***}$ & -0.002$^{}$ & 0.177$^{***}$ & -0.013$^{}$  \\
 &  (0.604) & (0.582) & (0.060) & (0.091) & (0.049) & (0.078)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,654 & 1,654 & 1,654 & 1,654 & 1,654 & 1,654  \\
Adjusted $R^2$ &  0.014 & 0.018 & 0.041 & 0.051 & 0.041 & 0.050  \\
\bottomrule
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize \vspace{2pt}Clustered standard errors at department level in parentheses.}}\\
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize $^{+}p<0.1$; $^{*}p<0.05$; $^{**}p<0.01$; $^{***}p<0.001$\vspace{2pt}}}\\
\end{tabularx}
\end{table}

## Black Female

\begin{table}[H]
\caption{Effect on Black Female Speakers}
\label{tab:black_female}
\centering
\scriptsize
\begin{tabularx}{\textwidth}{l*{6}{>{\centering\arraybackslash}X}}
\toprule
 & \% Black Female & \% Black Female & Count Black Female & Count Black Female & Any Black Female & Any Black Female \\
 &  (1) & (2) & (3) & (4) & (5) & (6)  \\
\midrule
Treatment  &  0.141$^{*}$ & 0.150$^{*}$ & 0.012$^{}$ & 0.013$^{}$ & 0.014$^{+}$ & 0.015$^{+}$  \\
 &  (0.069) & (0.072) & (0.009) & (0.009) & (0.008) & (0.008)  \\
Constant  &  0.493$^{**}$ & 0.063$^{}$ & 0.056$^{*}$ & 0.003$^{}$ & 0.044$^{*}$ & 0.003$^{}$  \\
 &  (0.153) & (0.272) & (0.024) & (0.042) & (0.020) & (0.036)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,654 & 1,654 & 1,654 & 1,654 & 1,654 & 1,654  \\
Adjusted $R^2$ &  0.032 & 0.036 & 0.024 & 0.029 & 0.020 & 0.025  \\
\bottomrule
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize \vspace{2pt}Clustered standard errors at department level in parentheses.}}\\
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize $^{+}p<0.1$; $^{*}p<0.05$; $^{**}p<0.01$; $^{***}p<0.001$\vspace{2pt}}}\\
\end{tabularx}
\end{table}

## Black Male

\begin{table}[H]
\caption{Effect on Black Male Speakers}
\label{tab:black_male}
\centering
\scriptsize
\begin{tabularx}{\textwidth}{l*{6}{>{\centering\arraybackslash}X}}
\toprule
 & \% Black Male & \% Black Male & Count Black Male & Count Black Male & Any Black Male & Any Black Male \\
 &  (1) & (2) & (3) & (4) & (5) & (6)  \\
\midrule
Treatment  &  0.538$^{*}$ & 0.514$^{*}$ & 0.071$^{*}$ & 0.070$^{*}$ & 0.058$^{*}$ & 0.056$^{*}$  \\
 &  (0.264) & (0.249) & (0.034) & (0.033) & (0.022) & (0.022)  \\
Constant  &  2.215$^{**}$ & 0.870$^{}$ & 0.365$^{***}$ & 0.097$^{}$ & 0.279$^{***}$ & 0.034$^{}$  \\
 &  (0.708) & (1.164) & (0.092) & (0.143) & (0.060) & (0.103)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,654 & 1,654 & 1,654 & 1,654 & 1,654 & 1,654  \\
Adjusted $R^2$ &  0.018 & 0.022 & 0.040 & 0.047 & 0.035 & 0.044  \\
\bottomrule
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize \vspace{2pt}Clustered standard errors at department level in parentheses.}}\\
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize $^{+}p<0.1$; $^{*}p<0.05$; $^{**}p<0.01$; $^{***}p<0.001$\vspace{2pt}}}\\
\end{tabularx}
\end{table}

## Hispanic Female

\begin{table}[H]
\caption{Effect on Hispanic Female Speakers}
\label{tab:hispanic_female}
\centering
\scriptsize
\begin{tabularx}{\textwidth}{l*{6}{>{\centering\arraybackslash}X}}
\toprule
 & \% Hispanic Female & \% Hispanic Female & Count Hispanic Female & Count Hispanic Female & Any Hispanic Female & Any Hispanic Female \\
 &  (1) & (2) & (3) & (4) & (5) & (6)  \\
\midrule
Treatment  &  -0.134$^{}$ & -0.204$^{}$ & 0.007$^{}$ & 0.000$^{}$ & 0.004$^{}$ & -0.002$^{}$  \\
 &  (0.160) & (0.174) & (0.013) & (0.013) & (0.012) & (0.012)  \\
Constant  &  1.298$^{*}$ & -0.178$^{}$ & 0.062$^{}$ & -0.063$^{}$ & 0.056$^{}$ & -0.065$^{}$  \\
 &  (0.587) & (0.485) & (0.044) & (0.066) & (0.034) & (0.057)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,654 & 1,654 & 1,654 & 1,654 & 1,654 & 1,654  \\
Adjusted $R^2$ &  0.002 & 0.004 & 0.010 & 0.018 & 0.008 & 0.016  \\
\bottomrule
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize \vspace{2pt}Clustered standard errors at department level in parentheses.}}\\
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize $^{+}p<0.1$; $^{*}p<0.05$; $^{**}p<0.01$; $^{***}p<0.001$\vspace{2pt}}}\\
\end{tabularx}
\end{table}

## Hispanic Male

\begin{table}[H]
\caption{Effect on Hispanic Male Speakers}
\label{tab:hispanic_male}
\centering
\scriptsize
\begin{tabularx}{\textwidth}{l*{6}{>{\centering\arraybackslash}X}}
\toprule
 & \% Hispanic Male & \% Hispanic Male & Count Hispanic Male & Count Hispanic Male & Any Hispanic Male & Any Hispanic Male \\
 &  (1) & (2) & (3) & (4) & (5) & (6)  \\
\midrule
Treatment  &  0.133$^{}$ & 0.179$^{}$ & -0.004$^{}$ & -0.024$^{}$ & -0.021$^{}$ & -0.032$^{}$  \\
 &  (0.389) & (0.400) & (0.045) & (0.044) & (0.025) & (0.025)  \\
Constant  &  4.228$^{**}$ & 3.029$^{+}$ & 0.639$^{***}$ & 0.169$^{}$ & 0.439$^{***}$ & 0.178$^{}$  \\
 &  (1.346) & (1.688) & (0.130) & (0.200) & (0.076) & (0.110)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,654 & 1,654 & 1,654 & 1,654 & 1,654 & 1,654  \\
Adjusted $R^2$ &  0.008 & 0.007 & 0.013 & 0.020 & 0.019 & 0.025  \\
\bottomrule
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize \vspace{2pt}Clustered standard errors at department level in parentheses.}}\\
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize $^{+}p<0.1$; $^{*}p<0.05$; $^{**}p<0.01$; $^{***}p<0.001$\vspace{2pt}}}\\
\end{tabularx}
\end{table}

\newpage

# Discipline Subgroup Analysis


\subsubsection{Chemistry (N=270)}

\begin{table}[H]
\caption{Chemistry : Effect on URM Speaker Representation}
\label{tab:discipline_chemistry_urm}
\centering
\scriptsize
\begin{tabularx}{\textwidth}{l*{6}{>{\centering\arraybackslash}X}}
\toprule
 & \% URM & \% URM & Count URM & Count URM & Any URM & Any URM \\
 &  (1) & (2) & (3) & (4) & (5) & (6)  \\
\midrule
Treatment  &  0.469$^{}$ & -0.413$^{}$ & -0.105$^{}$ & -0.185$^{}$ & 0.023$^{}$ & -0.006$^{}$  \\
 &  (1.173) & (1.162) & (0.165) & (0.165) & (0.052) & (0.057)  \\
Constant  &  6.332$^{*}$ & -1.871$^{}$ & 0.930$^{*}$ & -0.747$^{}$ & 0.233$^{+}$ & -0.288$^{}$  \\
 &  (2.674) & (5.820) & (0.411) & (0.779) & (0.133) & (0.266)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  270 & 270 & 270 & 270 & 270 & 270  \\
Adjusted $R^2$ &  -0.024 & -0.019 & 0.100 & 0.108 & 0.106 & 0.115  \\
\bottomrule
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize \vspace{2pt}Clustered standard errors at department level in parentheses.}}\\
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize $^{+}p<0.1$; $^{*}p<0.05$; $^{**}p<0.01$; $^{***}p<0.001$\vspace{2pt}}}\\
\end{tabularx}
\end{table}
\begin{table}[H]
\caption{Chemistry : Effect on Black Speaker Representation}
\label{tab:discipline_chemistry_black}
\centering
\scriptsize
\begin{tabularx}{\textwidth}{l*{6}{>{\centering\arraybackslash}X}}
\toprule
 & \% Black & \% Black & Count Black & Count Black & Any Black & Any Black \\
 &  (1) & (2) & (3) & (4) & (5) & (6)  \\
\midrule
Treatment  &  0.740$^{}$ & 0.399$^{}$ & 0.021$^{}$ & 0.024$^{}$ & 0.090$^{}$ & 0.062$^{}$  \\
 &  (1.057) & (0.848) & (0.121) & (0.100) & (0.065) & (0.059)  \\
Constant  &  2.261$^{}$ & -8.839$^{*}$ & 0.314$^{}$ & -1.603$^{**}$ & 0.120$^{}$ & -0.963$^{**}$  \\
 &  (2.566) & (3.921) & (0.246) & (0.535) & (0.155) & (0.295)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  270 & 270 & 270 & 270 & 270 & 270  \\
Adjusted $R^2$ &  -0.033 & -0.013 & 0.045 & 0.084 & 0.045 & 0.098  \\
\bottomrule
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize \vspace{2pt}Clustered standard errors at department level in parentheses.}}\\
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize $^{+}p<0.1$; $^{*}p<0.05$; $^{**}p<0.01$; $^{***}p<0.001$\vspace{2pt}}}\\
\end{tabularx}
\end{table}
\begin{table}[H]
\caption{Chemistry : Effect on Hispanic Speaker Representation}
\label{tab:discipline_chemistry_hispanic}
\centering
\scriptsize
\begin{tabularx}{\textwidth}{l*{6}{>{\centering\arraybackslash}X}}
\toprule
 & \% Hispanic & \% Hispanic & Count Hispanic & Count Hispanic & Any Hispanic & Any Hispanic \\
 &  (1) & (2) & (3) & (4) & (5) & (6)  \\
\midrule
Treatment  &  -0.205$^{}$ & -0.771$^{}$ & -0.139$^{}$ & -0.230$^{+}$ & -0.105$^{}$ & -0.153$^{*}$  \\
 &  (0.976) & (0.983) & (0.117) & (0.125) & (0.064) & (0.063)  \\
Constant  &  3.238$^{+}$ & 4.762$^{}$ & 0.584$^{}$ & 0.596$^{}$ & 0.258$^{}$ & 0.261$^{}$  \\
 &  (1.788) & (4.913) & (0.361) & (0.548) & (0.162) & (0.304)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  270 & 270 & 270 & 270 & 270 & 270  \\
Adjusted $R^2$ &  -0.024 & -0.021 & 0.046 & 0.077 & 0.035 & 0.062  \\
\bottomrule
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize \vspace{2pt}Clustered standard errors at department level in parentheses.}}\\
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize $^{+}p<0.1$; $^{*}p<0.05$; $^{**}p<0.01$; $^{***}p<0.001$\vspace{2pt}}}\\
\end{tabularx}
\end{table}

\subsubsection{Mathematics (N=811)}

\begin{table}[H]
\caption{Mathematics : Effect on URM Speaker Representation}
\label{tab:discipline_mathematics_urm}
\centering
\scriptsize
\begin{tabularx}{\textwidth}{l*{6}{>{\centering\arraybackslash}X}}
\toprule
 & \% URM & \% URM & Count URM & Count URM & Any URM & Any URM \\
 &  (1) & (2) & (3) & (4) & (5) & (6)  \\
\midrule
Treatment  &  0.944$^{}$ & 1.212$^{}$ & 0.154$^{}$ & 0.151$^{}$ & 0.022$^{}$ & 0.012$^{}$  \\
 &  (0.719) & (0.793) & (0.094) & (0.103) & (0.034) & (0.033)  \\
Constant  &  6.229$^{***}$ & 6.083$^{}$ & 0.872$^{***}$ & 0.210$^{}$ & 0.503$^{***}$ & 0.215$^{}$  \\
 &  (1.421) & (4.161) & (0.145) & (0.546) & (0.068) & (0.193)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  811 & 811 & 811 & 811 & 811 & 811  \\
Adjusted $R^2$ &  0.001 & -0.001 & 0.000 & -0.002 & -0.009 & -0.000  \\
\bottomrule
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize \vspace{2pt}Clustered standard errors at department level in parentheses.}}\\
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize $^{+}p<0.1$; $^{*}p<0.05$; $^{**}p<0.01$; $^{***}p<0.001$\vspace{2pt}}}\\
\end{tabularx}
\end{table}
\begin{table}[H]
\caption{Mathematics : Effect on Black Speaker Representation}
\label{tab:discipline_mathematics_black}
\centering
\scriptsize
\begin{tabularx}{\textwidth}{l*{6}{>{\centering\arraybackslash}X}}
\toprule
 & \% Black & \% Black & Count Black & Count Black & Any Black & Any Black \\
 &  (1) & (2) & (3) & (4) & (5) & (6)  \\
\midrule
Treatment  &  0.236$^{}$ & 0.526$^{}$ & 0.077$^{}$ & 0.113$^{*}$ & 0.019$^{}$ & 0.028$^{}$  \\
 &  (0.393) & (0.430) & (0.049) & (0.054) & (0.029) & (0.027)  \\
Constant  &  0.896$^{+}$ & 1.729$^{}$ & 0.195$^{**}$ & 0.334$^{}$ & 0.170$^{***}$ & 0.053$^{}$  \\
 &  (0.533) & (2.406) & (0.072) & (0.262) & (0.051) & (0.151)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  811 & 811 & 811 & 811 & 811 & 811  \\
Adjusted $R^2$ &  0.012 & 0.020 & 0.010 & 0.023 & 0.005 & 0.019  \\
\bottomrule
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize \vspace{2pt}Clustered standard errors at department level in parentheses.}}\\
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize $^{+}p<0.1$; $^{*}p<0.05$; $^{**}p<0.01$; $^{***}p<0.001$\vspace{2pt}}}\\
\end{tabularx}
\end{table}
\begin{table}[H]
\caption{Mathematics : Effect on Hispanic Speaker Representation}
\label{tab:discipline_mathematics_hispanic}
\centering
\scriptsize
\begin{tabularx}{\textwidth}{l*{6}{>{\centering\arraybackslash}X}}
\toprule
 & \% Hispanic & \% Hispanic & Count Hispanic & Count Hispanic & Any Hispanic & Any Hispanic \\
 &  (1) & (2) & (3) & (4) & (5) & (6)  \\
\midrule
Treatment  &  0.727$^{}$ & 0.690$^{}$ & 0.081$^{}$ & 0.039$^{}$ & 0.028$^{}$ & 0.010$^{}$  \\
 &  (0.640) & (0.682) & (0.074) & (0.072) & (0.034) & (0.036)  \\
Constant  &  5.257$^{***}$ & 4.202$^{}$ & 0.658$^{***}$ & -0.161$^{}$ & 0.398$^{***}$ & 0.182$^{}$  \\
 &  (1.389) & (3.374) & (0.133) & (0.430) & (0.079) & (0.198)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  811 & 811 & 811 & 811 & 811 & 811  \\
Adjusted $R^2$ &  -0.004 & -0.002 & -0.001 & 0.003 & -0.001 & -0.001  \\
\bottomrule
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize \vspace{2pt}Clustered standard errors at department level in parentheses.}}\\
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize $^{+}p<0.1$; $^{*}p<0.05$; $^{**}p<0.01$; $^{***}p<0.001$\vspace{2pt}}}\\
\end{tabularx}
\end{table}

\subsubsection{Physics (N=350)}

\begin{table}[H]
\caption{Physics : Effect on URM Speaker Representation}
\label{tab:discipline_physics_urm}
\centering
\scriptsize
\begin{tabularx}{\textwidth}{l*{6}{>{\centering\arraybackslash}X}}
\toprule
 & \% URM & \% URM & Count URM & Count URM & Any URM & Any URM \\
 &  (1) & (2) & (3) & (4) & (5) & (6)  \\
\midrule
Treatment  &  0.040$^{}$ & 0.104$^{}$ & 0.148$^{}$ & 0.116$^{}$ & -0.012$^{}$ & -0.009$^{}$  \\
 &  (1.192) & (1.142) & (0.133) & (0.132) & (0.060) & (0.052)  \\
Constant  &  13.433$^{***}$ & 9.484$^{}$ & 1.248$^{***}$ & 1.333$^{}$ & 0.407$^{***}$ & 0.829$^{}$  \\
 &  (2.389) & (13.067) & (0.170) & (1.516) & (0.074) & (0.562)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  350 & 350 & 350 & 350 & 350 & 350  \\
Adjusted $R^2$ &  0.003 & -0.005 & 0.004 & 0.012 & 0.001 & 0.029  \\
\bottomrule
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize \vspace{2pt}Clustered standard errors at department level in parentheses.}}\\
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize $^{+}p<0.1$; $^{*}p<0.05$; $^{**}p<0.01$; $^{***}p<0.001$\vspace{2pt}}}\\
\end{tabularx}
\end{table}
\begin{table}[H]
\caption{Physics : Effect on Black Speaker Representation}
\label{tab:discipline_physics_black}
\centering
\scriptsize
\begin{tabularx}{\textwidth}{l*{6}{>{\centering\arraybackslash}X}}
\toprule
 & \% Black & \% Black & Count Black & Count Black & Any Black & Any Black \\
 &  (1) & (2) & (3) & (4) & (5) & (6)  \\
\midrule
Treatment  &  1.479$^{*}$ & 1.604$^{**}$ & 0.174$^{*}$ & 0.182$^{**}$ & 0.123$^{*}$ & 0.128$^{*}$  \\
 &  (0.603) & (0.613) & (0.068) & (0.069) & (0.048) & (0.050)  \\
Constant  &  -0.216$^{}$ & -0.091$^{}$ & 0.031$^{}$ & 0.229$^{}$ & 0.001$^{}$ & 0.017$^{}$  \\
 &  (0.409) & (4.601) & (0.082) & (0.649) & (0.052) & (0.443)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  350 & 350 & 350 & 350 & 350 & 350  \\
Adjusted $R^2$ &  0.002 & -0.002 & 0.020 & 0.009 & 0.012 & 0.015  \\
\bottomrule
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize \vspace{2pt}Clustered standard errors at department level in parentheses.}}\\
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize $^{+}p<0.1$; $^{*}p<0.05$; $^{**}p<0.01$; $^{***}p<0.001$\vspace{2pt}}}\\
\end{tabularx}
\end{table}
\begin{table}[H]
\caption{Physics : Effect on Hispanic Speaker Representation}
\label{tab:discipline_physics_hispanic}
\centering
\scriptsize
\begin{tabularx}{\textwidth}{l*{6}{>{\centering\arraybackslash}X}}
\toprule
 & \% Hispanic & \% Hispanic & Count Hispanic & Count Hispanic & Any Hispanic & Any Hispanic \\
 &  (1) & (2) & (3) & (4) & (5) & (6)  \\
\midrule
Treatment  &  -1.439$^{}$ & -1.500$^{}$ & -0.026$^{}$ & -0.066$^{}$ & -0.074$^{}$ & -0.075$^{}$  \\
 &  (1.170) & (1.160) & (0.115) & (0.119) & (0.064) & (0.060)  \\
Constant  &  13.649$^{***}$ & 9.574$^{}$ & 1.217$^{***}$ & 1.104$^{}$ & 0.435$^{***}$ & 0.738$^{}$  \\
 &  (2.389) & (11.919) & (0.153) & (1.278) & (0.081) & (0.581)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  350 & 350 & 350 & 350 & 350 & 350  \\
Adjusted $R^2$ &  0.001 & -0.010 & -0.007 & 0.014 & -0.002 & 0.010  \\
\bottomrule
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize \vspace{2pt}Clustered standard errors at department level in parentheses.}}\\
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize $^{+}p<0.1$; $^{*}p<0.05$; $^{**}p<0.01$; $^{***}p<0.001$\vspace{2pt}}}\\
\end{tabularx}
\end{table}

\subsubsection{Computer Science (N=142)}

\begin{table}[H]
\caption{Computer Science : Effect on URM Speaker Representation}
\label{tab:discipline_computer_science_urm}
\centering
\scriptsize
\begin{tabularx}{\textwidth}{l*{6}{>{\centering\arraybackslash}X}}
\toprule
 & \% URM & \% URM & Count URM & Count URM & Any URM & Any URM \\
 &  (1) & (2) & (3) & (4) & (5) & (6)  \\
\midrule
Treatment  &  2.148$^{}$ & 2.645$^{}$ & 0.073$^{}$ & 0.063$^{}$ & 0.110$^{}$ & 0.109$^{}$  \\
 &  (1.370) & (1.775) & (0.162) & (0.212) & (0.091) & (0.094)  \\
Constant  &  7.104$^{***}$ & 16.416$^{}$ & 1.378$^{***}$ & 4.200$^{**}$ & 0.882$^{***}$ & 2.540$^{***}$  \\
 &  (1.952) & (13.370) & (0.329) & (1.453) & (0.186) & (0.674)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  142 & 142 & 142 & 142 & 142 & 142  \\
Adjusted $R^2$ &  0.031 & 0.076 & 0.067 & 0.058 & 0.081 & 0.100  \\
\bottomrule
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize \vspace{2pt}Clustered standard errors at department level in parentheses.}}\\
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize $^{+}p<0.1$; $^{*}p<0.05$; $^{**}p<0.01$; $^{***}p<0.001$\vspace{2pt}}}\\
\end{tabularx}
\end{table}
\begin{table}[H]
\caption{Computer Science : Effect on Black Speaker Representation}
\label{tab:discipline_computer_science_black}
\centering
\scriptsize
\begin{tabularx}{\textwidth}{l*{6}{>{\centering\arraybackslash}X}}
\toprule
 & \% Black & \% Black & Count Black & Count Black & Any Black & Any Black \\
 &  (1) & (2) & (3) & (4) & (5) & (6)  \\
\midrule
Treatment  &  0.203$^{}$ & -0.178$^{}$ & -0.057$^{}$ & -0.065$^{}$ & -0.018$^{}$ & -0.042$^{}$  \\
 &  (0.698) & (0.713) & (0.064) & (0.072) & (0.055) & (0.067)  \\
Constant  &  4.152$^{**}$ & 3.617$^{}$ & 0.703$^{***}$ & 2.104$^{*}$ & 0.603$^{***}$ & 1.437$^{*}$  \\
 &  (1.454) & (9.859) & (0.207) & (0.917) & (0.155) & (0.696)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  142 & 142 & 142 & 142 & 142 & 142  \\
Adjusted $R^2$ &  -0.041 & -0.076 & 0.042 & 0.027 & 0.051 & 0.026  \\
\bottomrule
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize \vspace{2pt}Clustered standard errors at department level in parentheses.}}\\
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize $^{+}p<0.1$; $^{*}p<0.05$; $^{**}p<0.01$; $^{***}p<0.001$\vspace{2pt}}}\\
\end{tabularx}
\end{table}
\begin{table}[H]
\caption{Computer Science : Effect on Hispanic Speaker Representation}
\label{tab:discipline_computer_science_hispanic}
\centering
\scriptsize
\begin{tabularx}{\textwidth}{l*{6}{>{\centering\arraybackslash}X}}
\toprule
 & \% Hispanic & \% Hispanic & Count Hispanic & Count Hispanic & Any Hispanic & Any Hispanic \\
 &  (1) & (2) & (3) & (4) & (5) & (6)  \\
\midrule
Treatment  &  1.945$^{}$ & 2.823$^{}$ & 0.131$^{}$ & 0.128$^{}$ & 0.136$^{}$ & 0.156$^{+}$  \\
 &  (1.458) & (1.754) & (0.145) & (0.182) & (0.096) & (0.089)  \\
Constant  &  2.952$^{}$ & 12.798$^{}$ & 0.675$^{*}$ & 2.097$^{+}$ & 0.589$^{**}$ & 2.245$^{**}$  \\
 &  (2.209) & (11.268) & (0.305) & (1.089) & (0.224) & (0.704)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  142 & 142 & 142 & 142 & 142 & 142  \\
Adjusted $R^2$ &  0.039 & 0.101 & 0.029 & 0.018 & 0.066 & 0.088  \\
\bottomrule
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize \vspace{2pt}Clustered standard errors at department level in parentheses.}}\\
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize $^{+}p<0.1$; $^{*}p<0.05$; $^{**}p<0.01$; $^{***}p<0.001$\vspace{2pt}}}\\
\end{tabularx}
\end{table}

\subsubsection{Mechanical Engineering (N=81)}

\begin{table}[H]
\caption{Mechanical Engineering : Effect on URM Speaker Representation}
\label{tab:discipline_mechanical_engineering_urm}
\centering
\scriptsize
\begin{tabularx}{\textwidth}{l*{6}{>{\centering\arraybackslash}X}}
\toprule
 & \% URM & \% URM & Count URM & Count URM & Any URM & Any URM \\
 &  (1) & (2) & (3) & (4) & (5) & (6)  \\
\midrule
Treatment  &  3.859$^{+}$ & 2.959$^{}$ & 0.665$^{*}$ & 0.731$^{+}$ & 0.113$^{}$ & 0.107$^{}$  \\
 &  (2.026) & (2.002) & (0.300) & (0.370) & (0.116) & (0.130)  \\
Constant  &  17.140$^{**}$ & 0.793$^{}$ & 2.618$^{**}$ & 1.814$^{}$ & 0.792$^{**}$ & 0.316$^{}$  \\
 &  (5.984) & (11.347) & (0.963) & (2.267) & (0.279) & (0.597)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  81 & 81 & 81 & 81 & 81 & 81  \\
Adjusted $R^2$ &  0.039 & 0.055 & 0.033 & 0.133 & -0.002 & -0.009  \\
\bottomrule
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize \vspace{2pt}Clustered standard errors at department level in parentheses.}}\\
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize $^{+}p<0.1$; $^{*}p<0.05$; $^{**}p<0.01$; $^{***}p<0.001$\vspace{2pt}}}\\
\end{tabularx}
\end{table}
\begin{table}[H]
\caption{Mechanical Engineering : Effect on Black Speaker Representation}
\label{tab:discipline_mechanical_engineering_black}
\centering
\scriptsize
\begin{tabularx}{\textwidth}{l*{6}{>{\centering\arraybackslash}X}}
\toprule
 & \% Black & \% Black & Count Black & Count Black & Any Black & Any Black \\
 &  (1) & (2) & (3) & (4) & (5) & (6)  \\
\midrule
Treatment  &  3.942$^{***}$ & 2.942$^{**}$ & 0.646$^{***}$ & 0.551$^{*}$ & 0.346$^{***}$ & 0.310$^{**}$  \\
 &  (0.999) & (0.937) & (0.185) & (0.210) & (0.090) & (0.097)  \\
Constant  &  8.540$^{**}$ & 6.694$^{}$ & 0.966$^{***}$ & 0.498$^{}$ & 0.818$^{***}$ & 0.679$^{}$  \\
 &  (2.526) & (5.016) & (0.149) & (1.711) & (0.174) & (0.466)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  81 & 81 & 81 & 81 & 81 & 81  \\
Adjusted $R^2$ &  0.153 & 0.170 & 0.129 & 0.185 & 0.157 & 0.196  \\
\bottomrule
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize \vspace{2pt}Clustered standard errors at department level in parentheses.}}\\
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize $^{+}p<0.1$; $^{*}p<0.05$; $^{**}p<0.01$; $^{***}p<0.001$\vspace{2pt}}}\\
\end{tabularx}
\end{table}
\begin{table}[H]
\caption{Mechanical Engineering : Effect on Hispanic Speaker Representation}
\label{tab:discipline_mechanical_engineering_hispanic}
\centering
\scriptsize
\begin{tabularx}{\textwidth}{l*{6}{>{\centering\arraybackslash}X}}
\toprule
 & \% Hispanic & \% Hispanic & Count Hispanic & Count Hispanic & Any Hispanic & Any Hispanic \\
 &  (1) & (2) & (3) & (4) & (5) & (6)  \\
\midrule
Treatment  &  -0.083$^{}$ & 0.017$^{}$ & 0.019$^{}$ & 0.181$^{}$ & -0.034$^{}$ & 0.006$^{}$  \\
 &  (1.897) & (1.900) & (0.227) & (0.244) & (0.122) & (0.132)  \\
Constant  &  8.600$^{+}$ & -5.901$^{}$ & 1.652$^{+}$ & 1.316$^{}$ & 0.585$^{*}$ & 0.036$^{}$  \\
 &  (4.526) & (11.026) & (0.926) & (1.569) & (0.291) & (0.645)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  81 & 81 & 81 & 81 & 81 & 81  \\
Adjusted $R^2$ &  -0.053 & -0.041 & 0.025 & 0.067 & -0.015 & 0.001  \\
\bottomrule
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize \vspace{2pt}Clustered standard errors at department level in parentheses.}}\\
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize $^{+}p<0.1$; $^{*}p<0.05$; $^{**}p<0.01$; $^{***}p<0.001$\vspace{2pt}}}\\
\end{tabularx}
\end{table}

\newpage

# Semester-Specific Analysis

## Fall Semester

\begin{table}[H]
\caption{Fall: Effect on URM Speakers}
\label{tab:fall_urm}
\centering
\scriptsize
\begin{tabularx}{\textwidth}{l*{6}{>{\centering\arraybackslash}X}}
\toprule
 & \% URM & \% URM & Count URM & Count URM & Any URM & Any URM \\
 &  (1) & (2) & (3) & (4) & (5) & (6)  \\
\midrule
Treatment  &  0.949$^{}$ & 0.859$^{}$ & 0.078$^{+}$ & 0.049$^{}$ & 0.033$^{}$ & 0.020$^{}$  \\
 &  (0.695) & (0.687) & (0.046) & (0.044) & (0.025) & (0.025)  \\
Constant  &  6.357$^{**}$ & -2.483$^{}$ & 0.538$^{***}$ & -0.283$^{}$ & 0.366$^{***}$ & -0.058$^{}$  \\
 &  (2.449) & (3.059) & (0.145) & (0.212) & (0.070) & (0.111)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,448 & 1,448 & 1,448 & 1,448 & 1,448 & 1,448  \\
Adjusted $R^2$ &  0.018 & 0.026 & 0.024 & 0.040 & 0.023 & 0.035  \\
\bottomrule
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize \vspace{2pt}Clustered standard errors at department level in parentheses.}}\\
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize $^{+}p<0.1$; $^{*}p<0.05$; $^{**}p<0.01$; $^{***}p<0.001$\vspace{2pt}}}\\
\end{tabularx}
\end{table}
\begin{table}[H]
\caption{Fall: Effect on Black Speakers}
\label{tab:fall_black}
\centering
\scriptsize
\begin{tabularx}{\textwidth}{l*{6}{>{\centering\arraybackslash}X}}
\toprule
 & \% Black & \% Black & Count Black & Count Black & Any Black & Any Black \\
 &  (1) & (2) & (3) & (4) & (5) & (6)  \\
\midrule
Treatment  &  0.494$^{}$ & 0.456$^{}$ & 0.053$^{*}$ & 0.050$^{*}$ & 0.043$^{**}$ & 0.042$^{*}$  \\
 &  (0.333) & (0.334) & (0.021) & (0.021) & (0.017) & (0.017)  \\
Constant  &  2.863$^{**}$ & -1.651$^{}$ & 0.224$^{***}$ & -0.075$^{}$ & 0.172$^{***}$ & -0.067$^{}$  \\
 &  (0.987) & (1.434) & (0.061) & (0.097) & (0.046) & (0.080)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,448 & 1,448 & 1,448 & 1,448 & 1,448 & 1,448  \\
Adjusted $R^2$ &  0.023 & 0.037 & 0.033 & 0.046 & 0.028 & 0.041  \\
\bottomrule
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize \vspace{2pt}Clustered standard errors at department level in parentheses.}}\\
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize $^{+}p<0.1$; $^{*}p<0.05$; $^{**}p<0.01$; $^{***}p<0.001$\vspace{2pt}}}\\
\end{tabularx}
\end{table}
\begin{table}[H]
\caption{Fall: Effect on Hispanic Speakers}
\label{tab:fall_hispanic}
\centering
\scriptsize
\begin{tabularx}{\textwidth}{l*{6}{>{\centering\arraybackslash}X}}
\toprule
 & \% Hispanic & \% Hispanic & Count Hispanic & Count Hispanic & Any Hispanic & Any Hispanic \\
 &  (1) & (2) & (3) & (4) & (5) & (6)  \\
\midrule
Treatment  &  0.437$^{}$ & 0.371$^{}$ & 0.024$^{}$ & -0.003$^{}$ & 0.009$^{}$ & -0.006$^{}$  \\
 &  (0.635) & (0.657) & (0.038) & (0.038) & (0.024) & (0.025)  \\
Constant  &  3.351$^{}$ & -1.075$^{}$ & 0.301$^{*}$ & -0.231$^{}$ & 0.236$^{**}$ & -0.066$^{}$  \\
 &  (2.358) & (2.931) & (0.134) & (0.188) & (0.073) & (0.109)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,448 & 1,448 & 1,448 & 1,448 & 1,448 & 1,448  \\
Adjusted $R^2$ &  0.011 & 0.010 & 0.020 & 0.030 & 0.022 & 0.028  \\
\bottomrule
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize \vspace{2pt}Clustered standard errors at department level in parentheses.}}\\
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize $^{+}p<0.1$; $^{*}p<0.05$; $^{**}p<0.01$; $^{***}p<0.001$\vspace{2pt}}}\\
\end{tabularx}
\end{table}

## Spring Semester

\begin{table}[H]
\caption{Spring: Effect on URM Speakers}
\label{tab:spring_urm}
\centering
\scriptsize
\begin{tabularx}{\textwidth}{l*{6}{>{\centering\arraybackslash}X}}
\toprule
 & \% URM & \% URM & Count URM & Count URM & Any URM & Any URM \\
 &  (1) & (2) & (3) & (4) & (5) & (6)  \\
\midrule
Treatment  &  0.468$^{}$ & 0.520$^{}$ & 0.007$^{}$ & 0.009$^{}$ & -0.013$^{}$ & -0.013$^{}$  \\
 &  (0.737) & (0.757) & (0.055) & (0.056) & (0.028) & (0.028)  \\
Constant  &  8.564$^{***}$ & 8.921$^{**}$ & 0.985$^{***}$ & 0.897$^{***}$ & 0.539$^{***}$ & 0.420$^{***}$  \\
 &  (1.839) & (3.097) & (0.144) & (0.251) & (0.073) & (0.122)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,385 & 1,385 & 1,385 & 1,385 & 1,385 & 1,385  \\
Adjusted $R^2$ &  0.001 & 0.000 & 0.022 & 0.019 & 0.022 & 0.023  \\
\bottomrule
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize \vspace{2pt}Clustered standard errors at department level in parentheses.}}\\
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize $^{+}p<0.1$; $^{*}p<0.05$; $^{**}p<0.01$; $^{***}p<0.001$\vspace{2pt}}}\\
\end{tabularx}
\end{table}
\begin{table}[H]
\caption{Spring: Effect on Black Speakers}
\label{tab:spring_black}
\centering
\scriptsize
\begin{tabularx}{\textwidth}{l*{6}{>{\centering\arraybackslash}X}}
\toprule
 & \% Black & \% Black & Count Black & Count Black & Any Black & Any Black \\
 &  (1) & (2) & (3) & (4) & (5) & (6)  \\
\midrule
Treatment  &  0.831$^{+}$ & 0.844$^{+}$ & 0.036$^{}$ & 0.039$^{}$ & 0.026$^{}$ & 0.028$^{}$  \\
 &  (0.464) & (0.446) & (0.035) & (0.034) & (0.023) & (0.023)  \\
Constant  &  1.814$^{+}$ & 1.523$^{}$ & 0.322$^{***}$ & 0.305$^{*}$ & 0.235$^{***}$ & 0.176$^{+}$  \\
 &  (1.018) & (1.731) & (0.088) & (0.149) & (0.059) & (0.102)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,385 & 1,385 & 1,385 & 1,385 & 1,385 & 1,385  \\
Adjusted $R^2$ &  0.010 & 0.009 & 0.031 & 0.033 & 0.022 & 0.022  \\
\bottomrule
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize \vspace{2pt}Clustered standard errors at department level in parentheses.}}\\
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize $^{+}p<0.1$; $^{*}p<0.05$; $^{**}p<0.01$; $^{***}p<0.001$\vspace{2pt}}}\\
\end{tabularx}
\end{table}
\begin{table}[H]
\caption{Spring: Effect on Hispanic Speakers}
\label{tab:spring_hispanic}
\centering
\scriptsize
\begin{tabularx}{\textwidth}{l*{6}{>{\centering\arraybackslash}X}}
\toprule
 & \% Hispanic & \% Hispanic & Count Hispanic & Count Hispanic & Any Hispanic & Any Hispanic \\
 &  (1) & (2) & (3) & (4) & (5) & (6)  \\
\midrule
Treatment  &  -0.342$^{}$ & -0.310$^{}$ & -0.028$^{}$ & -0.030$^{}$ & -0.034$^{}$ & -0.036$^{}$  \\
 &  (0.625) & (0.648) & (0.040) & (0.040) & (0.026) & (0.027)  \\
Constant  &  6.528$^{***}$ & 7.174$^{*}$ & 0.645$^{***}$ & 0.571$^{**}$ & 0.415$^{***}$ & 0.337$^{**}$  \\
 &  (1.662) & (2.817) & (0.115) & (0.193) & (0.073) & (0.108)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,385 & 1,385 & 1,385 & 1,385 & 1,385 & 1,385  \\
Adjusted $R^2$ &  -0.007 & -0.007 & 0.008 & 0.010 & 0.013 & 0.015  \\
\bottomrule
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize \vspace{2pt}Clustered standard errors at department level in parentheses.}}\\
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize $^{+}p<0.1$; $^{*}p<0.05$; $^{**}p<0.01$; $^{***}p<0.001$\vspace{2pt}}}\\
\end{tabularx}
\end{table}

\newpage

# Heterogeneity Analysis

## Moderation by Department Ranking

\begin{table}[H]
\caption{Effect by Department Rank}
\label{tab:mod_ranking}
\centering
\scriptsize
\begin{tabularx}{\textwidth}{l*{6}{>{\centering\arraybackslash}X}}
\toprule
 & \% URM & \% URM & Count URM & Count URM & Any URM & Any URM \\
 &  (1) & (2) & (3) & (4) & (5) & (6)  \\
\midrule
Treatment  &  0.623$^{}$ & 0.622$^{}$ & 0.087$^{}$ & 0.051$^{}$ & 0.018$^{}$ & 0.007$^{}$  \\
 &  (0.513) & (0.513) & (0.065) & (0.064) & (0.025) & (0.024)  \\
Constant  &  9.549$^{***}$ & 5.515$^{**}$ & 1.117$^{***}$ & 0.297$^{}$ & 0.529$^{***}$ & 0.203$^{+}$  \\
 &  (1.639) & (1.956) & (0.175) & (0.256) & (0.077) & (0.110)  \\
Dept Ranking (centered)  &  0.014$^{}$ & 0.028$^{*}$ & -0.003$^{**}$ & -0.001$^{}$ & -0.002$^{**}$ & -0.001$^{}$  \\
 &  (0.013) & (0.013) & (0.001) & (0.001) & (0.001) & (0.001)  \\
Treatment $\times$ Dept Ranking (centered)  &  0.008$^{}$ & 0.007$^{}$ & 0.005$^{**}$ & 0.005$^{**}$ & 0.001$^{}$ & 0.001$^{+}$  \\
 &  (0.016) & (0.016) & (0.002) & (0.002) & (0.001) & (0.001)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,654 & 1,654 & 1,654 & 1,654 & 1,654 & 1,654  \\
Adjusted $R^2$ &  0.011 & 0.014 & 0.033 & 0.042 & 0.029 & 0.040  \\
\bottomrule
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize \vspace{2pt}Clustered standard errors at department level in parentheses.}}\\
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize $^{+}p<0.1$; $^{*}p<0.05$; $^{**}p<0.01$; $^{***}p<0.001$\vspace{2pt}}}\\
\end{tabularx}
\end{table}

\newpage

## Moderation by Total Faculty Size

\begin{table}[H]
\caption{Effect by Faculty Size}
\label{tab:mod_faculty_size}
\centering
\scriptsize
\begin{tabularx}{\textwidth}{l*{6}{>{\centering\arraybackslash}X}}
\toprule
 & \% URM & \% URM & Count URM & Count URM & Any URM & Any URM \\
 &  (1) & (2) & (3) & (4) & (5) & (6)  \\
\midrule
Treatment  &  0.834$^{}$ & 0.650$^{}$ & 0.063$^{}$ & 0.055$^{}$ & 0.008$^{}$ & 0.009$^{}$  \\
 &  (0.531) & (0.513) & (0.069) & (0.065) & (0.025) & (0.024)  \\
Constant  &  8.374$^{***}$ & 3.142$^{}$ & 1.154$^{***}$ & 0.295$^{}$ & 0.567$^{***}$ & 0.213$^{+}$  \\
 &  (1.593) & (2.097) & (0.179) & (0.294) & (0.070) & (0.114)  \\
Total Faculty (centered)  &  -0.035$^{}$ & -0.028$^{}$ & 0.004$^{}$ & 0.003$^{}$ & 0.001$^{}$ & -0.000$^{}$  \\
 &  (0.026) & (0.026) & (0.003) & (0.003) & (0.001) & (0.001)  \\
Treatment $\times$ Total Faculty (centered)  &  0.025$^{}$ & 0.013$^{}$ & -0.002$^{}$ & -0.003$^{}$ & 0.001$^{}$ & 0.000$^{}$  \\
 &  (0.029) & (0.029) & (0.003) & (0.003) & (0.001) & (0.001)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,654 & 1,654 & 1,654 & 1,654 & 1,654 & 1,654  \\
Adjusted $R^2$ &  0.010 & 0.014 & 0.029 & 0.037 & 0.026 & 0.038  \\
\bottomrule
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize \vspace{2pt}Clustered standard errors at department level in parentheses.}}\\
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize $^{+}p<0.1$; $^{*}p<0.05$; $^{**}p<0.01$; $^{***}p<0.001$\vspace{2pt}}}\\
\end{tabularx}
\end{table}

\newpage

## Moderation by URM Faculty in Peer Departments

\begin{table}[H]
\caption{Effect by Peer URM Faculty}
\label{tab:mod_peer_urm}
\centering
\scriptsize
\begin{tabularx}{\textwidth}{l*{6}{>{\centering\arraybackslash}X}}
\toprule
 & \% URM & \% URM & Count URM & Count URM & Any URM & Any URM \\
 &  (1) & (2) & (3) & (4) & (5) & (6)  \\
\midrule
Treatment  &  0.670$^{}$ & 0.611$^{}$ & 0.091$^{}$ & 0.056$^{}$ & 0.018$^{}$ & 0.008$^{}$  \\
 &  (0.516) & (0.518) & (0.065) & (0.064) & (0.025) & (0.024)  \\
Constant  &  8.283$^{***}$ & 7.695$^{***}$ & 1.116$^{***}$ & 0.815$^{***}$ & 0.569$^{***}$ & 0.419$^{***}$  \\
 &  (1.575) & (1.789) & (0.167) & (0.234) & (0.068) & (0.100)  \\
Peer URM Faculty (centered)  &  0.069$^{}$ & 0.139$^{*}$ & 0.017$^{**}$ & 0.021$^{***}$ & 0.007$^{**}$ & 0.007$^{**}$  \\
 &  (0.053) & (0.054) & (0.005) & (0.006) & (0.002) & (0.002)  \\
Treatment $\times$ Peer URM Faculty (centered)  &  -0.057$^{}$ & -0.047$^{}$ & -0.005$^{}$ & -0.006$^{}$ & -0.001$^{}$ & -0.001$^{}$  \\
 &  (0.071) & (0.071) & (0.008) & (0.008) & (0.003) & (0.003)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,654 & 1,654 & 1,654 & 1,654 & 1,654 & 1,654  \\
Adjusted $R^2$ &  0.010 & 0.014 & 0.035 & 0.037 & 0.034 & 0.038  \\
\bottomrule
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize \vspace{2pt}Clustered standard errors at department level in parentheses.}}\\
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize $^{+}p<0.1$; $^{*}p<0.05$; $^{**}p<0.01$; $^{***}p<0.001$\vspace{2pt}}}\\
\end{tabularx}
\end{table}


\clearpage
\section{Summary of All Significant Results}

\begin{table}[H]
\caption{All Significant Results (p < 0.1) from All Analyses (Excluding Constant Term)}
\label{tab:all_significant_results}
\centering
{\scriptsize % Start group for scriptsize and tabcolsep
\setlength{\tabcolsep}{2pt} % Reduce column separation further
\begin{tabular}{p{3.2cm} p{2.3cm} p{2.3cm} l r r r r l}
\toprule
Analysis & Outcome & Variable & Model & Coef. & SE & t-stat & p-value & Sig. \\
\midrule
\multicolumn{9}{l}{\textbf{Discipline Analysis}} \\
\midrule
Chemistry & Any Hispanic & Treatment & Extended & -0.1528 & 0.0628 & -2.433 & 0.0157 & * \\
Chemistry & Count Hispanic & Treatment & Extended & -0.2296 & 0.1246 & -1.842 & 0.0666 & + \\
Computer Science & Any Hispanic & Treatment & Extended & 0.1556 & 0.0892 & 1.745 & 0.0836 & + \\
Mathematics & Count Black & Treatment & Extended & 0.1125 & 0.0541 & 2.079 & 0.0379 & * \\
Mechanical Engineering & \% Black & Treatment & Simple & 3.9420 & 0.9989 & 3.946 & 0.0002 & *** \\
Mechanical Engineering & \% URM & Treatment & Simple & 3.8590 & 2.0259 & 1.905 & 0.0613 & + \\
Mechanical Engineering & Any Black & Treatment & Simple & 0.3462 & 0.0898 & 3.855 & 0.0003 & *** \\
Mechanical Engineering & Count Black & Treatment & Simple & 0.6458 & 0.1853 & 3.486 & 0.0009 & *** \\
Mechanical Engineering & Count URM & Treatment & Simple & 0.6652 & 0.2998 & 2.219 & 0.0301 & * \\
Physics & \% Black & Treatment & Extended & 1.6042 & 0.6127 & 2.618 & 0.0093 & ** \\
Physics & Any Black & Treatment & Simple & 0.1228 & 0.0479 & 2.561 & 0.0109 & * \\
Physics & Count Black & Treatment & Extended & 0.1820 & 0.0692 & 2.629 & 0.0090 & ** \\
\addlinespace[0.5em]
\multicolumn{9}{l}{\textbf{Identity Analysis}} \\
\midrule
Demographic Subgroup & \% Black & Treatment & Extended & 0.6640 & 0.2941 & 2.258 & 0.0241 & * \\
Demographic Subgroup & \% Black Female & Treatment & Extended & 0.1503 & 0.0719 & 2.091 & 0.0367 & * \\
Demographic Subgroup & \% Black Male & Treatment & Extended & 0.5136 & 0.2486 & 2.066 & 0.0390 & * \\
Demographic Subgroup & Any Black & Treatment & Simple & 0.0547 & 0.0227 & 2.412 & 0.0160 & * \\
Demographic Subgroup & Any Black Female & Treatment & Extended & 0.0149 & 0.0081 & 1.839 & 0.0662 & + \\
Demographic Subgroup & Any Black Male & Treatment & Simple & 0.0578 & 0.0225 & 2.576 & 0.0101 & * \\
Demographic Subgroup & Count Black & Treatment & Extended & 0.0812 & 0.0376 & 2.157 & 0.0311 & * \\
Demographic Subgroup & Count Black Male & Treatment & Extended & 0.0696 & 0.0326 & 2.133 & 0.0331 & * \\
\addlinespace[0.5em]
\multicolumn{9}{l}{\textbf{Moderation Analysis}} \\
\midrule
Department Rank & Any URM & Treatment $\times$ Dept Ranking & Extended & 0.0012 & 0.0006 & 1.857 & 0.0634 & + \\
Department Rank & Count URM & Treatment $\times$ Dept Ranking & Extended & 0.0054 & 0.0018 & 2.966 & 0.0031 & ** \\
\addlinespace[0.5em]
\multicolumn{9}{l}{\textbf{Semester Analysis}} \\
\midrule
Fall Semester & Any Black & Treatment & Simple & 0.0434 & 0.0167 & 2.603 & 0.0093 & ** \\
Fall Semester & Count Black & Treatment & Simple & 0.0531 & 0.0209 & 2.541 & 0.0112 & * \\
Fall Semester & Count URM & Treatment & Simple & 0.0780 & 0.0456 & 1.711 & 0.0873 & + \\
Spring Semester & \% Black & Treatment & Extended & 0.8443 & 0.4464 & 1.891 & 0.0588 & + \\
\bottomrule
\end{tabular}
} % End group for scriptsize and tabcolsep
\parbox{\linewidth}{\footnotesize Note: Significance levels: + p<0.1; * p<0.05; ** p<0.01; *** p<0.001. SE = Clustered standard errors at department level. Constant terms are excluded from this summary.}
\end{table}

## Exploratory Analysis: Seniority Moderation

### Analysis 1: Does speaker seniority moderate the treatment effect?


\clearpage
\section{Exploratory Analysis: Seniority Moderation}

\subsection{Distribution of Years Since PhD}

\textbf{Seniority Data Coverage:}

- Total seminars with seniority data: 1624 (98.2\% of total)
- Number of departments: 522
- Mean of seminar-level mean years since PhD: 15.7 (SD = 7.5)
- Median of seminar-level mean years since PhD: 15.1
- Range of seminar means: 1.0 to 59.0 years
- IQR of seminar means: 10.5 to 20.0 years

\subsection{Continuous Moderation Analysis}

We test whether the average seniority of speakers in a seminar moderates the treatment effect on Black speaker representation.

Note: Seniority is measured as the mean years since PhD for speakers in each seminar.

\subsubsection{Outcome: Percentage Black Speakers}

\begin{table}[H]
\caption{Seniority Moderation Analysis: Percentage Black Speakers}
\centering
\begin{tabular}{lccc}
\toprule
 & (1) & (2) & (3) \\
 & Main Effects & Interaction & With Controls \\
\midrule
Treatment & 0.8131* & 0.8330* & 0.9043** \\
 & (0.3357) & (0.3440) & (0.3280) \\
Years Since PhD (centered) & -0.0161 & -0.0018 & -0.0017 \\
 & (0.0188) & (0.0234) & (0.0233) \\
Treatment × Years Since PhD &   & -0.0311 & -0.0368 \\
 &   & (0.0385) & (0.0385) \\
\midrule
Observations & 1624 & 1624 & 1624 \\
R-squared & 0.005 & 0.005 & 0.017 \\
Controls & No & No & Yes \\
\bottomrule
\end{tabular}
\parbox{\linewidth}{\footnotesize Note: Clustered standard errors at department level in parentheses. Years since PhD is the mean years since PhD for speakers in each seminar, centered at the median. Controls include department ranking, total faculty, and fraction URM faculty. Significance: + p<0.1; * p<0.05; ** p<0.01; *** p<0.001.}
\end{table}

\subsubsection{Outcome: Any Black Speakers}

\begin{table}[H]
\caption{Seniority Moderation Analysis: Any Black Speakers}
\centering
\begin{tabular}{lccc}
\toprule
 & (1) & (2) & (3) \\
 & Main Effects & Interaction & With Controls \\
\midrule
Treatment & 0.0632** & 0.0611* & 0.0689** \\
 & (0.0239) & (0.0240) & (0.0236) \\
Years Since PhD (centered) & 0.0003 & -0.0012 & -0.0012 \\
 & (0.0013) & (0.0016) & (0.0016) \\
Treatment × Years Since PhD &   & 0.0032 & 0.0029 \\
 &   & (0.0027) & (0.0026) \\
\midrule
Observations & 1624 & 1624 & 1624 \\
R-squared & 0.006 & 0.006 & 0.014 \\
Controls & No & No & Yes \\
\bottomrule
\end{tabular}
\parbox{\linewidth}{\footnotesize Note: Clustered standard errors at department level in parentheses. Years since PhD is the mean years since PhD for speakers in each seminar, centered at the median. Controls include department ranking, total faculty, and fraction URM faculty. Significance: + p<0.1; * p<0.05; ** p<0.01; *** p<0.001.}
\end{table}

\subsection{Subgroup Analysis: Seminars with Senior vs Junior Speakers}

\textbf{Median Split Groups:}

- Seminars with junior speakers (n=812): Mean = 10.0 years, Range = 1.0-15.1 years
- Seminars with senior speakers (n=812): Mean = 21.4 years, Range = 15.1-59.0 years

\subsubsection{Outcome: Percentage Black Speakers}

\begin{table}[H]
\caption{Subgroup Analysis by Seniority: Percentage Black Speakers}
\centering
\begin{tabular}{lcccc}
\toprule
 & \multicolumn{2}{c}{Seminars with Junior Speakers} & \multicolumn{2}{c}{Seminars with Senior Speakers} \\
 & (1) & (2) & (3) & (4) \\
 & Simple & With Controls & Simple & With Controls \\
\midrule
Treatment & 1.0238* & 1.1521* & 0.5718 & 0.6162 \\
 & (0.4826) & (0.4819) & (0.4160) & (0.4001) \\
\midrule
Observations & 812 & 812 & 812 & 812 \\
R-squared & 0.006 & 0.024 & 0.003 & 0.010 \\
Controls & No & Yes & No & Yes \\
\bottomrule
\end{tabular}
\parbox{\linewidth}{\footnotesize Note: Clustered standard errors at department level in parentheses. Junior/Senior split at median of seminar-level mean years since PhD. Controls include department ranking, total faculty, and fraction URM faculty. Significance: + p<0.1; * p<0.05; ** p<0.01; *** p<0.001.}
\end{table}

\textbf{Test for Difference Between Groups:}

Difference in treatment effect (Senior - Junior): -0.4520 (SE = 0.6026), p = 0.4534

\subsubsection{Outcome: Any Black Speakers}

\begin{table}[H]
\caption{Subgroup Analysis by Seniority: Any Black Speakers}
\centering
\begin{tabular}{lcccc}
\toprule
 & \multicolumn{2}{c}{Seminars with Junior Speakers} & \multicolumn{2}{c}{Seminars with Senior Speakers} \\
 & (1) & (2) & (3) & (4) \\
 & Simple & With Controls & Simple & With Controls \\
\midrule
Treatment & 0.0324 & 0.0429 & 0.0910** & 0.0938** \\
 & (0.0305) & (0.0307) & (0.0340) & (0.0340) \\
\midrule
Observations & 812 & 812 & 812 & 812 \\
R-squared & 0.002 & 0.007 & 0.011 & 0.020 \\
Controls & No & Yes & No & Yes \\
\bottomrule
\end{tabular}
\parbox{\linewidth}{\footnotesize Note: Clustered standard errors at department level in parentheses. Junior/Senior split at median of seminar-level mean years since PhD. Controls include department ranking, total faculty, and fraction URM faculty. Significance: + p<0.1; * p<0.05; ** p<0.01; *** p<0.001.}
\end{table}

\textbf{Test for Difference Between Groups:}

Difference in treatment effect (Senior - Junior): 0.0586 (SE = 0.0437), p = 0.1804

## Exploratory Analysis: Discipline Moderation

### Analysis 2: Does academic discipline moderate the treatment effect?


\clearpage
\section{Exploratory Analysis: Discipline Moderation}

\subsection{Distribution Across Disciplines}

\begin{table}[H]
\caption{Sample Distribution by Discipline}
\centering
\begin{tabular}{lrrrrr}
\toprule
Discipline & Seminars & Departments & Treatment & Control & \% of Total \\
\midrule
Mathematics & 811 & 134 & 381 & 430 & 49.0\% \\
Physics & 350 & 125 & 181 & 169 & 21.2\% \\
Chemistry & 270 & 122 & 143 & 127 & 16.3\% \\
Computer Science & 142 & 82 & 66 & 76 & 8.6\% \\
Mechanical Engineering & 81 & 65 & 38 & 43 & 4.9\% \\
\midrule
Total & 1654 & 528 & 809 & 845 & 100.0\% \\
\bottomrule
\end{tabular}
\end{table}

\subsection{Full Interaction Model}

We estimate the following model where treatment effects vary by discipline:

$$Y_{it} = \beta_0 + \sum_{d} \beta_{1d} \cdot \text{Treatment}_i \times \text{Discipline}_d + \sum_{d} \beta_{2d} \cdot \text{Discipline}_d + \epsilon_{it}$$

\subsubsection{Outcome: Percentage Black Speakers}

\begin{table}[H]
\caption{Treatment Effects by Discipline: Percentage Black Speakers}
\centering
\begin{tabular}{lccc}
\toprule
 & (1) & (2) & (3) \\
 & Pooled Effect & By Discipline & With Controls \\
\midrule
\textbf{Treatment Effects} & & & \\
Pooled & 0.7267* & & \\
 & (0.3099) & & \\
 & & & \\
Physics & & 1.5170* & 1.5489* \\
 & & (0.5992) & (0.6294) \\
Mathematics & & 0.2645 & 0.3570 \\
 & & (0.4114) & (0.4061) \\
Chemistry & & 0.4834 & 0.2874 \\
 & & (1.0422) & (0.9901) \\
MAE & & 4.2843*** & 3.9220** \\
 & & (1.2170) & (1.2280) \\
Computer Science & & -0.1545 & 0.0967 \\
 & & (0.8006) & (0.8040) \\
\midrule
Observations & 1654 & 1654 & 1654 \\
R-squared & 0.028 & 0.034 & 0.040 \\
Controls & No & No & Yes \\
\bottomrule
\end{tabular}
\parbox{\linewidth}{\footnotesize Note: Clustered standard errors at department level in parentheses. Computer Science is the reference category. MAE = Mechanical Engineering. Controls include department ranking, total faculty, and fraction URM faculty. Significance: + p<0.1; * p<0.05; ** p<0.01; *** p<0.001.}
\end{table}

\textbf{Wald Tests: Pairwise Comparisons of Treatment Effects}

\begin{table}[H]
\caption{Pairwise Comparisons of Discipline-Specific Treatment Effects}
\centering
\begin{tabular}{lcc}
\toprule
Comparison & Difference (SE) & p-value \\
\midrule
Physics - Mathematics & 1.1920 (0.7445) & 0.1094 \\
Physics - Chemistry & 1.2616 (1.1804) & 0.2852 \\
Physics - MAE & -2.3731 (1.3725) & 0.0838+ \\
Physics - Computer Science & 1.4522 (1.0289) & 0.1581 \\
Mathematics - Chemistry & 0.0696 (1.0760) & 0.9484 \\
Mathematics - MAE & -3.5650 (1.3013) & 0.0062** \\
Mathematics - Computer Science & 0.2603 (0.9060) & 0.7739 \\
Chemistry - MAE & -3.6346 (1.5834) & 0.0217* \\
Chemistry - Computer Science & 0.1907 (1.3011) & 0.8835 \\
MAE - Computer Science & 3.8253 (1.4739) & 0.0094** \\
\bottomrule
\end{tabular}
\parbox{\linewidth}{\footnotesize Note: Based on Model 3 with controls. Positive values indicate the first discipline has a larger treatment effect. Significance: + p<0.1; * p<0.05; ** p<0.01; *** p<0.001.}
\end{table}

\subsubsection{Outcome: Any Black Speakers}

\begin{table}[H]
\caption{Treatment Effects by Discipline: Any Black Speakers}
\centering
\begin{tabular}{lccc}
\toprule
 & (1) & (2) & (3) \\
 & Pooled Effect & By Discipline & With Controls \\
\midrule
\textbf{Treatment Effects} & & & \\
Pooled & 0.0568* & & \\
 & (0.0226) & & \\
 & & & \\
Physics & & 0.0944* & 0.0972* \\
 & & (0.0477) & (0.0484) \\
Mathematics & & 0.0260 & 0.0331 \\
 & & (0.0298) & (0.0303) \\
Chemistry & & 0.0644 & 0.0558 \\
 & & (0.0686) & (0.0676) \\
MAE & & 0.3574*** & 0.3450*** \\
 & & (0.0956) & (0.0972) \\
Computer Science & & -0.0459 & -0.0321 \\
 & & (0.0710) & (0.0716) \\
\midrule
Observations & 1654 & 1654 & 1654 \\
R-squared & 0.036 & 0.045 & 0.047 \\
Controls & No & No & Yes \\
\bottomrule
\end{tabular}
\parbox{\linewidth}{\footnotesize Note: Clustered standard errors at department level in parentheses. Computer Science is the reference category. MAE = Mechanical Engineering. Controls include department ranking, total faculty, and fraction URM faculty. Significance: + p<0.1; * p<0.05; ** p<0.01; *** p<0.001.}
\end{table}

\textbf{Wald Tests: Pairwise Comparisons of Treatment Effects}

\begin{table}[H]
\caption{Pairwise Comparisons of Discipline-Specific Treatment Effects}
\centering
\begin{tabular}{lcc}
\toprule
Comparison & Difference (SE) & p-value \\
\midrule
Physics - Mathematics & 0.0641 (0.0568) & 0.2598 \\
Physics - Chemistry & 0.0414 (0.0829) & 0.6175 \\
Physics - MAE & -0.2478 (0.1079) & 0.0216* \\
Physics - Computer Science & 0.1292 (0.0871) & 0.1378 \\
Mathematics - Chemistry & -0.0227 (0.0742) & 0.7598 \\
Mathematics - MAE & -0.3119 (0.1014) & 0.0021** \\
Mathematics - Computer Science & 0.0652 (0.0776) & 0.4008 \\
Chemistry - MAE & -0.2892 (0.1181) & 0.0143* \\
Chemistry - Computer Science & 0.0879 (0.0993) & 0.3762 \\
MAE - Computer Science & 0.3770 (0.1207) & 0.0018** \\
\bottomrule
\end{tabular}
\parbox{\linewidth}{\footnotesize Note: Based on Model 3 with controls. Positive values indicate the first discipline has a larger treatment effect. Significance: + p<0.1; * p<0.05; ** p<0.01; *** p<0.001.}
\end{table}

\subsection{Summary of Exploratory Analyses}

\textbf{Key Findings:}

\begin{enumerate}
\item \textbf{Seniority Moderation:} We examined whether the treatment effect varies by speaker seniority (years since PhD). The continuous moderation analysis tests for a linear interaction between treatment and years since PhD, while the subgroup analysis compares effects for junior vs senior speakers (split at median).

\item \textbf{Discipline Moderation:} We tested whether treatment effects differ across the five academic disciplines in our sample. The full interaction model allows each discipline to have its own treatment effect, and pairwise Wald tests examine whether these differences are statistically significant.
\end{enumerate}

\textbf{Note:} These are exploratory analyses not pre-registered in our analysis plan. Results should be interpreted with appropriate caution regarding multiple testing.
