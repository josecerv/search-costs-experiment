---
title: "Search Costs Field Experiment"
date: "2025-06-10"
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
Number of seminars & 1655 \\
Number of unique departments & 528 \\
Total speakers across all seminars & 23193 \\
Mean speakers per seminar & 14.01 \\
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
URM & 7.42 & 11.10 & 1.00 & 1.28 & 54.1 \\
Black & 2.23 & 5.95 & 0.32 & 0.68 & 23.3 \\
Hispanic & 5.17 & 9.51 & 0.68 & 1.01 & 42.7 \\
Female & 16.97 & 16.17 & 2.40 & 2.47 & 76.1 \\
\bottomrule
\end{tabular}
\parbox{\linewidth}{\footnotesize Note: N =  1655  seminars. Percentages calculated among speakers with demographic data available. 'Pct. Any' indicates the percentage of seminars that have at least one speaker from that demographic group.}
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
Computer Science & 142 & 82 & 13.2 & 10.3 \\
Mathematics & 812 & 134 & 13.3 & 9.1 \\
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
Chemistry & 270 & 8.92 & 10.51 & 1.27 & 64.4 \\
Computer Science & 142 & 4.48 & 8.21 & 0.54 & 36.6 \\
Mathematics & 812 & 7.02 & 10.67 & 0.93 & 50.0 \\
Mechanical Engineering & 81 & 8.20 & 9.17 & 1.12 & 61.7 \\
Physics & 350 & 8.21 & 13.45 & 1.12 & 60.9 \\
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
Chemistry & 4.23 & 39.6 & 4.58 & 45.6 & 23.70 & 86.7 \\
Computer Science & 1.55 & 17.6 & 2.93 & 24.6 & 19.23 & 78.2 \\
Mathematics & 1.79 & 19.5 & 5.22 & 40.6 & 14.01 & 70.8 \\
Mechanical Engineering & 2.95 & 28.4 & 5.25 & 46.9 & 19.83 & 76.5 \\
Physics & 1.82 & 20.9 & 6.39 & 51.7 & 17.05 & 79.4 \\
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
Spring (1389) & 7.51 & 0.64 & 41.7 & 2.68 & 18.4 & 4.81 & 29.6 \\
\midrule
 & \multicolumn{3}{c}{Female} & \multicolumn{2}{c}{Total Speakers} & & \\
Semester & Mean \% & Mean Count & Pct. Any & Mean & SD & & \\
\midrule
Fall & 16.16 & 1.27 & 62.0 & 7.75 & 5.50 & & \\
Spring & 17.71 & 1.53 & 65.0 & 8.62 & 6.86 & & \\
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
Treatment  &  0.773$^{}$ & 0.721$^{}$ & 0.101$^{}$ & 0.076$^{}$ & 0.021$^{}$ & 0.013$^{}$  \\
 &  (0.523) & (0.515) & (0.066) & (0.064) & (0.025) & (0.023)  \\
Constant  &  7.902$^{***}$ & 3.183$^{}$ & 1.102$^{***}$ & 0.163$^{}$ & 0.573$^{***}$ & 0.197$^{+}$  \\
 &  (1.636) & (2.097) & (0.168) & (0.272) & (0.072) & (0.115)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,655 & 1,655 & 1,655 & 1,655 & 1,655 & 1,655  \\
Adjusted $R^2$ &  0.011 & 0.017 & 0.030 & 0.039 & 0.028 & 0.042  \\
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
Treatment  &  -0.508$^{}$ & -0.468$^{}$ & 0.101$^{}$ & 0.076$^{}$ & -0.609$^{}$ & -0.544$^{}$  \\
 &  (0.546) & (0.545) & (0.066) & (0.064) & (0.519) & (0.520)  \\
Constant  &  17.111$^{***}$ & 13.874$^{***}$ & 1.102$^{***}$ & 0.163$^{}$ & 16.009$^{***}$ & 13.712$^{***}$  \\
 &  (1.257) & (2.406) & (0.168) & (0.272) & (1.175) & (2.252)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,655 & 1,655 & 1,655 & 1,655 & 1,655 & 1,655  \\
Adjusted $R^2$ &  0.032 & 0.055 & 0.030 & 0.039 & 0.031 & 0.056  \\
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
URM Speakers & 0.1006 & (0.0630) \\
Non-URM Speakers & -0.6088 & (0.4599) \\
\midrule
Sum of Effects & -0.5081 & --- \\
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
Treatment  &  0.676$^{*}$ & 0.660$^{*}$ & 0.084$^{*}$ & 0.083$^{*}$ & 0.056$^{*}$ & 0.055$^{*}$  \\
 &  (0.308) & (0.294) & (0.039) & (0.038) & (0.023) & (0.023)  \\
Constant  &  2.714$^{***}$ & 0.929$^{}$ & 0.428$^{***}$ & 0.103$^{}$ & 0.287$^{***}$ & 0.051$^{}$  \\
 &  (0.791) & (1.301) & (0.103) & (0.167) & (0.061) & (0.104)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,655 & 1,655 & 1,655 & 1,655 & 1,655 & 1,655  \\
Adjusted $R^2$ &  0.026 & 0.031 & 0.048 & 0.056 & 0.036 & 0.044  \\
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
Treatment  &  0.111$^{}$ & 0.067$^{}$ & 0.017$^{}$ & -0.009$^{}$ & -0.017$^{}$ & -0.029$^{}$  \\
 &  (0.455) & (0.469) & (0.049) & (0.048) & (0.025) & (0.025)  \\
Constant  &  4.976$^{***}$ & 2.037$^{}$ & 0.648$^{***}$ & 0.023$^{}$ & 0.429$^{***}$ & 0.141$^{}$  \\
 &  (1.496) & (1.865) & (0.138) & (0.209) & (0.074) & (0.106)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,655 & 1,655 & 1,655 & 1,655 & 1,655 & 1,655  \\
Adjusted $R^2$ &  0.006 & 0.006 & 0.015 & 0.022 & 0.020 & 0.026  \\
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
Treatment  &  0.341$^{}$ & -0.126$^{}$ & -0.061$^{}$ & -0.122$^{}$ & 0.005$^{}$ & 0.001$^{}$  \\
 &  (0.836) & (0.830) & (0.128) & (0.128) & (0.022) & (0.022)  \\
Constant  &  22.012$^{***}$ & 13.852$^{***}$ & 3.650$^{***}$ & 2.285$^{***}$ & 0.872$^{***}$ & 0.691$^{***}$  \\
 &  (2.105) & (4.017) & (0.339) & (0.592) & (0.061) & (0.100)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,655 & 1,655 & 1,655 & 1,655 & 1,655 & 1,655  \\
Adjusted $R^2$ &  0.051 & 0.059 & 0.083 & 0.098 & 0.016 & 0.026  \\
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
Treatment  &  0.024$^{}$ & -0.040$^{}$ & 0.021$^{}$ & 0.014$^{}$ & 0.014$^{}$ & 0.008$^{}$  \\
 &  (0.172) & (0.183) & (0.019) & (0.019) & (0.017) & (0.017)  \\
Constant  &  1.802$^{**}$ & -0.051$^{}$ & 0.206$^{***}$ & -0.002$^{}$ & 0.175$^{***}$ & -0.014$^{}$  \\
 &  (0.604) & (0.582) & (0.060) & (0.091) & (0.049) & (0.078)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,655 & 1,655 & 1,655 & 1,655 & 1,655 & 1,655  \\
Adjusted $R^2$ &  0.014 & 0.019 & 0.040 & 0.049 & 0.040 & 0.048  \\
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
Treatment  &  0.145$^{*}$ & 0.155$^{*}$ & 0.012$^{}$ & 0.013$^{}$ & 0.014$^{+}$ & 0.015$^{+}$  \\
 &  (0.069) & (0.072) & (0.009) & (0.009) & (0.008) & (0.008)  \\
Constant  &  0.484$^{**}$ & 0.068$^{}$ & 0.056$^{*}$ & 0.003$^{}$ & 0.044$^{*}$ & 0.003$^{}$  \\
 &  (0.152) & (0.271) & (0.024) & (0.042) & (0.020) & (0.036)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,655 & 1,655 & 1,655 & 1,655 & 1,655 & 1,655  \\
Adjusted $R^2$ &  0.032 & 0.035 & 0.024 & 0.029 & 0.020 & 0.025  \\
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
Treatment  &  0.531$^{*}$ & 0.506$^{*}$ & 0.072$^{*}$ & 0.071$^{*}$ & 0.059$^{**}$ & 0.058$^{**}$  \\
 &  (0.264) & (0.248) & (0.034) & (0.033) & (0.022) & (0.022)  \\
Constant  &  2.229$^{**}$ & 0.860$^{}$ & 0.363$^{***}$ & 0.097$^{}$ & 0.278$^{***}$ & 0.035$^{}$  \\
 &  (0.709) & (1.165) & (0.092) & (0.142) & (0.060) & (0.102)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,655 & 1,655 & 1,655 & 1,655 & 1,655 & 1,655  \\
Adjusted $R^2$ &  0.018 & 0.022 & 0.040 & 0.047 & 0.035 & 0.043  \\
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
Treatment  &  -0.125$^{}$ & -0.202$^{}$ & 0.006$^{}$ & -0.000$^{}$ & 0.003$^{}$ & -0.003$^{}$  \\
 &  (0.161) & (0.175) & (0.013) & (0.013) & (0.012) & (0.012)  \\
Constant  &  1.293$^{*}$ & -0.163$^{}$ & 0.061$^{}$ & -0.063$^{}$ & 0.055$^{}$ & -0.066$^{}$  \\
 &  (0.588) & (0.486) & (0.044) & (0.066) & (0.034) & (0.057)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,655 & 1,655 & 1,655 & 1,655 & 1,655 & 1,655  \\
Adjusted $R^2$ &  0.002 & 0.004 & 0.009 & 0.016 & 0.008 & 0.015  \\
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
Treatment  &  0.236$^{}$ & 0.269$^{}$ & 0.010$^{}$ & -0.009$^{}$ & -0.018$^{}$ & -0.029$^{}$  \\
 &  (0.387) & (0.397) & (0.044) & (0.043) & (0.025) & (0.025)  \\
Constant  &  3.683$^{**}$ & 2.199$^{}$ & 0.581$^{***}$ & 0.084$^{}$ & 0.425$^{***}$ & 0.156$^{}$  \\
 &  (1.314) & (1.634) & (0.116) & (0.178) & (0.074) & (0.106)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,655 & 1,655 & 1,655 & 1,655 & 1,655 & 1,655  \\
Adjusted $R^2$ &  0.008 & 0.007 & 0.014 & 0.021 & 0.020 & 0.026  \\
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
Treatment  &  0.516$^{}$ & -0.291$^{}$ & -0.101$^{}$ & -0.174$^{}$ & 0.027$^{}$ & 0.005$^{}$  \\
 &  (1.173) & (1.162) & (0.165) & (0.165) & (0.052) & (0.057)  \\
Constant  &  5.938$^{*}$ & -2.041$^{}$ & 0.894$^{*}$ & -0.763$^{}$ & 0.197$^{}$ & -0.304$^{}$  \\
 &  (2.653) & (5.789) & (0.408) & (0.779) & (0.130) & (0.266)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  270 & 270 & 270 & 270 & 270 & 270  \\
Adjusted $R^2$ &  -0.025 & -0.021 & 0.101 & 0.107 & 0.111 & 0.119  \\
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
Treatment  &  -0.158$^{}$ & -0.649$^{}$ & -0.135$^{}$ & -0.219$^{+}$ & -0.101$^{}$ & -0.142$^{*}$  \\
 &  (0.974) & (0.985) & (0.116) & (0.125) & (0.063) & (0.063)  \\
Constant  &  2.845$^{}$ & 4.591$^{}$ & 0.548$^{}$ & 0.580$^{}$ & 0.223$^{}$ & 0.246$^{}$  \\
 &  (1.778) & (4.882) & (0.359) & (0.546) & (0.161) & (0.303)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  270 & 270 & 270 & 270 & 270 & 270  \\
Adjusted $R^2$ &  -0.025 & -0.022 & 0.047 & 0.075 & 0.037 & 0.061  \\
\bottomrule
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize \vspace{2pt}Clustered standard errors at department level in parentheses.}}\\
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize $^{+}p<0.1$; $^{*}p<0.05$; $^{**}p<0.01$; $^{***}p<0.001$\vspace{2pt}}}\\
\end{tabularx}
\end{table}

\subsubsection{Mathematics (N=812)}

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
Treatment  &  1.080$^{}$ & 1.330$^{+}$ & 0.183$^{+}$ & 0.183$^{+}$ & 0.026$^{}$ & 0.017$^{}$  \\
 &  (0.727) & (0.793) & (0.093) & (0.101) & (0.034) & (0.032)  \\
Constant  &  5.667$^{***}$ & 4.366$^{}$ & 0.786$^{***}$ & -0.028$^{}$ & 0.484$^{***}$ & 0.143$^{}$  \\
 &  (1.385) & (4.164) & (0.129) & (0.514) & (0.067) & (0.186)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  812 & 812 & 812 & 812 & 812 & 812  \\
Adjusted $R^2$ &  0.002 & 0.000 & 0.002 & 0.001 & -0.009 & 0.001  \\
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
Treatment  &  0.229$^{}$ & 0.513$^{}$ & 0.080$^{}$ & 0.116$^{*}$ & 0.022$^{}$ & 0.032$^{}$  \\
 &  (0.392) & (0.428) & (0.049) & (0.054) & (0.029) & (0.027)  \\
Constant  &  0.908$^{+}$ & 1.732$^{}$ & 0.191$^{**}$ & 0.326$^{}$ & 0.166$^{**}$ & 0.045$^{}$  \\
 &  (0.532) & (2.406) & (0.072) & (0.262) & (0.051) & (0.150)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  812 & 812 & 812 & 812 & 812 & 812  \\
Adjusted $R^2$ &  0.012 & 0.020 & 0.011 & 0.023 & 0.006 & 0.019  \\
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
Treatment  &  0.869$^{}$ & 0.821$^{}$ & 0.107$^{}$ & 0.067$^{}$ & 0.029$^{}$ & 0.011$^{}$  \\
 &  (0.627) & (0.676) & (0.071) & (0.068) & (0.033) & (0.035)  \\
Constant  &  4.683$^{***}$ & 2.482$^{}$ & 0.577$^{***}$ & -0.390$^{}$ & 0.384$^{***}$ & 0.117$^{}$  \\
 &  (1.262) & (3.194) & (0.106) & (0.376) & (0.073) & (0.184)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  812 & 812 & 812 & 812 & 812 & 812  \\
Adjusted $R^2$ &  -0.004 & -0.003 & -0.000 & 0.004 & -0.002 & -0.000  \\
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
Treatment  &  0.227$^{}$ & 0.131$^{}$ & 0.150$^{}$ & 0.126$^{}$ & -0.005$^{}$ & -0.004$^{}$  \\
 &  (1.191) & (1.161) & (0.131) & (0.130) & (0.059) & (0.051)  \\
Constant  &  13.463$^{***}$ & 6.977$^{}$ & 1.248$^{***}$ & 1.542$^{}$ & 0.408$^{***}$ & 0.871$^{}$  \\
 &  (2.401) & (13.865) & (0.170) & (1.447) & (0.074) & (0.555)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  350 & 350 & 350 & 350 & 350 & 350  \\
Adjusted $R^2$ &  0.004 & -0.003 & 0.003 & 0.010 & 0.002 & 0.032  \\
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
Treatment  &  -1.251$^{}$ & -1.473$^{}$ & -0.024$^{}$ & -0.056$^{}$ & -0.067$^{}$ & -0.069$^{}$  \\
 &  (1.177) & (1.180) & (0.114) & (0.116) & (0.064) & (0.059)  \\
Constant  &  13.679$^{***}$ & 7.068$^{}$ & 1.217$^{***}$ & 1.313$^{}$ & 0.436$^{***}$ & 0.780$^{}$  \\
 &  (2.400) & (12.765) & (0.153) & (1.192) & (0.081) & (0.574)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  350 & 350 & 350 & 350 & 350 & 350  \\
Adjusted $R^2$ &  -0.000 & -0.007 & -0.008 & 0.011 & -0.003 & 0.011  \\
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

## Testing for Significant Moderation Across Disciplines

\textbf{F-test for Treatment × Discipline Interactions (Black Speakers):}
F-statistic: 3.608 
p-value: 0.0062 
Degrees of freedom: 4 

The treatment effect on Black speaker representation varies significantly across disciplines (p < 0.05).
This indicates that the diversity intervention has heterogeneous effects depending on the academic field.

\textbf{F-test for Treatment × Discipline Interactions (URM Speakers):}
F-statistic: 0.649 
p-value: 0.6276 
Degrees of freedom: 4 

\textbf{F-test for Treatment × Discipline Interactions (% Black Speakers):}
F-statistic: 2.431 
p-value: 0.0458 
Degrees of freedom: 4 

\textbf{F-test for Treatment × Discipline Interactions (Total Black Speakers):}
F-statistic: 4.13 
p-value: 0.0025 
Degrees of freedom: 4 

\textbf{Individual Interaction Effects (Black Speakers):}
                                      Estimate Std. Error t value Pr(>|t|)
treatment:disc_mathematics             -0.0584     0.0605 -0.9662   0.3341
treatment:disc_physics                  0.0222     0.0685  0.3244   0.7457
treatment:disc_computer_science        -0.1074     0.0879 -1.2225   0.2217
treatment:disc_mechanical_engineering   0.2797     0.1059  2.6419   0.0083

\newpage

# Semester-Specific Analysis

## Fall Semester


Call:
lm(formula = as.formula(formula_str), data = data_complete)

Residuals:
    Min      1Q  Median      3Q     Max 
-12.605  -7.477  -4.980   3.554  95.007 

Coefficients:
                            Estimate Std. Error t value Pr(>|t|)   
(Intercept)                  6.35696    2.14015   2.970  0.00302 **
treatment                    0.94922    0.72180   1.315  0.18870   
bin_0_1                      1.48922    1.89568   0.786  0.43224   
bin_1_3                      1.14316    1.82433   0.627  0.53101   
bin_3_5                      2.00801    1.74786   1.149  0.25081   
bin_5_7                     -0.03272    1.74150  -0.019  0.98501   
bin_7_11                     2.18899    1.68911   1.296  0.19520   
bin_11_17                   -1.42973    1.67659  -0.853  0.39393   
disc_mathematics             0.05245    1.19124   0.044  0.96489   
disc_physics                 0.34638    1.21922   0.284  0.77637   
disc_computer_science       -4.91430    1.54564  -3.179  0.00151 **
disc_mechanical_engineering -2.70485    1.89142  -1.430  0.15292   
batch_1                      0.87044    1.66325   0.523  0.60082   
batch_2                      1.38845    1.96032   0.708  0.47889   
batch_3                     -2.13347    1.55207  -1.375  0.16947   
batch_4                      2.76342    1.55058   1.782  0.07493 . 
batch_5                      0.89058    1.51030   0.590  0.55551   
batch_6                     -0.14252    1.51698  -0.094  0.92516   
batch_7                     -1.22984    1.50242  -0.819  0.41317   
batch_8                      0.61867    1.60368   0.386  0.69972   
batch_9                     -2.64601    1.53713  -1.721  0.08539 . 
---
Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1

Residual standard error: 13.5 on 1427 degrees of freedom
Multiple R-squared:  0.03113,	Adjusted R-squared:  0.01755 
F-statistic: 2.292 on 20 and 1427 DF,  p-value: 0.000971

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
Treatment  &  0.783$^{}$ & 0.878$^{}$ & 0.027$^{}$ & 0.030$^{}$ & -0.007$^{}$ & -0.007$^{}$  \\
 &  (0.744) & (0.777) & (0.055) & (0.056) & (0.029) & (0.028)  \\
Constant  &  7.449$^{***}$ & 6.781$^{*}$ & 0.886$^{***}$ & 0.761$^{**}$ & 0.509$^{***}$ & 0.378$^{**}$  \\
 &  (1.709) & (2.884) & (0.140) & (0.240) & (0.075) & (0.121)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,389 & 1,389 & 1,389 & 1,389 & 1,389 & 1,389  \\
Adjusted $R^2$ &  0.006 & 0.006 & 0.024 & 0.022 & 0.025 & 0.028  \\
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
Treatment  &  0.822$^{+}$ & 0.820$^{+}$ & 0.038$^{}$ & 0.040$^{}$ & 0.028$^{}$ & 0.030$^{}$  \\
 &  (0.460) & (0.440) & (0.035) & (0.034) & (0.023) & (0.023)  \\
Constant  &  1.802$^{+}$ & 1.456$^{}$ & 0.315$^{***}$ & 0.301$^{*}$ & 0.230$^{***}$ & 0.174$^{+}$  \\
 &  (1.023) & (1.712) & (0.088) & (0.147) & (0.059) & (0.100)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,389 & 1,389 & 1,389 & 1,389 & 1,389 & 1,389  \\
Adjusted $R^2$ &  0.010 & 0.010 & 0.032 & 0.034 & 0.023 & 0.022  \\
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
Treatment  &  -0.018$^{}$ & 0.072$^{}$ & -0.010$^{}$ & -0.011$^{}$ & -0.030$^{}$ & -0.031$^{}$  \\
 &  (0.628) & (0.675) & (0.040) & (0.040) & (0.026) & (0.027)  \\
Constant  &  5.424$^{***}$ & 5.097$^{*}$ & 0.553$^{***}$ & 0.438$^{**}$ & 0.389$^{***}$ & 0.296$^{**}$  \\
 &  (1.403) & (2.466) & (0.097) & (0.169) & (0.071) & (0.103)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,389 & 1,389 & 1,389 & 1,389 & 1,389 & 1,389  \\
Adjusted $R^2$ &  -0.004 & -0.003 & 0.008 & 0.010 & 0.014 & 0.017  \\
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
Treatment  &  0.729$^{}$ & 0.710$^{}$ & 0.101$^{}$ & 0.068$^{}$ & 0.022$^{}$ & 0.011$^{}$  \\
 &  (0.515) & (0.512) & (0.065) & (0.063) & (0.025) & (0.023)  \\
Constant  &  9.084$^{***}$ & 4.778$^{*}$ & 1.059$^{***}$ & 0.220$^{}$ & 0.515$^{***}$ & 0.185$^{+}$  \\
 &  (1.636) & (1.962) & (0.178) & (0.249) & (0.079) & (0.109)  \\
Dept Ranking (centered)  &  0.015$^{}$ & 0.029$^{*}$ & -0.003$^{*}$ & -0.001$^{}$ & -0.002$^{**}$ & -0.001$^{}$  \\
 &  (0.013) & (0.013) & (0.001) & (0.001) & (0.001) & (0.001)  \\
Treatment $\times$ Dept Ranking (centered)  &  0.008$^{}$ & 0.007$^{}$ & 0.005$^{*}$ & 0.005$^{**}$ & 0.001$^{}$ & 0.001$^{+}$  \\
 &  (0.016) & (0.016) & (0.002) & (0.002) & (0.001) & (0.001)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,655 & 1,655 & 1,655 & 1,655 & 1,655 & 1,655  \\
Adjusted $R^2$ &  0.013 & 0.017 & 0.034 & 0.044 & 0.031 & 0.043  \\
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
Treatment  &  0.958$^{+}$ & 0.744$^{}$ & 0.080$^{}$ & 0.072$^{}$ & 0.012$^{}$ & 0.014$^{}$  \\
 &  (0.531) & (0.511) & (0.068) & (0.064) & (0.025) & (0.024)  \\
Constant  &  7.792$^{***}$ & 2.224$^{}$ & 1.087$^{***}$ & 0.191$^{}$ & 0.551$^{***}$ & 0.185$^{+}$  \\
 &  (1.568) & (2.043) & (0.177) & (0.279) & (0.071) & (0.111)  \\
Total Faculty (centered)  &  -0.039$^{}$ & -0.032$^{}$ & 0.003$^{}$ & 0.002$^{}$ & 0.001$^{}$ & -0.001$^{}$  \\
 &  (0.026) & (0.026) & (0.003) & (0.003) & (0.001) & (0.001)  \\
Treatment $\times$ Total Faculty (centered)  &  0.030$^{}$ & 0.016$^{}$ & -0.001$^{}$ & -0.003$^{}$ & 0.001$^{}$ & 0.000$^{}$  \\
 &  (0.029) & (0.028) & (0.003) & (0.003) & (0.001) & (0.001)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,655 & 1,655 & 1,655 & 1,655 & 1,655 & 1,655  \\
Adjusted $R^2$ &  0.012 & 0.017 & 0.030 & 0.039 & 0.029 & 0.041  \\
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
Treatment  &  0.779$^{}$ & 0.696$^{}$ & 0.105$^{}$ & 0.073$^{}$ & 0.022$^{}$ & 0.013$^{}$  \\
 &  (0.519) & (0.516) & (0.064) & (0.064) & (0.025) & (0.023)  \\
Constant  &  7.738$^{***}$ & 6.936$^{***}$ & 1.054$^{***}$ & 0.760$^{***}$ & 0.552$^{***}$ & 0.409$^{***}$  \\
 &  (1.569) & (1.811) & (0.162) & (0.220) & (0.069) & (0.098)  \\
Peer URM Faculty (centered)  &  0.072$^{}$ & 0.145$^{**}$ & 0.017$^{**}$ & 0.021$^{***}$ & 0.007$^{**}$ & 0.007$^{**}$  \\
 &  (0.053) & (0.054) & (0.005) & (0.006) & (0.002) & (0.002)  \\
Treatment $\times$ Peer URM Faculty (centered)  &  -0.064$^{}$ & -0.054$^{}$ & -0.004$^{}$ & -0.006$^{}$ & -0.001$^{}$ & -0.001$^{}$  \\
 &  (0.072) & (0.071) & (0.008) & (0.008) & (0.003) & (0.003)  \\
\midrule
Controls &  Simple & Extended & Simple & Extended & Simple & Extended  \\
N &  1,655 & 1,655 & 1,655 & 1,655 & 1,655 & 1,655  \\
Adjusted $R^2$ &  0.011 & 0.017 & 0.037 & 0.039 & 0.037 & 0.041  \\
\bottomrule
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize \vspace{2pt}Clustered standard errors at department level in parentheses.}}\\
\multicolumn{7}{l}{\parbox{\linewidth}{\footnotesize $^{+}p<0.1$; $^{*}p<0.05$; $^{**}p<0.01$; $^{***}p<0.001$\vspace{2pt}}}\\
\end{tabularx}
\end{table}

\newpage

## Exploratory Analysis: Seniority Moderation

### Analysis 1: Does speaker seniority moderate the treatment effect?


\clearpage
\section{Exploratory Analysis: Seniority Moderation}

\subsection{Distribution of Years Since PhD}

\textbf{Seniority Data Coverage:}

- Total seminars with seniority data: 1626 (98.2\% of total)
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
Treatment & 0.8064* & 0.8236* & 0.8952** \\
 & (0.3340) & (0.3429) & (0.3272) \\
Years Since PhD (centered) & -0.0161 & -0.0045 & -0.0043 \\
 & (0.0187) & (0.0228) & (0.0227) \\
Treatment × Years Since PhD &   & -0.0260 & -0.0323 \\
 &   & (0.0385) & (0.0386) \\
\midrule
Observations & 1626 & 1626 & 1626 \\
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
Treatment & 0.0644** & 0.0621** & 0.0700** \\
 & (0.0239) & (0.0240) & (0.0237) \\
Years Since PhD (centered) & 0.0001 & -0.0015 & -0.0015 \\
 & (0.0013) & (0.0016) & (0.0016) \\
Treatment × Years Since PhD &   & 0.0036 & 0.0032 \\
 &   & (0.0027) & (0.0026) \\
\midrule
Observations & 1626 & 1626 & 1626 \\
R-squared & 0.006 & 0.007 & 0.015 \\
Controls & No & No & Yes \\
\bottomrule
\end{tabular}
\parbox{\linewidth}{\footnotesize Note: Clustered standard errors at department level in parentheses. Years since PhD is the mean years since PhD for speakers in each seminar, centered at the median. Controls include department ranking, total faculty, and fraction URM faculty. Significance: + p<0.1; * p<0.05; ** p<0.01; *** p<0.001.}
\end{table}

\subsection{Subgroup Analysis: Seminars with Senior vs Junior Speakers}

\textbf{Median Split Groups:}

- Seminars with junior speakers (n=813): Mean = 10.0 years, Range = 1.0-15.1 years
- Seminars with senior speakers (n=813): Mean = 21.5 years, Range = 15.1-59.0 years

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
Treatment & 1.0086* & 1.1326* & 0.5771 & 0.6213 \\
 & (0.4807) & (0.4807) & (0.4163) & (0.4000) \\
\midrule
Observations & 813 & 813 & 813 & 813 \\
R-squared & 0.006 & 0.023 & 0.003 & 0.010 \\
Controls & No & Yes & No & Yes \\
\bottomrule
\end{tabular}
\parbox{\linewidth}{\footnotesize Note: Clustered standard errors at department level in parentheses. Junior/Senior split at median of seminar-level mean years since PhD. Controls include department ranking, total faculty, and fraction URM faculty. Significance: + p<0.1; * p<0.05; ** p<0.01; *** p<0.001.}
\end{table}

\textbf{Test for Difference Between Groups:}

Difference in treatment effect (Senior - Junior): -0.4315 (SE = 0.6025), p = 0.4739

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
Treatment & 0.0344 & 0.0451 & 0.0916** & 0.0943** \\
 & (0.0303) & (0.0306) & (0.0341) & (0.0340) \\
\midrule
Observations & 813 & 813 & 813 & 813 \\
R-squared & 0.002 & 0.007 & 0.011 & 0.021 \\
Controls & No & Yes & No & Yes \\
\bottomrule
\end{tabular}
\parbox{\linewidth}{\footnotesize Note: Clustered standard errors at department level in parentheses. Junior/Senior split at median of seminar-level mean years since PhD. Controls include department ranking, total faculty, and fraction URM faculty. Significance: + p<0.1; * p<0.05; ** p<0.01; *** p<0.001.}
\end{table}

\textbf{Test for Difference Between Groups:}

Difference in treatment effect (Senior - Junior): 0.0571 (SE = 0.0437), p = 0.1914


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
Chemistry & Any Hispanic & Treatment & Extended & -0.1418 & 0.0630 & -2.250 & 0.0253 & * \\
Chemistry & Count Hispanic & Treatment & Extended & -0.2186 & 0.1246 & -1.755 & 0.0805 & + \\
Computer Science & Any Hispanic & Treatment & Extended & 0.1556 & 0.0892 & 1.745 & 0.0836 & + \\
Mathematics & \% URM & Treatment & Extended & 1.3298 & 0.7933 & 1.676 & 0.0941 & + \\
Mathematics & Count Black & Treatment & Extended & 0.1164 & 0.0542 & 2.146 & 0.0322 & * \\
Mathematics & Count URM & Treatment & Simple & 0.1828 & 0.0935 & 1.956 & 0.0508 & + \\
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
Demographic Subgroup & \% Black & Treatment & Extended & 0.6604 & 0.2936 & 2.249 & 0.0246 & * \\
Demographic Subgroup & \% Black Female & Treatment & Extended & 0.1546 & 0.0720 & 2.146 & 0.0320 & * \\
Demographic Subgroup & \% Black Male & Treatment & Extended & 0.5058 & 0.2483 & 2.037 & 0.0418 & * \\
Demographic Subgroup & Any Black & Treatment & Simple & 0.0558 & 0.0227 & 2.457 & 0.0141 & * \\
Demographic Subgroup & Any Black Female & Treatment & Extended & 0.0149 & 0.0081 & 1.837 & 0.0663 & + \\
Demographic Subgroup & Any Black Male & Treatment & Simple & 0.0590 & 0.0225 & 2.625 & 0.0087 & ** \\
Demographic Subgroup & Count Black & Treatment & Extended & 0.0826 & 0.0377 & 2.192 & 0.0285 & * \\
Demographic Subgroup & Count Black Male & Treatment & Extended & 0.0710 & 0.0326 & 2.176 & 0.0297 & * \\
\addlinespace[0.5em]
\multicolumn{9}{l}{\textbf{Moderation Analysis}} \\
\midrule
Department Rank & Any URM & Treatment $\times$ Dept Ranking & Extended & 0.0012 & 0.0006 & 1.796 & 0.0727 & + \\
Department Rank & Count URM & Treatment $\times$ Dept Ranking & Extended & 0.0050 & 0.0018 & 2.809 & 0.0050 & ** \\
Faculty Size & \% URM & Treatment & Simple & 0.9579 & 0.5308 & 1.805 & 0.0713 & + \\
\addlinespace[0.5em]
\multicolumn{9}{l}{\textbf{Semester Analysis}} \\
\midrule
Fall Semester & Any Black & Treatment & Simple & 0.0434 & 0.0167 & 2.603 & 0.0093 & ** \\
Fall Semester & Count Black & Treatment & Simple & 0.0531 & 0.0209 & 2.541 & 0.0112 & * \\
Fall Semester & Count URM & Treatment & Simple & 0.0780 & 0.0456 & 1.711 & 0.0873 & + \\
Spring Semester & \% Black & Treatment & Extended & 0.8204 & 0.4401 & 1.864 & 0.0625 & + \\
\bottomrule
\end{tabular}
} % End group for scriptsize and tabcolsep
\parbox{\linewidth}{\footnotesize Note: Significance levels: + p<0.1; * p<0.05; ** p<0.01; *** p<0.001. SE = Clustered standard errors at department level. Constant terms are excluded from this summary.}
\end{table}
